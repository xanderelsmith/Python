

class  Student:
    def __init__(self,name,classno,dOB):
        self.name=name
        self.classno=classno
        self.dOB=dOB
    
newStudent=Student('Emmanuel','pry21',123)
print(newStudent.classno)


class Product:
    def __init__(self,product_name,brand_name,price):
        self.product_name=product_name
        self.brand_name=brand_name
        self.price=price
        

        
laptop =Product('dell','vostro',1000)
print(laptop.brand_name)
