import app.history_db_manager as db
from datetime import datetime

db.create_history_database()
date = datetime.now()
db.add_meal_to_database(date, "dinner", ["apple", "banana"])
print(db.find_meal_date(date, "dinner"))
print(db.find_meal_date(date, "brunch"))