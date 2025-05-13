class User:
    def __init__(self,userId):
        self.userId=userId
        self.followers=0
    def assign_followers(self,followers:int):
        self.followers= followers
        

