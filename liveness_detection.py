import cv2
import numpy as np

class LivenessDetector:
    def __init__(self):
        self.eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
    
    def detect_eyes(self, face_roi):
        """Simple eye detection for basic liveness check"""
        gray = cv2.cvtColor(face_roi, cv2.COLOR_BGR2GRAY)
        eyes = self.eye_cascade.detectMultiScale(gray, 1.1, 4)
        return len(eyes) >= 1  # At least one eye detected
    
    def basic_movement_check(self, prev_frame, current_frame):
        """Basic movement detection between frames"""
        if prev_frame is None or current_frame is None:
            return True
        
        diff = cv2.absdiff(prev_frame, current_frame)
        non_zero_count = np.count_nonzero(diff)
        return non_zero_count > 1000  # Basic threshold
