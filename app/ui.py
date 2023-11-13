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
            raw_str = num_str.encode('unicode_escape').decode()
            if (parser is int 
                    and str(err) == ("invalid literal for int() with base 10: " 
                                     f"'{raw_str}'")):
                print("\n**Invalid value. "
                      "The value must be a non-negative integer.**\n")
                
            elif (parser is float
                    and str(err) == ("could not convert string to float: "
                                     f"'{raw_str}'")):
                print("\n**Invalid value. "
                      "The value must be a non-negative number.**\n")
        else:
            if num >= 0:
                return num
            print("\n**Invalid value. The value cannot be negative.**\n")

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
                print(f"\n**Invalid date format. "
                      f"Please use {cls.format_prompt} format.**\n")
            else:
                now = datetime.today()
                if date > now:
                    print("\n**The date you entered is in the future. "
                          "Please enter a valid date.**\n")
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
                print("\n**The start date should be before the end date.**\n")
            else:
                break
        return start_date, end_date + timedelta(days=1)
    
    def is_recent(date, days_limit):
        return date >= datetime.today() - timedelta(days=days_limit)

    @staticmethod  
    def no_info():
        print("\n**The date has missing info.**\n")

    @staticmethod 
    def range_no_info():
        print("\n**The all dates in the range has missing info.**\n")


class MealInput():
    days_old_limit = 30    

    def __init__(
            self, 
            mealtimes: tuple[str, ...],                      
            food_name_key: str,  
            types_key: tuple[str, ...], 
            units: tuple[str, ...]) -> None:
        self.mealtimes = mealtimes
        self.food_name_key = food_name_key
        self.types_key = types_key
        self.units = units
        self.foods = []

    def enter_time(self) -> (datetime, str):
        while True:
            date = DateInput.enter_one()
            if DateInput.is_recent(date, self.days_old_limit):
                break
            print(f"\n**Date entered is too old. "
                  f"Please enter a date within "
                  f"{self.days_old_limit} days.**\n")
        while True:
            # Convert to lowercase for case-insensitivity
            meal = input(f"Enter meal type ({'/'.join(self.mealtimes)}): "
                        ).lower()  
            
            if meal in self.mealtimes:
                return date, meal
            else:
                print(f"\n**Invalid meal type. "
                      f"Please enter {_or_list(self.mealtimes)}.**\n")

    def overwrite(self) -> bool:
        choice = input("A meal at this time already exists " 
                       "would you like to overwrite it (y/n)? ").lower()
        while True:
            if choice == "y":
                return True
            elif choice == "n":
                return False
            else:
                choice = input("Invalid input. Enter y or n: ")

    def enter_food(self):
        print("\nCommands:\n"
              "\t'done' to finish and save\n"
              "\t'cancel' to cancel")
        while True:
            user_food = input(
                "Enter a food item: ").lower()
            if user_food == "done":
                if not self.foods:
                    print("\n**Warning no food entered.**\n")
                else:
                    print("\nFood items:\n\t{}".format(
                        '\n\t'.join(self.foods)))
                print("Saving...")
                break
            elif user_food == "cancel":
                print("\nProcess canceled. No meal added.\n")
                raise Exception("cancelled")
            elif not all(word.isalpha() for word in user_food.split(" ")):
                print("\n**Food name must alphabetical. Space is allowed.**\n")
            elif user_food in self.foods:
                print("\nThis food has already been inputted\n")
            else:
                self.foods.append(user_food)
                yield user_food
                print(f"{user_food} added.")

    def new_food_type(self):
        summary_info = {self.food_name_key: self.foods[-1]}
        units = [f"({unit})" for unit in self.units]
        spacings = [max(map(len, lst)) for lst in (self.types_key, units)]
        print(f"No data on {self.foods[-1]}. Please fill in the following:")
        while True:
            types_info = [
                _get_pos_num(
                    float, f"\t{k:<{spacings[0]}} {unit:^{spacings[1]}}: ")     
                for k, unit in zip(self.types_key, units)
            ]
            if any(types_info):
                break
            print("\n**Nutrition value cannot be all zero.**\n")
        summary_info.update(dict(zip(self.types_key, types_info)))
        return summary_info

def ask_nutrition_type(nutrition_types: str):
    while True:
    # Ask the user to input a nutrition type (calories, sodium, or sugar)
        nutrition_type = input(
            f"Enter a nutrition type ({'/'.join(nutrition_types)}): ").lower()

    # Check if the input is valid
        if nutrition_type not in nutrition_types:
            print(f"\n**Invalid nutrition type." 
                  f"Please enter {_or_list(nutrition_types)}.**\n")
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
            print(f"\n**Invalid choice. Please select {_or_list(indices)}.**\n")
        else:
            print("\n")
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
    spacing = max(map(len, report_info[1]))
    print(f"\n{report_info[0].strftime('%Y/%m/%d')} Summary:")
    for key, total in report_info[1].items():
        print(f"{key:<{spacing}}: {total}")
