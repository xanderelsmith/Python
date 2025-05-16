
from question_model import Question


class QuizBrain:
    def __init__(self,quizlist:list[Question]):
        self.questionIndex=0
        self.questionList=quizlist
    
        
        

    def nextQuestion(self):        
            response =input(f'Q{self.questionIndex+1}.{self.questionList[self.questionIndex].text} (True/False)').lower()
            if response==self.questionList[self.questionIndex].answer.lower():
                print('Correct')
            else:
                print('Wrong')
            return self.counter()
            
    
    
    def counter(self):        
        if self.questionIndex+1>=len(self.questionList):             
            return False
        else:
            print('Countering')         
            self.questionIndex=self.questionIndex+1
            return True