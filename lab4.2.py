import math

def func1(x, y, z):
    if(y!=0):
        return ((0.7*math.cos(x)+math.log(abs(y)))**(1/5)+math.pow(math.e, z+x))

a = float(input("x:"))
b = float(input("y:"))
c = float(input("z:"))
result = func1(a, b, c)
print(result)