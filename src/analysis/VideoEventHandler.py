from src.log.Log import LOG


class VideoEventHandler:

    def __init__(self):
        pass

    def handle(self, event):
        LOG.info("Handling event %s" % event)