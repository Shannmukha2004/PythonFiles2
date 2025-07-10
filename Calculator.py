class Claculator:
    def addition(self,a,b):
        return a+b
    def subtraction(self,a,b):
        return a-b
    def multiplication(self,a,b):
        return a*b
    def division(self,a,b):
        try:
            res=a/b
            return res
        except ZeroDivisionError:
            return 'Error : Division by zero is not allowed'

c=Claculator()
print(c.addition(10,20))
print(c.subtraction(10,20))
print(c.multiplication(10,20))
print(c.division(10,0))