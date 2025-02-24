import sys


def add_Student_Details(nam, roll_num, mar, name, roll_number, mark):
    nam.append(name)
    roll_num.append(roll_number)
    mar.append(mark)


def get_Grades(mar):
    if 90 <= mar:
        return "A"
    elif 80 <= mar:
        return "B"
    elif 70 <= mar:
        return "C"
    else:
        return "D"


def display_All_Students(nam, roll_num, mar):
    for i in range(len(nam)):
        grade = get_Grades(mar[i])
        print(
            f"Name: {nam[i]}, Roll Number: {roll_num[i]}, Marks: {mar[i]}, Grade: {grade}"
        )


def calculate_Total_Average(mar):
    if len(mar) > 0:
        avg_mar = sum(mar) / len(mar)

        print(f"Average Marks: {avg_mar:.2f}")


def main():
    nam = []
    roll_num = []
    mar = []

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
            add_Student_Details(nam, roll_num, mar, name, roll_number, mark)

        elif command == "DisplayStudents":
            display_All_Students(nam, roll_num, mar)

        elif command == "CalculateAverageMarks":
            calculate_Total_Average(mar)


main()
