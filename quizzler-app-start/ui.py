from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self,quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window=Tk()
        self.window.title("Quizzle App")
        self.window.config(padx=20,pady=20,bg=THEME_COLOR)

        self.score_label=Label(text="Score: 0",fg="white",bg=THEME_COLOR)
        self.score_label.grid(column=1,row=0)

        self.canvas=Canvas(width=300,height=250,bg="white")
        self.quote_text=self.canvas.create_text(
             150,125,
             width=280,
             text="Hello! Enjoy the Game",
             fill=THEME_COLOR,
             font=("Arial",20,"italic")
             )
        self.canvas.grid(column=0,row=1,columnspan=2,pady=50)

        self.false_button_image=PhotoImage(file="images/false.png")
        self.false_button=Button(image=self.false_button_image,highlightthickness=0,command=self.false)
        self.false_button.grid(column=1,row=2)

        self.right_button_image=PhotoImage(file="images/true.png")
        self.right_button=Button(image=self.right_button_image,highlightthickness=0,command=self.true)
        self.right_button.grid(column=0,row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score:{self.quiz.score}")
            q_text=self.quiz.next_question()
            self.canvas.itemconfig(self.quote_text,text=q_text)
        else:
            self.canvas.itemconfig(self.quote_text,text="You have completed the quiz. Thank You!")
            self.false_button.config(state="disabled")
            self.true_button.config(state="disabled")

    def true(self):
        self.feedback(self.quiz.check_answer("True"))

    def false(self):
        is_right=self.quiz.check_answer("False")
        self.feedback(is_right)

    def feedback(self,is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000,self.get_next_question)







