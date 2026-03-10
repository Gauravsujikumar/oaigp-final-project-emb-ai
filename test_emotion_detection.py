import unittest
from emotion_detection import emotion_detector

class TestEmotionDetection(unittest.TestCase):

    def test_joy(self):
        result = emotion_detector("I am happy")
        self.assertIn("joy", str(result))

    def test_sadness(self):
        result = emotion_detector("I am sad")
        self.assertIn("sadness", str(result))

if __name__ == "__main__":
    unittest.main()
