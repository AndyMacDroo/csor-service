# Security Image Processor [![Build Status](https://travis-ci.org/AndyMacDroo/security-image-processor.svg?branch=master)](https://travis-ci.org/AndyMacDroo/security-image-processor) [![Python 3.6](https://img.shields.io/badge/python-3.6-blue.svg)](https://www.python.org/downloads/release/python-360/)

This project processes [RTSP](https://tools.ietf.org/html/rfc2326) video streams using OpenCV and the [YOLO Real-Time Object Detection Model](https://pjreddie.com/darknet/yolo/).


## Getting Started ##

**Installing Dependencies**
```sh
src/yolov3-coco/get_model.sh
pip install -r requirements.txt
```

**Running Unit Tests**
```sh
python -m unittest discover -s test -p "*Test.py"
```

## Configuration ##

**Program Arguments**

For a full list of arguments run:
`python main.py -h`
```sh
usage: main.py [-h] [-m MODEL_PATH] [-w WEIGHTS] [-cfg CONFIG] [-i IMAGE_PATH]
               [-v VIDEO_PATH] [-vo VIDEO_OUTPUT_PATH] [-l LABELS]
               [-c CONFIDENCE] [-th THRESHOLD] [-t SHOW_TIME] [-d DEBUG]
               [-sc SHOW_CAM] [-ri REFRESH_INTERVAL] [-loc STREAM_LOCATION]

```