import pickle
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
import face_recognition

class FaceRecognizer:
    def __init__(self):
        self.knn_clf = None
    
    def load_model(self, model_path):
        """Load trained KNN model"""
        try:
            with open(model_path, 'rb') as f:
                self.knn_clf = pickle.load(f)
            return True
        except Exception as e:
            print(f"Error loading model: {e}")
            return False
    
    def recognize_face(self, face_encoding):
        """Recognize face using simple distance comparison"""
        if self.knn_clf is None:
            return "Unknown", 0.0
        
        try:
            distances, indices = self.knn_clf.kneighbors([face_encoding], n_neighbors=1)
            confidence = 1.0 / (1.0 + distances[0][0])
            
            if confidence > 0.6:
                return self.knn_clf.classes_[indices[0][0]], confidence
            return "Unknown", confidence
        except:
            return "Unknown", 0.0
    
    def simple_recognize(self, encoding, known_encodings, known_names):
        """Simple recognition using distance comparison"""
        if len(known_encodings) == 0:
            return "Unknown", 0.0
        
        distances = face_recognition.face_distance(known_encodings, encoding)
        min_distance = min(distances)
        
        if min_distance < 0.6:
            index = np.argmin(distances)
            return known_names[index], 1.0 - min_distance
        return "Unknown", 1.0 - min_distance
