class QuizBrain:
    def __init__(self,question_bank):
        self.question_number=0
        self.question_list=question_bank
        self.score=0
    def still_has_question(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question=self.question_list[self.question_number]
        self.question_number+=1
        user_input= input(f"Q.{self.question_number}: {current_question.text} (True/False):")
        self.check_answer(user_input,current_question.answer)

    def check_answer(self,user_input,current_answer):
        if user_input.lower()==current_answer.lower():
            self.score+= 1
            print(f"You got it right! ")
            print(f"Your current score is {self.score}/{self.question_number}")

        else:
            print(f"You were wrong !")
            print(f"The right answer is {current_answer}")
            print(f"Your current score is {self.score}/{self.question_number}")
