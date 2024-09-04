#Обьявление класса
class CCalculator:
    def __init__(self, x, y):
        self.x = 3
        self.y = 2
    
    def Sum(self):
        return self.x + self.y
    
    def Mult(self):
        return self.x * self.y

#Object creating
MyCalc = CCalculator(3,2)

#Выполнение методов обьекта
print(MyCalc.Sum())
print(MyCalc.Mult())
