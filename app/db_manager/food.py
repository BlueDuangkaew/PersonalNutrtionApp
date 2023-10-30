"""
find_food_name.py

This module contains functions for the food database.

Funtions: 
    add_food
"""

import mysql.connector
from mysql.connector import Error
import pandas as pd

__author__ = "Peach"

# Constants
PW = "@1992!"
DB_NAME = "food_database"

# Database Management Functions

def create_server_connection(
        host_name, user_name, user_password, db_name=None
    ):
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print("MySQL Database connection successful")
        return connection
    except Error as err:
        print(f"Error: '{err.msg}'")
        return None

def check_database_exists(connection, db_name):
    cursor = connection.cursor()
    cursor.execute(f"SHOW DATABASES LIKE '{db_name}'")
    database = cursor.fetchone()
    return database is not None

def create_database(connection, db_name):
    with connection.cursor() as cursor:
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_name}")
        print("Database created successfully")

def drop_database(connection, db_name):
    with connection.cursor() as cursor:
        cursor.execute(f"DROP DATABASE {db_name}")
        print(f"Database {db_name} dropped successfully")

def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        print(f"Executing query:\n{query}\n")  
        cursor.execute(query)
        
        # If the query is a SELECT statement, fetch the results.
        if query.strip().upper().startswith("SELECT"):
            cursor.fetchall()
        else:
            connection.commit()

        print("Query successful")
    except Error as e:
        print(f"Error: '{e.msg}'")
    finally:
        cursor.close()


def fetch_all_rows(connection, query):
    with connection.cursor() as cursor:
        cursor.execute(query)
        rows = cursor.fetchall()
        for row in rows:
            print(row)

def main():
    # Connect to server and setup database
    connection = create_server_connection("localhost", "root", PW)

    if connection and check_database_exists(connection, DB_NAME):
        drop_database(connection, DB_NAME)
    if connection:
        create_database(connection, DB_NAME)

    # Connect to the created database and set up tables
    connection = create_server_connection("localhost", "root", PW, DB_NAME)

    if connection:
       
        create_table_query = """
            CREATE TABLE food (
                id INT AUTO_INCREMENT PRIMARY KEY,
                food_name VARCHAR(255) NOT NULL,
                calories VARCHAR(255) NOT NULL,
                sodium VARCHAR(3)
              
                
            );
        """

        execute_query(connection, create_table_query)

        create_food_table = """
        INSERT INTO food VALUES
        (1, 'oatmeal', 90, 1.5),
        (2, 'tempura', 350, 1.3),
        (3, 'burger', 365, 0.2),
        (4, 'pizza', 256, 0.1),
        (5, 'sushi', 483, 0.9),
        (6, 'garlic', 449, 1.3),
        (7, 'sushi', 96, 0.9),
        (8, 'banana', 489, 1.3),
        (9, 'muffin', 445, 0.2),
        (10, 'blueberry', 368, 1.2),
        (11, 'blueberry', 457, 1.5),
        (12, 'sandwich', 201, 1.1),
        (13, 'lobster', 125, 0.2),
        (14, 'garlic', 383, 1.5),
        (15, 'burger', 425, 0.8),
        (16, 'onion', 99, 1.4),
        (17, 'avocado', 295, 0.3),
        (18, 'sandwich', 216, 1.1),
        (19, 'cheese', 53, 0.5),
        (20, 'pizza', 111, 1.0),
        (21, 'honeydew', 198, 1.2),
        (22, 'bacon', 494, 1.4),
        (23, 'beef', 445, 0.5),
        (24, 'onion', 110, 0.8),
        (25, 'rice', 452, 0.2),
        (26, 'pancake', 164, 0.5),
        (27, 'bagel', 398, 0.4),
        (28, 'cucumber', 269, 0.6),
        (29, 'toast', 307, 0.4),
        (30, 'cheese', 108, 0.9),
        (31, 'toast', 289, 0.2),
        (32, 'pepper', 436, 1.3),
        (33, 'peach', 225, 0.9),
        (34, 'kale', 88, 0.5),
        (35, 'nectarine', 82, 0.4),
        (36, 'quinoa', 241, 0.3),
        (37, 'bagel', 277, 0.5),
        (38, 'cheese', 434, 0.5),
        (39, 'sushi', 285, 0.9),
        (40, 'lentils', 331, 0.9),
        (41, 'taco', 111, 1.1),
        (42, 'orange', 241, 0.8),
        (43, 'cucumber', 330, 1.2),
        (44, 'edamame', 118, 1.2),
        (45, 'bacon', 488, 0.7),
        (46, 'cherry', 108, 0.8),
        (47, 'muffin', 323, 1.4),
        (48, 'lemon', 88, 1.5),
        (49, 'zucchini', 434, 0.4),
        (50, 'cantaloupe', 328, 0.3),
        (51, 'blueberry', 375, 1.0),
        (52, 'rice', 369, 1.2),
        (53, 'doughnut', 147, 0.4),
        (54, 'olive', 464, 1.3),
        (55, 'croissant', 470, 0.6),
        (56, 'bread', 246, 1.1),
        (57, 'waffle', 127, 0.9),
        (58, 'zucchini', 441, 0.1),
        (59, 'blueberry', 424, 0.9),
        (60, 'figs', 313, 0.8),
        (61, 'raisins', 404, 0.1),
        (62, 'enchilada', 471, 0.4),
        (63, 'quesadilla', 363, 1.4),
        (64, 'grapes', 420, 1.3),
        (65, 'cheese', 58, 0.4),
        (66, 'waffle', 355, 0.2),
        (67, 'carrot', 285, 0.9),
        (68, 'tofu', 175, 1.4),
        (69, 'chocolate', 324, 0.3),
        (70, 'pork', 479, 1.2),
        (71, 'dates', 65, 0.5),
        (72, 'pineapple', 371, 0.5),
        (73, 'pineapple', 56, 0.8),
        (74, 'croissant', 163, 0.9),
        (75, 'edamame', 354, 1.3),
        (76, 'burrito', 210, 0.2),
        (77, 'burrito', 443, 0.9),
        (78, 'pear', 211, 0.3),
        (79, 'barley', 496, 0.5),
        (80, 'carrot', 437, 0.5),
        (81, 'zucchini', 433, 0.4),
        (82, 'burrito', 155, 1.4),
        (83, 'ice cream', 266, 1.1),
        (84, 'wheat', 66, 1.2),
        (85, 'watermelon', 56, 1.1),
        (86, 'pizza', 317, 1.0),
        (87, 'figs', 90, 1.4),
        (88, 'doughnut', 109, 0.7),
        (89, 'coconut', 167, 1.5);


    
        """

        execute_query(connection, create_food_table)

        # print out rows
        print("\nRows in the food table:")
        fetch_all_rows(connection, "SELECT * FROM food;")
    
    # Close connection
    if connection:
        connection.close()
        print("MySQL connection is closed")

#to find food name in the databse
def find_food_name(connection, food_name):
    if connection:
        with connection.cursor() as cursor:
            # for the SQL query to select rows with the specified food_name
            query = f"SELECT * FROM food WHERE food_name = '{food_name}'"

            cursor.execute(query)
            rows = cursor.fetchall()

            if rows:
                print(f"Found {len(rows)} matching records for food name '{food_name}':")
                for row in rows:
                    print(row)
            else:
                print(f"No records found for food name '{food_name}'")

#to add new food name and its values
def add_food(connection, food_info):
    if connection:
        with connection.cursor() as cursor:
            # get food info from the dictionary
            food_name = food_info.get('food_name')
            calories = food_info.get('calories')
            sodium = food_info.get('sodium')

            if food_name and calories is not None and sodium is not None:
                # for the SQL query to insert the food information into the 'food' table
                insert_query = f"INSERT INTO food (food_name, calories, sodium) VALUES ('{food_name}', {calories}, {sodium});"

                try:
                    cursor.execute(insert_query)
                    connection.commit()
                    print(f"Food '{food_name}' added to the database.")
                except Error as e:
                    print(f"Error adding food to the database: {e}")
            else:
                print("Invalid food information. Make sure 'food_name' is provided and 'calories' and 'sodium' are int values.")


if __name__ == "__main__":
    connection = create_server_connection("localhost", "root", PW, DB_NAME)
    if connection:
        find_food_name(connection, "pizza")
        connection.close()