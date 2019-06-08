import unittest
from unittest.mock import MagicMock

from src.object_recognition.ObjectRecognitionService import ObjectRecognitionService
from src.video.VideoStream import VideoStream
from test.MockConfig import MockConfig

mock_config = MockConfig()


class ObjectRecognitionServiceTest(unittest.TestCase):

    def setUp(self):
        pass

    def test_object_recognition_service_returns_video_stream_on_get_video_stream(self):
        video_stream = { "name" : "mockStream" }
        object_recognition_service = ObjectRecognitionService(config=mock_config, video_stream=video_stream)
        self.assertEqual(video_stream, object_recognition_service.get_video_stream())

    def test_object_recognition_service_generates_expected_error_with_none_stream(self):
        with self.assertRaises(ValueError) as context:
            ObjectRecognitionService(config=mock_config, video_stream=None)
        self.assertTrue("Cannot pass empty stream" in str(context.exception))


if __name__ == '__main__':
    unittest.main()