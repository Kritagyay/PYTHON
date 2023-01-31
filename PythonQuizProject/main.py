from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank=[]
for question in question_data:
    new=Question(question["text"],question["answer"])
    question_bank.append(new)

quiz=QuizBrain(question_bank)
quiz.next_question()

# end=False
while quiz.still_has_question():
    quiz.next_question()
print(f"You have completed the Quiz !")
print(f"You'r final score is {quiz.score}/{len(question_bank)}")