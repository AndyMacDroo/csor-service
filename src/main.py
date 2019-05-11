import sys
sys.path.append("..")
import schedule
import argparse
import cv2 as cv

from src.analysis.VideoEventHandler import VideoEventHandler
from src.analysis.EventStreamAnalyser import EventStreamAnalyser
from src.object_recognition.ObjectRecognitionService import ObjectRecognitionService
from src.video.VideoStream import VideoStream

# Global variable for access to close stream
STREAM = None


def run_security_image_processor(config):
    STREAM = VideoStream(stream_location=config.stream_location) # initialise the video stream
    event_handler = VideoEventHandler(config=config)
    object_recognition_service = ObjectRecognitionService(config=config, video_stream=STREAM)
    EventStreamAnalyser(config=config, event_data_stream=object_recognition_service, event_handler= event_handler).daemon()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('-m', '--model-path',
                        type=str,
                        default='./yolov3-coco/',
                        help='The directory where the model weights and \
    			  configuration files are.')

    parser.add_argument('-w', '--weights',
                        type=str,
                        default='./yolov3-coco/yolov3.weights',
                        help='Path to the file which contains the weights \
    			 	for YOLOv3.')

    parser.add_argument('-cfg', '--config',
                        type=str,
                        default='./yolov3-coco/yolov3.cfg',
                        help='Path to the configuration file for the YOLOv3 model.')

    parser.add_argument('-i', '--image-path',
                        type=str,
                        help='The path to the image file')

    parser.add_argument('-v', '--video-path',
                        type=str,
                        help='The path to the video file')

    parser.add_argument('-vo', '--video-output-path',
                        type=str,
                        default='./output.avi',
                        help='The path of the output video file')

    parser.add_argument('-l', '--labels',
                        type=str,
                        default='./yolov3-coco/coco-labels',
                        help='Path to the file having the \
    					labels in a new-line seperated way.')

    parser.add_argument('-c', '--confidence',
                        type=float,
                        default=0.5,
                        help='The model will reject boundaries which has a \
    				probabiity less than the confidence value. \
    				default: 0.5')

    parser.add_argument('-th', '--threshold',
                        type=float,
                        default=0.3,
                        help='The threshold to use when applying the \
    				Non-Max Suppresion')

    parser.add_argument('-t', '--show-time',
                        type=bool,
                        default=False,
                        help='Show the time taken to infer each image.')

    parser.add_argument('-d', '--debug',
                        type=bool,
                        default=True,
                        help='Global debug mode')

    parser.add_argument('-sc', '--show-cam',
                        type=bool,
                        default=True,
                        help='Show camera')

    parser.add_argument('-ri', '--refresh-interval',
                        type=int,
                        default=0.1,
                        help='Camera refresh interval')

    parser.add_argument('-loc', '--stream-location',
                        type=str,
                        default='http://82.215.168.242:8083/mjpg/video.mjpg',
                        help='Stream location')

    config, unparsed = parser.parse_known_args()
    run_security_image_processor(config)
    while True:
        schedule.run_pending()
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    STREAM.close()
    cv.destroyAllWindows()