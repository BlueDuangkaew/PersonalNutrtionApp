'''
nutrition_report_byGoal.py

This module contains functions for reporting nutrition from the user goal set
'''
import sqlite3

__author__ = "Blue"

def generate_report_by_goal(nutrition_type, max_value):
    '''
    <<function brief description>>

    Arguments:
        nutrition_type:
            <<brief description>> 
        max_value:
            <<brief description>> 
    
    Returns:
        <<brief description>> 
    '''
    eating_history_conn = sqlite3.connect('eating_history.db')
    eating_history_cursor = eating_history_conn.cursor()
    operator = '<=' if nutrition_type == 'calories' else '>='
    eating_history_cursor.execute(f'''
        SELECT date, SUM(food.{nutrition_type} * servings) 
        AS total_{nutrition_type}
        FROM eating_history
        INNER JOIN food ON eating_history.food_id = food.food_id
        GROUP BY date
        HAVING total_{nutrition_type} {operator} ?
    ''', (max_value,))
    
    report = eating_history_cursor.fetchall()
    eating_history_conn.close()
    return report
