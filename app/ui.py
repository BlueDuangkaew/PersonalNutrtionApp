'''
ui.py

This module contains functions for the user interface.
'''

__author__ = "Palm"


# Define the main function
def main():
    # Create an infinite loop for the main menu
    while True:
        print("\nFood and Nutrition Tracker")
        print("1. Enter a meal")
        print("2. Generate a nutrition report")
        print("3. Exit")

        # Prompt the user to select an option
        choice = input("Select an option (1/2/3): ")

        # Check the user's choice and take appropriate actions
        if choice == '1':
            add_meal_to_database()  # Call the function to enter a meal
        elif choice == '2':
            report_menu()  # Call the function to display the report menu
        elif choice == '3':
            print("Exit. Have a great day!")
            break  # Exit the program
        else:
            print("Invalid choice. Please select 1, 2, or 3.")

# Define the report menu function
def report_menu():
    # Create an infinite loop for the report menu
    while True:
        print("\nReport Menu")
        print("1. Daily report")
        print("2. Goal report")
        print("3. Back to main menu")

        # Prompt the user to select an option
        choice = input("Select an option (1/2/3): ")

        # Check the user's choice and take appropriate actions
        if choice == '1':
            print("Generating reports from a date range.")
            generate_report_by_date()  # Call the function to generate a daily report
        elif choice == '2':
            print("Generating reports from the user's goal.")
            generate_report_by_goal()  # Call the function to generate a goal report
        elif choice == '3':
            break  # Return to the main menu
        else:
            print("Invalid choice. Please select 1, 2, or 3.")

if __name__ == '__main__':
    main()
