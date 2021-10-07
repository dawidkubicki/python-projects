from question_model import Question
from data import question_data

question_bank = []

for question_item in question_data:
    question = Question(question_item["text"], question_item["answer"])
    question_bank.append(question)
#
# for question in question_bank:
#     print(question.text)
#     print(question.answer)
