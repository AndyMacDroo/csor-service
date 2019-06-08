from threading import Thread

import cv2 as cv

from src.log.Log import LOG

DEFAULT_SUBMIT_COOL_DOWN = 8

class EventStreamAnalyser:

    def __init__(self, config, event_data_stream, event_handler):
        self.config = config
        self.event_data_stream = event_data_stream
        self.handler = event_handler
        self.submit_cool_off = 0
        if self.config.debug:
            LOG.debug("Initialised EventStreamAnalyser")

    def analyse_stream(self):
        if self.config.debug:
            LOG.debug("Checking stream for event")
        event = self.check_stream_for_event()
        if self.config.show_cam and event:
            cv.imshow('webcam', event[0])
        if event is not None and event:
            LOG.debug("Not posting for another %s frames" % self.submit_cool_off)
            if self.submit_cool_off < 0:
                self.submit_cool_off = 0
            if self.submit_cool_off == 0:
                event_notification_thread = Thread(target=self.__dispatch_notification_for_event, args=[event])
                event_notification_thread.start()
                self.submit_cool_off = DEFAULT_SUBMIT_COOL_DOWN
            elif self.submit_cool_off > 0:
                self.submit_cool_off = self.submit_cool_off - 1

    def daemon(self):
        while True:
            self.analyse_stream()
            if cv.waitKey(1) & 0xFF == ord('q'):
                break

    def check_stream_for_event(self):
        return self.event_data_stream.read_stream_for_event()

    def __dispatch_notification_for_event(self, event):
        self.handler.handle(event)

