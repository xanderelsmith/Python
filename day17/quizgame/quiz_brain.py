
from question_model import Question


class QuizBrain:
    def __init__(self,quizlist:list[Question]):
        self.current_question_index=0
        self.questionList=quizlist
        self.score=0
    
        
        

    def nextQuestion(self):        
            response =input(f'Q{self.current_question_index+1}.{self.questionList[self.current_question_index].text} (True/False)').lower()
            correct_answer=self.questionList[self.current_question_index].answer.lower()
            return self.checkAnswer(user_answer=response,correct_answer=correct_answer)
            
    
    def still_has_questions(self):
        return self.current_question_index<len(self.questionList)
    def checkAnswer(self,user_answer,correct_answer):
        if user_answer==correct_answer:
                self.score+=1
                print('Correct')
        else:
                print('Wrong')      
        self.current_question_index+=1
         