# grade_manager.py
import json
from student import Student  # Change to absolute import

class GradeManager:
    def __init__(self):
        self.students = {}

    def add_student(self, student_id, name):
        if student_id in self.students:
            print("Student already exists.")
            return
        self.students[student_id] = Student(student_id, name)

    def remove_student(self, student_id):
        if student_id in self.students:
            del self.students[student_id]
        else:
            print("Student not found.")

    def add_grade(self, student_id, grade):
        if student_id in self.students:
            self.students[student_id].add_grade(grade)
        else:
            print("Student not found.")

    def get_student_average(self, student_id):
        if student_id in self.students:
            return self.students[student_id].calculate_average()
        else:
            print("Student not found.")
            return None

    def get_all_students_average(self):
        if not self.students:
            return 0
        total_sum = 0
        total_count = 0
        for student in self.students.values():
            total_sum += sum(student.grades)
            total_count += len(student.grades)
        return total_sum / total_count if total_count else 0

    def save_data(self, filename):
        with open(filename, 'w') as f:
            json.dump(self.students, f, default=lambda o: o.__dict__, indent=4)

    def load_data(self, filename):
        with open(filename, 'r') as f:
            data = json.load(f)
            self.students = {int(k): Student(**v) for k, v in data.items()}
