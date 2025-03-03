import random
# change python3 to python if use windows in eval.sh of line 15 
# =========================
# Part 1: Quiz and Question Classes
# =========================

class Question:
    # Todo
    def __init__(self,question_text,options,correct_answer):
        self.question_text = question_text
        self.options = options
        self._correct_answer = correct_answer
    
    def get_question_text(self):
        return self.question_text
    
    def get_options(self):
        return self.options
    
    def get_correct_answer(self):
        return self._correct_answer
    
    def set_question_text(self,question_text):
        self.question_text = question_text

    def set_options(self,options):
        self.options = options

    def set_correct_answer(self,correct_answer):
        self._correct_answer = correct_answer
    
    def validate_answer(self,answer):
        return self._correct_answer.lower() == answer.lower()


class MultipleChoiceQuestion(Question):
    
    def __init__(self, question_text, options, correct_answer):
        super().__init__(question_text, options, correct_answer)

    def validate_answer(self,answer):
        return self._correct_answer.lower() == answer.lower()



class TrueFalseQuestion(Question):
    
    def __init__(self, question_text,correct_answer,options = ["True", "False"]):
        super().__init__(question_text,options,correct_answer)

    def validate_answer(self, answer):
        return self._correct_answer.lower() == answer.lower()



class FillInTheBlankQuestion(Question):
    def __init__(self, question_text, correct_answer,options = ""):
        super().__init__(question_text, options, correct_answer)

    def validate_answer(self, answer):
        return self._correct_answer.lower() == answer.lower()



class Quiz:
    # Todo write the remaining methods
    def __init__(self):
        self._questions = []

    def shuffle_questions(self) -> None:
        random.shuffle(self._questions)
    
    def add_question(self,question):
        self._questions.append(question)

    def remove_question(self,question):
        self._questions.remove(question)

    def get_questions(self):
        return self._questions
    
    def get_total_questions(self):
        return len(self._questions)


# =========================
# Part 2: Person, Student, and Leaderboard Classes
# =========================

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def get_name(self):
        return self.name
    
    def get_age(self):
        return self.age


class Student(Person):
    def __init__(self, name, age,studentId):
        self.name = name
        self.age = age
        self.studentId = studentId
        self.score = 0

    def simulate_quiz(self,quiz,simulated_answers):
        print()
        print(f"--- {self.get_name()} is taking the quiz ---")
        q = quiz.get_questions()
        num_of_questions = quiz.get_total_questions()
        for i in range(num_of_questions):
            if q[i].validate_answer(simulated_answers[i]):
                print("Correct!")
                self.score += 1
            else:
                print(f"Incorrect! Correct answer: {q[i]._correct_answer}")
        print()
        print(f"{self.get_name()} scored {self.get_score()} out of {num_of_questions}.")

    def get_score(self):
        return self.score


class Leaderboard:
    def __init__(self):
       self.students = []

    def add_student(self,student):
        self.students.append(student)

    def display_leaderboard(self):
        print()
        print("=== Leaderboard ===")
        for ele in self.students:
            print(f"Student: {ele.name} | Score: {ele.get_score()}")
