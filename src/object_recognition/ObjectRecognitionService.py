from src.log.Log import LOG


class ObjectRecognitionService:

    def __init__(self, config, video_stream):
        self.config = config
        if video_stream is None:
            raise ValueError("Cannot pass None as stream")
        self.video_stream = video_stream
        LOG.info("Initialised ObjectRecognitionService")

    def read_stream_for_event(self):
        return self.__run_recognition_check()

    def get_video_stream(self):
        return self.video_stream

    def __run_recognition_check(self):
        return {}