class Question:
    def __init__(self, question_text, choices, correctOption, max_marks, penalty):
        self.question_text = question_text
        self.choices = choices
        self.correctOption = correctOption
        self.max_marks = max_marks
        self.penalty = penalty
        self.userChoice = None
        self.score = 0

    def evaluate_answer(self, userChoice):
        self.userChoice = userChoice
        if self.userChoice == self.correctOption:
            self.score = self.max_marks
        else:
            self.score = self.penalty
        return self.score

    # def __str__(self):
    #     return f"{self.question_text} | {self.choices} | {self.correctOption} | {self.max_marks} | {self.penalty}"


class Quiz:
    def __init__(self):
        self.questions = []
        self.total_score = 0

    def parseQuestions(self, data):
        for ele in data.splitlines():
            q, o, c, m, p = ele.split(":")
            choices = o.split(",")
            question = Question(q, choices, int(c), int(m), int(p))
            self.questions.append(question)

    def startQuiz(self, test_answers):
        for i in range(len(self.questions)):
            self.total_score += self.questions[i].evaluate_answer(test_answers[i])

    def scoreReport(self):
        print()
        print("Score Report:")
        for ele in self.questions:
            print(f"Question: {ele.question_text}")
            print(f"Choices: {', '.join(ele.choices)}")
            print(f"Your Answer: {ele.userChoice} | Correct Answer: {ele.correctOption}")
            if ele.userChoice == ele.correctOption:
                print(f"Correct Answer! Marks Awarded: {ele.max_marks}")
            else:
                print(f"Wrong Answer! Penalty Applied: {ele.penalty}")
            print()
        print(f"Total Score: {self.total_score}")
