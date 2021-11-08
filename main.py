from Data import question_data
from Question_Model import Question
from quiz_brain import QuizBrain
question_bank = []

for n in range(0, len(question_data)):
    question_bank.append(Question(question_data[n]["text"], question_data[n]["answer"]))


quiz = QuizBrain(question_bank)

while quiz.still_has_questions() == True:
    quiz.next_question()

else:
    print("You have completed the quiz.")
    print(f"Your final score is {quiz.score}.")