from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for key in question_data:
    question_text = key["question"]
    question_answer = key["correct_answer"]

    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print(f"You've completed the quiz! Your final score was {quiz.score}/{len(question_bank)}")