import csv
from datetime import datetime
from src.database_handler import DatabaseHandler

class ReportGenerator:
    def __init__(self):
        self.db_handler = DatabaseHandler()
    
    def generate_daily_report(self):
        """Generate daily attendance report"""
        records = self.db_handler.get_attendance_records()
        
        report_data = {
            'total_records': len(records),
            'unique_users': len(set(record[0] for record in records)),
            'records': records
        }
        
        return report_data
    
    def export_to_csv(self, filename=None):
        """Export attendance data to CSV"""
        if filename is None:
            filename = f"attendance_report_{datetime.now().strftime('%Y%m%d')}.csv"
        
        records = self.db_handler.get_attendance_records()
        
        with open(filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['User ID', 'Name', 'Timestamp', 'Confidence'])
            
            for record in records:
                writer.writerow(record)
        
        return filename
