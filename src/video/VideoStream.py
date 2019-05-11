import cv2 as cv

class VideoStream:

    def __init__(self, stream_location):
        self.stream_location = stream_location
        self.v_stream = cv.VideoCapture(stream_location)

    def read(self):
        return self.v_stream.read()

    def close(self):
        self.v_stream.release()