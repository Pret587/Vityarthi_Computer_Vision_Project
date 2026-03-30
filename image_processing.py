
import cv2
import numpy as np

def preprocess_image(image):
    """Basic image preprocessing"""
    # Convert to RGB if needed
    if len(image.shape) == 3 and image.shape[2] == 3:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    
    # Resize image to standard size
    image = cv2.resize(image, (640, 480))
    
    return image

def normalize_image(image):
    """Normalize image pixel values"""
    return image / 255.0

def enhance_image(image):
    """Basic image enhancement"""
    # Convert to YUV color space
    yuv = cv2.cvtColor(image, cv2.COLOR_BGR2YUV)
    yuv[:,:,0] = cv2.equalizeHist(yuv[:,:,0])
    enhanced = cv2.cvtColor(yuv, cv2.COLOR_YUV2BGR)
    return enhanced
