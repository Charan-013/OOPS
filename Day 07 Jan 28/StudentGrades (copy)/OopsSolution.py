import sys


class Student:
    def __init__(self, name, roll_number, mark):
        self.name = name
        self.roll_number = roll_number
        self.mark = mark

    def get_Grade(self):
        if 90 <= self.mark:
            return "A"
        elif 80 <= self.mark:
            return "B"
        elif 70 <= self.mark:
            return "C"
        else:
            return "D"


class GradeBook:
    def __init__(self):
        self.nam = []
        self.roll_num = []
        self.mar = []

    def add_Student_Details(self, name, roll_number, mark):
        student = Student(name, roll_number, mark)
        self.nam.append(student.name)
        self.roll_num.append(student.roll_number)
        self.mar.append(student.mark)

    def display_All_Students(self):
        for i in range(len(self.nam)):
            student = Student(self.nam[i], self.roll_num[i], self.mar[i])
            grade = student.get_Grade()
            print(
                f"Name: {self.nam[i]}, Roll Number: {self.roll_num[i]}, Marks: {self.mar[i]}, Grade: {grade}"
            )

    def calculate_Total_Average(self):
        if len(self.mar) > 0:
            avg_mark = sum(self.mar) / len(self.mar)
            print(f"Average Marks: {avg_mark:.2f}")


def main():
    gradebook = GradeBook()

    input_data = sys.stdin.read().strip()
    commands = input_data.splitlines()

    for command in commands:
        command = command.strip()

        if command.startswith("Add Student:"):
            ignore, student_info = command.split("Add Student: ")
            name, roll_number, mark = student_info.split(", ")
            name = name.strip()
            roll_number = int(roll_number)
            mark = int(mark)
            gradebook.add_Student_Details(name, roll_number, mark)

        elif command == "DisplayStudents":
            gradebook.display_All_Students()

        elif command == "CalculateAverageMarks":
            gradebook.calculate_Total_Average()


main()
