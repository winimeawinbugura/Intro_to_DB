#!/usr/bin/env python3
"""
This script creates the alx_book_store database in a MySQL server.
"""

import mysql.connector
from mysql.connector import Error


def create_database():
    """Create the alx_book_store database if it does not exist."""
    connection = None
    cursor = None

    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="your_password_here"
        )

        cursor = connection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")

        print("Database 'alx_book_store' created successfully!")

    except Error as e:
        print(f"Error while connecting to MySQL: {e}")

    finally:
        if cursor is not None:
            cursor.close()
        if connection is not None:
            connection.close()


if __name__ == "__main__":
    create_database()
