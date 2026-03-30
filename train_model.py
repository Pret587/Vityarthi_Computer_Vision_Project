#!/usr/bin/env python3

import pickle
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from src.database_handler import DatabaseHandler

def train_knn_model():
    print("Training KNN model...")
    
    db_handler = DatabaseHandler()
    users = db_handler.get_all_users()
    
    if not users:
        print("No users found in database. Please register users first.")
        return
    
    encodings = []
    names = []
    
    for user in users:
        encoding_bytes = user[2]
        if encoding_bytes:
            encoding = np.frombuffer(encoding_bytes, dtype=np.float64)
            encodings.append(encoding)
            names.append(user[0])  # Using user_id as label
    
    if encodings:
        knn_clf = KNeighborsClassifier(n_neighbors=1, algorithm='ball_tree')
        knn_clf.fit(encodings, names)
        
        # Save the model
        with open('models/knn_model.clf', 'wb') as f:
            pickle.dump(knn_clf, f)
        
        print(f"Model trained with {len(encodings)} encodings")
    else:
        print("No face encodings found to train model.")

if __name__ == '__main__':
    train_knn_model()
