import unittest
import os
from src.database_handler import DatabaseHandler

class TestDatabase(unittest.TestCase):
    def setUp(self):
        self.db_handler = DatabaseHandler()
        self.test_user = ("test123", "Test User")
    
    def test_add_user(self):
        result = self.db_handler.add_user(self.test_user[0], self.test_user[1], b"test_encoding")
        self.assertTrue(result)
    
    def test_get_users(self):
        users = self.db_handler.get_all_users()
        self.assertIsInstance(users, list)

if __name__ == '__main__':
    unittest.main()
