#Version 0.0.1 11.09.2024

#Обьявление класса
class CCalculator:
    def __init__(self, x, y):
        self.x = 0  
        self.y = 0
    
    def Sum(self):
        return self.x + self.y
    
    def Mult(self):
        return self.x * self.y

#Object creating
MyCalc = CCalculator(3,2)

#Выполнение методов обьекта
print(MyCalc.Sum())
print(MyCalc.Mult())
