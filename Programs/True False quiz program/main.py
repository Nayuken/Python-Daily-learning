import random
from quiz_brain import QuizBrain
from question_model import Question
from data import question_data

# We created a new list
question_bank = []
# Made a 'for loop' for the dict provided by data
for key in question_data:
    # for the values held in the key labeled "text" the variable q_txt is storing them
    q_txt = key['question']
    # for the values held in the key labeled "answer" the variable q_answer is storing them
    q_answer = key['correct_answer']
    # we created a object called 'new_question" for our class Question and pass q_txt and q_answer as parameters
    new_question = Question(q_txt, q_answer)
    # we then append the original blank list with the values held in the object new_question
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.stil_has_question():
    quiz.next_question()
