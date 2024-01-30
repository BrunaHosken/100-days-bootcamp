from tkinter import *
from quizzler_files.quiz_brain import QuizBrain
THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain ):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=50, pady=50, bg=THEME_COLOR)

        self.label = Label(text="Score: 0", bg=THEME_COLOR, fg="white")
        self.label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250)
        self.question_text = self.canvas.create_text(150, 125, width=280, text="text", font=("Arial", 20, "italic"), fill=THEME_COLOR)
        self.canvas.grid(row=1, column=0, columnspan= 2, pady= 50 )

        right_img = PhotoImage(file="./quizzler_files/images/true.png")
        wrong_img = PhotoImage(file="./quizzler_files/images/false.png")

        self.right_button = Button(image=right_img, highlightthickness=0, command=self.true_pressed)
        self.right_button.grid(row=2, column=0)

        self.wrong_button = Button(image=wrong_img, highlightthickness=0, command=self.false_pressed)
        self.wrong_button.grid(row=2, column=1)

        self.get_next_question()
    
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        self.label.config(text=f"Score: {self.quiz.score}")
        if (self.quiz.still_has_questions()):
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
            self.buttons_state(ACTIVE)
        else:
            self.canvas.itemconfig(self.question_text, text="End of quiz")
            self.buttons_state(DISABLED)


    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer("False"))


    def buttons_state(self,state:str):
        self.right_button.config(state=state)
        self.wrong_button.config(state=state)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)