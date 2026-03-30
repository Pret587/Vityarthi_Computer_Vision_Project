from flask import Flask, render_template, request, jsonify, redirect, url_for
import os
from src.database_handler import DatabaseHandler
from src.face_detection import FaceDetector
from src.face_recognition import FaceRecognizer
import cv2
import numpy as np

app = Flask(__name__)
app.config.from_object('config.Config')

# Initialize components
db_handler = DatabaseHandler()
face_detector = FaceDetector()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        user_id = request.form['user_id']
        image = request.files['image']
        
        if image:
            # Save image
            image_path = os.path.join(app.config['UPLOAD_FOLDER'], f"{user_id}.jpg")
            image.save(image_path)
            
            # Process face
            img = cv2.imread(image_path)
            encodings = face_detector.extract_face_encodings(img)
            
            if encodings:
                # Save to database
                db_handler.add_user(user_id, name, encodings[0].tobytes())
                return "User registered successfully!"
    
    return render_template('register.html')

@app.route('/attendance')
def attendance():
    return render_template('attendance.html')

@app.route('/video_feed')
def video_feed():
    # This would handle real-time video processing
    return "Video feed endpoint"

@app.route('/reports')
def reports():
    records = db_handler.get_attendance_records()
    return render_template('reports.html', records=records)

if __name__ == '__main__':
    app.run(debug=True)
