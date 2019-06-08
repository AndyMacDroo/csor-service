from src.log.Log import LOG
import requests
import cv2 as cv


class VideoEventHandler:

    def __init__(self, config):
        self.config = config
        self.handled = False

    def handle(self, event):
        if self.config.debug:
            LOG.debug("Handling event")
        self.handled = False
        for detected in event[3]:
            if self.config.subject_of_interest in event[5][detected] and not self.handled:
                self.__upload_file_to_slack(event)

    def __upload_file_to_slack(self, event):
        cv.imwrite(self.config.tmp_file_location, event[0])
        my_file = {
            'file': (self.config.tmp_file_location, open(self.config.tmp_file_location, 'rb'), 'jpg')
        }

        payload = {
            "title" : self.config.slack_alert_title,
            "initial_comment" : "*WARNING*: A _%s_ was detected." % self.config.subject_of_interest,
            "token": self.config.slack_token,
            "channels": [self.config.slack_channel],
        }

        r = requests.post("https://slack.com/api/files.upload", params=payload, files=my_file)
        if self.config.debug:
            LOG.debug(str(r.content))
        self.handled = True