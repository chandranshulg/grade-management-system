# utils.py
def display_menu():
    print("1. Add student")
    print("2. Remove student")
    print("3. Add grade")
    print("4. Get student average")
    print("5. Get all students average")
    print("6. Save data")
    print("7. Load data")
    print("8. Exit")

def get_choice():
    try:
        return int(input("Enter your choice: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return -1
