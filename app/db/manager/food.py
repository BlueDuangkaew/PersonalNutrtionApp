"""
find_food_name.py

This module contains functions for the food database.

Funtions: 
    find_food_name
    add_food
"""

import sqlite3
import pandas as pd

__author__ = "Peach, Blue"

#Read .csv file
food_data = pd.read_csv('food_nutrition.csv')

#Data Clean Up
food_data.columns = food_data.columns.str.strip()

#Create/connect to a SQLite database
conn = sqlite3.connect("personal_nutrition_app.db")
# Create a cursor object
cursor = conn.cursor()

#Load data file to SQLite
#fail;replace;append
food_data.to_sql('food_nutrition', conn, if_exists='replace')

#Close connection
conn.close()

#Execute the query
def execute_query(query):
    try:
        cursor.execute(query)
        # if the query is a SELECT statement then it will fetch the results
        if query.strip().upper().startswith("SELECT"):
            return cursor.fetchall()
        else:
            conn.commit()
            return cursor.lastrowid  
    except sqlite3.Error as e:
        print(f"Error: '{e}'")
    finally:
        cursor.close()

#Add a new food in the database
def add_new_food(food_info):
    food_name = food_info.get('food_name')
    calories = food_info.get('calories')
    sodium = food_info.get('sodium')
    protien = food_info.get('protien')
    carbohydrate = food_info.get('carbohydrate')
    fat = food_info.get('fat')

    # check if all the necessary information is provided
    if food_name and calories is not None and sodium is not None:
        # check if the food already exists in the database
        check_query = f"SELECT * FROM food_nutrition WHERE food_name = '{food_name}'"
        existing_food = execute_query(check_query)
        
        if existing_food:
            print(f"The food '{food_name}' already exists in the database.")
        else:
            # food does not exist so insert it
            insert_query = f"""
            INSERT INTO food (food_name, calories, sodium, protien, carbohydrate, fat)
            VALUES ('{food_name}', {calories}, {sodium}, {protien}, {carbohydrate}, {fat});
            """
            try:
                execute_query(insert_query)
                print(f"Food '{food_name}' added to the database.")
            except sqlite3.Error as e:
                print(f"Error adding food to the database: {e}")
    else:
        print("Invalid food information. Make sure 'food_name', and the nutrition info are provided.")

# function to find food name in the db
def find_food_name(food_name):
    query = f"SELECT * FROM food_nutrition WHERE food_name = '{food_name}'"
    rows = execute_query(query)

    if not rows:
        raise Exception("No matching data.")
    return rows


'''
if __name__ == "__main__":
    main()
    conn = create_connection(DB_FILE)
    if conn:
        # find a food named 'pizza' in the database
        find_food_name(conn, "pizza")

        # add a new food item to the database
        new_food_info = {
            'food_name': 'peach',
            'calories': 150,
            'sodium': 0.4
        }
        add_food(conn, new_food_info)

        # Close the connection
        conn.close()
'''