#quiz oop

from quiz_files.question_model import Question
from quiz_files.data import question_data
from quiz_files.quiz_brain import QuizBrain

question_bank = []

for data in question_data:
    text = data['text']
    answer = data['answer']
    question_bank.append(Question(text,answer))

quiz_brain = QuizBrain(question_bank)

while quiz_brain.still_has_questions():
    quiz_brain.next_question()

print("You've completed the quiz :)")
print(f"Your final score was: {quiz_brain.score}/{quiz_brain.question_number}")