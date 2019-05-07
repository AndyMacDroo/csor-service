import schedule

from src.log.Log import LOG


class EventStreamAnalyser:

    def __init__(self, event_data_stream, event_handler):
        self.event_data_stream = event_data_stream
        self.handler = event_handler
        LOG.info("Initialised EventStreamAnalyser")

    def analyse_stream(self):
        LOG.info("Checking stream for event")
        event = self.check_stream_for_event()
        if event is not None and event:
            LOG.info("Event found")
            self.__dispatch_notification_for_event(event)

    def daemon(self):
        self.__configure_schedule_for_job().do(self.analyse_stream)

    def check_stream_for_event(self):
        return self.event_data_stream.read_stream_for_event()

    def __dispatch_notification_for_event(self, event):
        self.handler.handle(event)

    def __configure_schedule_for_job(self):
        return schedule.every(1).seconds
