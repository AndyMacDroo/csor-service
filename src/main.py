import schedule

from src.analysis.VideoEventHandler import VideoEventHandler
from src.analysis.EventStreamAnalyser import EventStreamAnalyser
from src.object_recognition.ObjectRecognitionService import ObjectRecognitionService
from src.video.VideoStream import VideoStream


STREAM_LOCATION = ""
event_handler = VideoEventHandler()


def run_security_image_processor():
    stream = VideoStream(stream_location=STREAM_LOCATION) # initialise the video stream
    object_recognition_service = ObjectRecognitionService(config={}, video_stream=stream)
    EventStreamAnalyser(event_data_stream=object_recognition_service, event_handler= event_handler).daemon()


if __name__ == '__main__':
    run_security_image_processor()
    while True:
        schedule.run_pending()