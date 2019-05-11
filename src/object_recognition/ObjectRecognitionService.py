from src.log.Log import LOG
import cv2 as cv
import numpy as np

from src.yolo.yolo_utils import infer_image


class ObjectRecognitionService:

    def __init__(self, config, video_stream):
        self.config = config
        if video_stream is None:
            raise ValueError("Cannot pass None as stream")
        self.video_stream = video_stream
        self.count = 0
        if self.config.debug:
            LOG.info("Initialised ObjectRecognitionService")
        try:
            self.labels = open(config.labels).read().strip().split('\n')
            self.colors = np.random.randint(0, 255, size=(len(self.labels), 3), dtype='uint8')
            if self.config.debug:
                LOG.info("ObjectRecognitionService found recognition labels %s" % self.labels)
            self.net = cv.dnn.readNetFromDarknet(config.config, config.weights)
            # Get the output layer names of the model
            self.layer_names = self.net.getLayerNames()
            self.layer_names = [self.layer_names[i[0] - 1] for i in self.net.getUnconnectedOutLayers()]
        except AttributeError:
            self.labels = []
            self.net, self.layer_names, self.colors = [],[],[]
            LOG.warn("ObjectRecognitionService found no recognition labels and will likely fail")


    def read_stream_for_event(self):
        if self.config.debug:
            LOG.info("Reading stream for event")
        event_stream =  self.__run_recognition_check()
        if event_stream and self.config.debug:
            LOG.info("Event stream exists")
        return event_stream

    def get_video_stream(self):
        return self.video_stream

    def __run_recognition_check(self):
        _, frame = self.get_video_stream().read()
        if frame is None:
            LOG.warn("No frame detected in stream")
            return {}
        height, width = frame.shape[:2]
        if not self.net:
            return {}
        if self.count == 0:
            frame, self.boxes, self.confidences, self.classids, self.idxs = infer_image(self.net, self.layer_names, \
                                                                    height, width, frame, self.colors, self.labels, self.config)
            self.count += 1
        else:
            frame, self.boxes, self.confidences, self.classids, self.idxs = infer_image(self.net, self.layer_names, \
                                                                    height, width, frame, self.colors, self.labels, self.config, self.boxes,
                                                                    self.confidences, self.classids, self.idxs, infer=False)
            self.count = (self.count + 1) % 6
        return frame, self.boxes, self.confidences, self.classids, self.idxs, self.labels