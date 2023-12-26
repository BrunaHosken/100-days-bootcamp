#day 34
#quizzler trivia

from quizzler_files.question_model import Question
from quizzler_files.data import question_data
from quizzler_files.quiz_brain import QuizBrain
from quizzler_files.ui import QuizInterface

question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)
quiz_ui = QuizInterface(quiz)

