import unittest
from emotion_detection import emotion_detector

class TestEmotionDetection(unittest.TestCase):
    """
    Unit tests for the emotion_detector function.
    Tests that the function correctly identifies dominant emotions for various statements.
    """
    
    def test_joy(self):
        """Test that 'I am glad this happened' is detected as joy"""
        result = emotion_detector("I am glad this happened")
        self.assertEqual(result['dominant_emotion'], 'joy')
    
    def test_anger(self):
        """Test that 'I am really mad about this' is detected as anger"""
        result = emotion_detector("I am really mad about this")
        self.assertEqual(result['dominant_emotion'], 'anger')
    
    def test_disgust(self):
        """Test that 'I feel disgusted just hearing about this' is detected as disgust"""
        result = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(result['dominant_emotion'], 'disgust')
    
    def test_sadness(self):
        """Test that 'I am so sad about this' is detected as sadness"""
        result = emotion_detector("I am so sad about this")
        self.assertEqual(result['dominant_emotion'], 'sadness')
    
    def test_fear(self):
        """Test that 'I am really afraid that this will happen' is detected as fear"""
        result = emotion_detector("I am really afraid that this will happen")
        self.assertEqual(result['dominant_emotion'], 'fear')


if __name__ == '__main__':
    unittest.main()
