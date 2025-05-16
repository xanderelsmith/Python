from data import question_data
from question_model import Question
from quiz_brain import  QuizBrain

quizbrain=QuizBrain(question_data)
isRunnning=True
while isRunnning:
    isRunnning=quizbrain.nextQuestion()