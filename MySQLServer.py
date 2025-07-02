#!/usr/bin/env python3
"""
MySQL Database Creation Script
Creates the alx_book_store database if it doesn't exist
"""

import mysql.connector
from mysql.connector import Error

def create_database():
    """
    Creates the alx_book_store database in MySQL server
    """
    connection = None
    cursor = None
    
    try:
        # Establish connection to MySQL server
        connection = mysql.connector.connect(
            host='localhost',        # Change this to your MySQL host
            user='root',            # Change this to your MySQL username
            password='password'     # Change this to your MySQL password
        )
        
        if connection.is_connected():
            cursor = connection.cursor()
            
            # Create database if it doesn't exist
            create_db_query = "CREATE DATABASE IF NOT EXISTS alx_book_store"
            cursor.execute(create_db_query)
            
            # Commit the transaction
            connection.commit()
            
            print("Database 'alx_book_store' created successfully!")
            
    except Error as e:
        print(f"Error: Failed to connect to MySQL server or create database - {e}")
        
    finally:
        # Close cursor and connection
        if cursor:
            cursor.close()
        if connection and connection.is_connected():
            connection.close()
            print("MySQL connection closed.")

if __name__ == "__main__":
    create_database()