from src.log.Log import LOG
import cv2 as cv


class VideoEventHandler:

    def __init__(self, config):
        self.config = config

    def handle(self, event):
        if self.config.debug:
            LOG.info("Handling event")
            for detected in event[3]:
                LOG.info("Detected %s" % event[5][detected])
        if self.config.show_cam:
            cv.imshow('webcam', event[0])