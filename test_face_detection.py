import unittest
import cv2
import numpy as np
from src.face_detection import FaceDetector

class TestFaceDetection(unittest.TestCase):
    def setUp(self):
        self.detector = FaceDetector()
        # Create a dummy image with a face-like region
        self.test_image = np.random.randint(0, 255, (100, 100, 3), dtype=np.uint8)
    
    def test_face_detection(self):
        faces = self.detector.detect_faces(self.test_image)
        self.assertIsInstance(faces, tuple)
    
    def test_face_encoding(self):
        encodings = self.detector.extract_face_encodings(self.test_image)
        self.assertIsInstance(encodings, list)

if __name__ == '__main__':
    unittest.main()
