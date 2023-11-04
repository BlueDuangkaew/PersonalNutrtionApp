### Module : eating_history.py

Committer: **Pokpong**
Reviewers: **Blue, Plam**
Scribe: **Peach**

### Code summary:

The new version modified by Pokpong extends the functionality with a function to return specific entries of data from the database and also adding a wrapper to align the return types to the agreed-on format.

The original version of the module written by Palm had a function to store one entry of data and retrieve all the entries `add_meal_to_database()` and `retrieve_all_meals()`, respectively. However, it didn’t contain a function to retrieve a specific entry based on the meal type (breakfast, lunch, etc.) and the date, which was a function deemed necessary in the early planning phase.

### Feedback:

-   The code is well-organized, making it easy to understand and follow along.
-   Each function has docstrings that describe their purpose and usage.
```python 3
def format_row(row: tuple) -> dict:
	# This function formats the a row of data from the database
	meal = dict(zip(COLUMNS, row))
	meal["foods"] = meal["foods"].split(", ")
	return meal
```
-   The code handles date formatting and the transformation of the database into dictionaries for easier data manipulation.
```python 3
if meal is None:
	raise Exception("No matching data.")
return format_row(meal)
```
-   Maybe extensive error handling and unit tests could be added.
-   The code follows the coding standards such as heading comments, comments, name variables.
```python 3
'''
history_manager.py

<<Add description here>>

Functions:
add_meal_to_database
retrieve_all_meals
find_meal_date
'''
```