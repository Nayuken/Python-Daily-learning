class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    # TODO: Setup the logic used for determining if quiz is complete or not
    def stil_has_question(self):
        if len(self.question_list) > self.question_number:
            return True
        else:
            print("You've completed the quiz!")
            print(f"Total Score: ({self.score}/{self.question_number})")

    # TODO setup the logic for asking the user a question
    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text}(True/False)")
        self.check_answer(user_answer, current_question.answer)

    # TODO Setup the logic for checking if the user answer was correct or not
    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print(f"Correct!")
            self.score += 1
        else:
            print("Incorrect.")
        print(f"The correct answer was {correct_answer}")
        print(f"Current score: ({self.score}/{self.question_number})\n")
