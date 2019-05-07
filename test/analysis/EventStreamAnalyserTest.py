import unittest
from unittest.mock import MagicMock

from src.analysis.EventStreamAnalyser import EventStreamAnalyser
from src.analysis.VideoEventHandler import VideoEventHandler
from src.object_recognition.ObjectRecognitionService import ObjectRecognitionService


class EventStreamAnalyserTest(unittest.TestCase):

    def setUp(self):
        pass

    def test_event_stream_analyser_does_not_calls_handle_on_event_handler_with_empty_event(self):
        event_data_stream = ObjectRecognitionService(config={}, video_stream={})
        event_data_stream.read_stream_for_event = MagicMock(return_value={})
        event_handler = VideoEventHandler()
        event_handler.handle = MagicMock()
        event_stream_analyser = EventStreamAnalyser(event_data_stream=event_data_stream, event_handler=event_handler)
        event_stream_analyser.analyse_stream()
        event_handler.handle.assert_not_called()


    def test_event_stream_analyser_does_not_calls_handle_on_event_handler_with_None_event(self):
        event_data_stream = ObjectRecognitionService(config={}, video_stream={})
        event_data_stream.read_stream_for_event = MagicMock(return_value=None)
        event_handler = VideoEventHandler()
        event_handler.handle = MagicMock()
        event_stream_analyser = EventStreamAnalyser(event_data_stream=event_data_stream, event_handler=event_handler)
        event_stream_analyser.analyse_stream()
        event_handler.handle.assert_not_called()


    def test_event_stream_analyser_calls_handle_on_event_handler_with_event(self):
        mock_event = { "event" : { "date" : "2007-10-01" } }
        event_data_stream = ObjectRecognitionService(config={}, video_stream={})
        event_data_stream.read_stream_for_event = MagicMock(return_value=mock_event)
        event_handler = VideoEventHandler()
        event_handler.handle = MagicMock()
        event_stream_analyser = EventStreamAnalyser(event_data_stream=event_data_stream, event_handler=event_handler)
        event_stream_analyser.analyse_stream()
        event_handler.handle.assert_called_with(mock_event)


    def test_event_stream_analyser_calls_read_stream_for_event(self):
        event_data_stream = ObjectRecognitionService(config={}, video_stream={})
        event_data_stream.read_stream_for_event = MagicMock(return_value={})
        event_handler = VideoEventHandler()
        event_handler.handle = MagicMock()
        event_stream_analyser = EventStreamAnalyser(event_data_stream=event_data_stream, event_handler=event_handler)
        event_stream_analyser.analyse_stream()
        event_data_stream.read_stream_for_event.assert_called()


if __name__ == '__main__':
    unittest.main()