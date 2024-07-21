# main.py
from grade_manager import GradeManager
from utils import display_menu, get_choice

def main():
    manager = GradeManager()
    
    while True:
        display_menu()
        choice = get_choice()
        
        if choice == 1:
            student_id = int(input("Enter student ID: "))
            name = input("Enter student name: ")
            manager.add_student(student_id, name)
        elif choice == 2:
            student_id = int(input("Enter student ID to remove: "))
            manager.remove_student(student_id)
        elif choice == 3:
            student_id = int(input("Enter student ID: "))
            grade = float(input("Enter grade: "))
            manager.add_grade(student_id, grade)
        elif choice == 4:
            student_id = int(input("Enter student ID: "))
            avg = manager.get_student_average(student_id)
            if avg is not None:
                print(f"Average grade for student {student_id}: {avg:.2f}")
        elif choice == 5:
            avg = manager.get_all_students_average()
            print(f"Average grade for all students: {avg:.2f}")
        elif choice == 6:
            filename = input("Enter filename to save data: ")
            manager.save_data(filename)
        elif choice == 7:
            filename = input("Enter filename to load data: ")
            manager.load_data(filename)
        elif choice == 8:
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
