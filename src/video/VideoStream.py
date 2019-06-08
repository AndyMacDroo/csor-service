from src.log.Log import LOG
import threading
from multiprocessing import Queue

import cv2 as cv

frames = Queue(maxsize=14)

class VideoStream:

    def __init__(self, stream_location):
        self.stream_location = stream_location
        if stream_location.strip() == "" or stream_location is None:
            raise ValueError("Cannot pass empty stream")
        else:
            self.v_stream = cv.VideoCapture(self.stream_location)
            t = threading.Thread(target=self.run)
            t.start()

    def run(self):
        while True:
            _, frame = self.v_stream.read()
            if _:
                frames.put(frame)
            if frames.full() or not _:
                self.close()
                self.v_stream = cv.VideoCapture(self.stream_location)
                LOG.debug("Frame buffer exceeded. Restarting stream")

    def read(self):
        return True, frames.get()

    def close(self):
        self.v_stream.release()