cheapFurniture=[]
expensiveFurniture=[]

# this is a furniture class
class Furniture :
    def __init__(self,name,price):
        self.name=name
        self.price=price
        
    # this is a method(A function in a class) 
           
    def sortIntoPosition(self):
        if self.price>160:
            expensiveFurniture.append(self.name)           
        else:
            cheapFurniture.append(self.name)
            
 # these are the objects with their data and methods
f1=Furniture('Chair',100)
f1.sortIntoPosition()
f2=Furniture('table',200)
f2.sortIntoPosition()
f3=Furniture('bench',150)
f3.sortIntoPosition()

selectedFurniture=[f1,f2,f3]

        
# these are the prints of their methods function
print(cheapFurniture)
print(expensiveFurniture)