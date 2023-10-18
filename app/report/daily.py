'''
nutrition_report_byDate.py

This module contains functions for reporting nutrition from a date range
'''
import sqlite3

__author__ = "Blue"

def generate_report_by_date(start_date, end_date):
    eating_history_conn = sqlite3.connect('eating_history.db')
    eating_history_cursor = eating_history_conn.cursor()
    
    eating_history_cursor.execute('''
        SELECT date, food.name, servings
        FROM eating_history
        INNER JOIN food ON eating_history.food_id = food.food_id
        WHERE date BETWEEN ? AND ?
    ''', (start_date, end_date))
    
    report = eating_history_cursor.fetchall()
    
    eating_history_conn.close()
    
    return report