#!/usr/bin/env python3

from src.database_handler import DatabaseHandler

def main():
    print("Setting up database...")
    db_handler = DatabaseHandler()
    print("Database setup completed!")

if __name__ == '__main__':
    main()
