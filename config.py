import os

class Config:
    SECRET_KEY = 'your-secret-key-here'
    DATABASE_PATH = 'database/attendance.db'
    UPLOAD_FOLDER = 'static/uploads'
    MODEL_PATH = 'models'
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
    
    # Face recognition settings
    FACE_DETECTION_CONFIDENCE = 0.6
    KNN_MODEL_PATH = os.path.join(MODEL_PATH, 'knn_model.clf')
    ENCODINGS_PATH = os.path.join(MODEL_PATH, 'face_encodings.pkl')
