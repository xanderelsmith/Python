from data import question_data
from question_model import Question
from quiz_brain import  QuizBrain

quizbrain=QuizBrain(question_data)

while quizbrain.still_has_questions():
    isRunnning=quizbrain.nextQuestion()
print("You have completed the quiz ")
print(f"Your final score was {quizbrain.score}/{len(question_data)} ")