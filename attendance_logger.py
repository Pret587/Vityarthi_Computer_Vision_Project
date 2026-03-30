from src.database_handler import DatabaseHandler

class AttendanceLogger:
    def __init__(self):
        self.db_handler = DatabaseHandler()
    
    def log_attendance(self, user_id, confidence=1.0):
        """Log attendance for a user"""
        self.db_handler.record_attendance(user_id, confidence)
        print(f"Attendance logged for user: {user_id}")
    
    def get_today_attendance(self):
        """Get today's attendance records"""
        records = self.db_handler.get_attendance_records()
        return records
