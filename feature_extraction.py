import cv2
import numpy as np

class FeatureExtractor:
    def __init__(self):
        pass
    
    def extract_basic_features(self, image):
        """Extract basic image features"""
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        
        # Histogram features
        hist = cv2.calcHist([gray], [0], None, [256], [0, 256])
        hist_features = hist.flatten()
        
        # Basic statistics
        mean = np.mean(gray)
        std = np.std(gray)
        
        return np.concatenate([hist_features, [mean, std]])
