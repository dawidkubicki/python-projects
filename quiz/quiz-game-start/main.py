from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for question_item in question_data:
    question = Question(question_item["question"], question_item["correct_answer"])
    question_bank.append(question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("\nYou've completed the quiz!")
print(f"Your final score is {quiz.score}/{len(quiz.question_list)}")
