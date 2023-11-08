from datetime import datetime, timedelta
from typing import Callable

'''
ui.py

This module contains functions for the user interface.
'''

__author__ = "Palm, Pokpong"

def _get_pos_num(parser: Callable, prompt: str):
    while True:
        num_str = input(prompt)
        try:
            num = parser(num_str)
        except ValueError as err:
            if (parser is int 
                    and str(err) == ("invalid literal for int() with base 10: " 
                                     f"'{num_str}'")):
                print("Invalid value. "
                      "The value must be a non-negative integer.")
            elif (parser is float
                    and str(err) == ("could not convert string to float: "
                                     f"'{num_str}'")):
                print("Invalid value. "
                      "The value must be a non-negative number.")
            print(parser is int, str(err))
        else:
            if num >= 0:
                return num
            print("Invalid value. The value cannot be negative.")

def _or_list(items: list[str]):
    str_list = items[0]
    for item in items[1:-1]:
        str_list += f", {item}"
    if items[0] != items[-1]:
        str_list += f", or {items[-1]}"
    return str_list

class DateInput():
    format = "%Y/%m/%d"
    format_prompt = "YYYY/MM/DD"

    @classmethod
    def _parse_input(cls, prompt: str):
        while True:
            date_str = input(prompt)
            try:
                date = datetime.strptime(date_str, cls.format)
            except ValueError:
                print(f"Invalid date format. "
                      f"Please use {cls.format_prompt} format.")
            else:
                now = datetime.today()
                if date > now:
                    print("The date you entered is in the future. "
                            "Please enter a valid date.")
                else:
                    return date
    @classmethod            
    def enter_one(cls):
        return cls._parse_input(f"Enter the date ({cls.format_prompt}): ")

    @classmethod  
    def enter_range(cls):
        while True:
            start_date = cls._parse_input(
                f"Enter the start date {cls.format_prompt}: ")
            end_date = cls._parse_input(
                f"Enter the end date {cls.format_prompt}: ")

            if start_date > end_date:
                print("The start date should be before the end date.")
            else:
                break
        return start_date, end_date + timedelta(days=1)
    
    def is_recent(date, days_limit):
        return date >= datetime.today() - timedelta(days=days_limit)

    @staticmethod  
    def no_info():
        print("The date has missing info.")

    @staticmethod 
    def range_no_info():
        print("The all dates in the range has missing info.")


class MealtimeInput():
    days_old_limit = 30

    def __init__(self, mealtimes: tuple[str, ...]) -> None:
        self.mealtimes = mealtimes

    def enter(self) -> (datetime, str):
        while True:
            date = DateInput.enter_one()
            if DateInput.is_recent(date, self.days_old_limit):
                break
            print(f"Date entered is too old. "
                  f"Please enter a date with {self.days_old_limit}")
        while True:
            # Convert to lowercase for case-insensitivity
            meal = input(f"Enter meal type ({'/'.join(self.mealtimes)}): "
                        ).lower()  
            
            if meal in self.mealtimes:
                return date, meal
            else:
                print(f"Invalid meal type. "
                      f"Please enter {_or_list(self.mealtimes)}.")

    def overwrite(self) -> bool:
        choice = input("A meal at this time already exists " 
                       "would you like to overwrite it (y/n)? ").lower()
        while True:
            match choice:
                case 'y':
                    return True
                case 'n':
                    return False
                case _:
                    choice = input("Invalid input. Enter y or n: ")

class FoodInput():
    def __init__(self, info_types: tuple[str, ...]) -> None:
        self.info_types = info_types
        self.foods = []
        
    def getter(self):
        while True:
            user_food = input(
                "Enter a food item (or 'done' to finish): ").lower()
            if user_food == 'done':
                if not self.foods:
                    print("No food entered. Returning to main menu.")
                else:
                    print("Foods:\n\t{}".format('\n\t'.join(self.foods)))
                break
            elif not all(word.isalpha() for word in user_food.split(" ")):
                print("Food name must alphabetical. Space is allowed")
            elif user_food in self.foods:
                print("This food has already been inputted")
            else:
                self.foods.append(user_food)
                yield user_food
                print(f"{user_food} added.")

    def new_type(self):
        print(f"No data on {self.foods[-1]}. Please fill in the following:")
        food_info = {self.info_types[0]: self.foods[-1]}
        while True:
            for nutrition in self.info_types[1:]:
                food_info.update({
                    nutrition: _get_pos_num(float, f"\t{nutrition}: ")
                    })
            if any(list(food_info.values())[1:]):
                break
            print("Nutrition value cannot be all zero.")
        return food_info

def ask_nutrition_type(nutrition_types: str):
    while True:
    # Ask the user to input a nutrition type (calories, sodium, or sugar)
        nutrition_type = input(
            f"Enter a nutrition type ({'/'.join(nutrition_types)}): ").lower()

    # Check if the input is valid
        if nutrition_type not in nutrition_types:
            print(f"Invalid nutrition type." 
                  f"Please enter {_or_list(nutrition_types)}")
            continue

    # Ask the user to input the limit for the chosen nutrition type
        max_value = _get_pos_num(
            float, f"Enter the limit for {nutrition_type}: ")
        break
    return nutrition_type, max_value

# Define the main function
def main_menu():
    options = (
        "Enter a meal", "Daily report", 
        "Goal report",  "Exit"
        )
    indices = []
    print("\nFood and Nutrition Tracker")
    for i, opt in enumerate(options):
        print(f"{i + 1}. {opt}")
        indices.append(str(i + 1))
    while True:
        # Prompt the user to select an option
        choice = _get_pos_num(int, f"Select an option ({'/'.join(indices)}): ")
        if str(choice) not in indices:
            print(f"Invalid choice. Please select {_or_list(indices)}")
        else:
            return choice - 1
        
def print_target_report(report_info: dict[str, dict]):
    columns_names = ("Date", "Value relative to max value")

    dates, diffs = map(list, zip(*report_info["diff"].items()))
    date_strs = [date.strftime('%Y/%m/%d') for date in dates]

    def format_diff(diff):
        if diff < 0:
            return f"{-1*diff}% under"
        elif diff > 0:
            return f"{diff}% over"
        else:
            return "same"
        
    diff_strs = [format_diff(diff) for diff in diffs]
    diff_strs.insert(0, columns_names[0])
    spacing = max(list(map(len, date_strs)))
    del diff_strs[0]
    print()
    for k, v in report_info["header"].items():
        print(f"{k}: {v}")
    print()
    header = f"{columns_names[0]:<{spacing}} | {columns_names[1]}"
    print(header)
    print("-"*len(header))
    for date_str, diff_str in zip(date_strs, diff_strs):
        print(f"{date_str:<{spacing}} | {diff_str}")

def print_daily_report(report_info: tuple[datetime, dict]):
    print(f"\n{report_info[0].strftime('%Y/%m/%d')} Summary:")
    for key, total in report_info[1].items():
        print(f"{key}: {total}")
