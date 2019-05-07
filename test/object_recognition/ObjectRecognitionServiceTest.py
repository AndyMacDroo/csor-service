import unittest

from src.object_recognition.ObjectRecognitionService import ObjectRecognitionService


class ObjectRecognitionServiceTest(unittest.TestCase):

    def setUp(self):
        pass

    def test_object_recognition_service_returns_video_stream_on_get_video_stream(self):
        video_stream = { "name" : "mockStream" }
        object_recognition_service = ObjectRecognitionService(config={}, video_stream=video_stream)
        self.assertEqual(video_stream, object_recognition_service.get_video_stream())

    def test_object_recognition_service_generates_expected_recognition_event(self):
        object_recognition_service = ObjectRecognitionService(config={}, video_stream={})
        event_from_stream = object_recognition_service.read_stream_for_event()
        self.assertEqual({}, event_from_stream)

    def test_object_recognition_service_generates_expected_error_with_none_stream(self):
        with self.assertRaises(ValueError) as context:
            ObjectRecognitionService(config={}, video_stream=None)
        self.assertTrue('Cannot pass None as stream' in str(context.exception))



if __name__ == '__main__':
    unittest.main()