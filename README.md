# CSORS - Camera Stream Object Recognition Service [![Build Status](https://travis-ci.org/AndyMacDroo/csor-service.svg?branch=master)](https://travis-ci.org/AndyMacDroo/csor-service) [![Python 3.6](https://img.shields.io/badge/python-3.6-blue.svg)](https://www.python.org/downloads/release/python-360/)

This project processes [RTSP](https://tools.ietf.org/html/rfc2326) video streams using OpenCV and the [YOLO Real-Time Object Detection Model](https://pjreddie.com/darknet/yolo/).

Frames containing a _"subject of interest"_ are posted to a slack channel.


## Getting Started ##

**Create Slack Bot Account**

Follow Slack documentation for [Bot-Users](https://api.slack.com/bot-users).

**Installing Dependencies**
```sh
src/yolov3-coco/get_model.sh && pip install -r requirements.txt
```

**Running Unit Tests**
```sh
python -m unittest discover -s test -p "*Test.py"
```

## Usage ##

Simply pass a suitable RTSP stream URL as an argument when running the application:

```sh
python src/main.py -loc http://82.215.168.242:8083/mjpg/video.mjpg
```

For a full list of arguments run:
`python src/main.py -h`
```sh
usage: main.py [-h] [-m MODEL_PATH] [-w WEIGHTS] [-cfg CONFIG] [-i IMAGE_PATH]
               [-v VIDEO_PATH] [-l LABELS] [-c CONFIDENCE] [-th THRESHOLD]
               [-t SHOW_TIME] [-d DEBUG] [-sc SHOW_CAM] [-ri REFRESH_INTERVAL]
               [-loc STREAM_LOCATION] [-stok SLACK_TOKEN]
               [-stit SLACK_ALERT_TITLE] [-schan SLACK_CHANNEL]
               [-tdir TMP_FILE_LOCATION] [-subj SUBJECT_OF_INTEREST]
```