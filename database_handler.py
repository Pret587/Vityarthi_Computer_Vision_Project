import sqlite3
import os
from config import Config

class DatabaseHandler:
    def __init__(self):
        self.db_path = Config.DATABASE_PATH
        self.init_database()
    
    def init_database(self):
        """Initialize database with required tables"""
        os.makedirs('database', exist_ok=True)
        
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        # Create users table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id TEXT UNIQUE NOT NULL,
                name TEXT NOT NULL,
                face_encoding BLOB,
                created_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        # Create attendance table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS attendance (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id TEXT NOT NULL,
                timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                confidence REAL,
                FOREIGN KEY (user_id) REFERENCES users(user_id)
            )
        ''')
        
        conn.commit()
        conn.close()
    
    def add_user(self, user_id, name, face_encoding):
        """Add a new user to the database"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        try:
            cursor.execute(
                'INSERT INTO users (user_id, name, face_encoding) VALUES (?, ?, ?)',
                (user_id, name, face_encoding)
            )
            conn.commit()
            return True
        except sqlite3.IntegrityError:
            return False
        finally:
            conn.close()
    
    def get_all_users(self):
        """Get all users from database"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('SELECT user_id, name, face_encoding FROM users')
        users = cursor.fetchall()
        conn.close()
        
        return users
    
    def record_attendance(self, user_id, confidence):
        """Record attendance for a user"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute(
            'INSERT INTO attendance (user_id, confidence) VALUES (?, ?)',
            (user_id, confidence)
        )
        conn.commit()
        conn.close()
    
    def get_attendance_records(self):
        """Get all attendance records"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('''
            SELECT a.user_id, u.name, a.timestamp, a.confidence 
            FROM attendance a 
            JOIN users u ON a.user_id = u.user_id 
            ORDER BY a.timestamp DESC
        ''')
        records = cursor.fetchall()
        conn.close()
        
        return records
