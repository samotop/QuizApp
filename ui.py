from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quizbrain: QuizBrain):
        self.quiz = quizbrain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(pady=20, padx=20,  background=THEME_COLOR)

        self.canvas = Canvas(width=300, height=250, background="white")
        self.question_text = self.canvas.create_text(150,
                                                     125,
                                                     text="Lalalal",
                                                     font=("Arial", 20, "italic"),
                                                     width=280)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        self.score_text = self.label = Label(fg="white", bg=THEME_COLOR, text=f"Score: {self.quiz.score}", font=("Arial", 12, "bold"))
        self.label.grid(column=1, row=0)

        true_image = PhotoImage(file="images/true.png")
        self.button_true = Button(image=true_image, highlightthickness=0, command=self.check_true_answer)
        self.button_true.grid(column=1, row=2)

        false_image = PhotoImage(file="images/false.png")
        self.button_false = Button(image=false_image, highlightthickness=0, command=self.check_false_answer)
        self.button_false.grid(column=0, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
            self.canvas.config(background="white")
        else:
            self.canvas.config(background="white")
            self.canvas.itemconfig(self.question_text, text="You finished the quiz. Congratulations!")
            self.button_true.config(state="disabled")
            self.button_false.config(state="disabled")

    def check_true_answer(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)
        self.score_text.config(text=f"Score: {self.quiz.score}")

    def check_false_answer(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)
        self.score_text.config(text=f"Score: {self.quiz.score}")

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(background="green")
            self.window.after(1000, self.get_next_question)
        else:
            self.canvas.config(background="red")
            self.window.after(1000, self.get_next_question)