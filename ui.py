from tkinter import *
from quiz_brain import QuizBrain
# from unittest.mock import right

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(pady=20, padx=20, bg=THEME_COLOR)

        self.score = 0
        self.score_label = Label(text=f"Score: {self.score}",pady=20, padx=20,bg=THEME_COLOR, fg="white")
        self.score_label.grid(row=0, column=1)
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="just a question",
            fill=THEME_COLOR,
            font=("Arial", 20, "italic")


        )
        self.canvas.grid(row=1, column=0, columnspan=2,pady=50)

        right_img = PhotoImage(file="./images/true.png")
        false_img = PhotoImage(file="images/false.png")
        self.right_button = Button(padx=30, pady=30, image=right_img, highlightthickness=0, command=self.check_true_answer)
        self.right_button.grid(row=2, column=0)
        self.false_button = Button(image=false_img,  highlightthickness=0, command=self.check_false_answer)
        self.false_button.grid(row=2 , column=1)
        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text,)
        else:
            self.canvas.itemconfig(self.question_text, text="You\'ve reached the end of the quiz")
            self.right_button.config(state="disabled")
            self.false_button.config(state="disabled")


    def check_true_answer(self):
        self.give_feedback(self.quiz.check_answer(user_answer="True"))

    def check_false_answer(self):
        self.give_feedback(self.quiz.check_answer(user_answer="False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)






