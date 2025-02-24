class Student:
    def __init__(self,studentID,name,enrolledCourses):
        self.studentID = studentID
        self.name = name
        self.enrolledCourses = enrolledCourses

    def enroll(self,courseCode):
        self.enrolledCourses.append(courseCode)

    def getCourses(self):
        return self.enrolledCourses
    
class Course:
    def __init__(self,courseCode,courseName,maxEnrollment,currentEnrollment):
        self.courseCode = courseCode
        self.courseName = courseName
        self.maxEnrollment = maxEnrollment
        self.currentEnrollment = currentEnrollment

    def canEnroll(self):
        return self.currentEnrollment < self.maxEnrollment

class EnrollmentManager:

    def __init__(self,students,courses):
        self.students = students
        self.courses = courses

    def enrollStudent(self, studentID, courseCode):
  
        student = None
        for s in self.students:
            if s.studentID == studentID:
                student = s
                break
        
        course = None
        for c in self.courses:
            if c.courseCode == courseCode:
                course = c
                break
        

        if student is None or course is None:
            return False
        

        if not course.canEnroll():
            return False
       
        student.enroll(courseCode)
        course.currentEnrollment += 1
        return True

    def listStudentsInCourse(self,courseCode):
        new = []
        for ele in self.students:
            if courseCode in ele.enrolledCourses:
                new.append(ele)
        return new






def main():
    # Create students
    student1 = Student(1, "Alice", [])
    student2 = Student(2, "Bob", [])
    # Create a course with maximum enrollment 1 to test capacity limits
    course = Course("CS101", "Intro to CS", 1, 0)
    # Create EnrollmentManager with students and the course
    em = EnrollmentManager([student1, student2], [course])
    # Test enrolling first student (should succeed)
    enroll1 = em.enrollStudent(1, "CS101")
    print("Alice enrolled in CS101:", enroll1)
    # Test enrolling second student (should fail due to capacity)
    enroll2 = em.enrollStudent(2, "CS101")
    print("Bob enrolled in CS101 (should fail):", enroll2)

    # List students in CS101
    print("Students in CS101:")
    for s in em.listStudentsInCourse("CS101"):
        print(s.name)
    # Additional: Check student's enrolled courses
    print("Alice's courses:", student1.getCourses())
    print("Bob's courses:", student2.getCourses())
if __name__ == '__main__':
    main()