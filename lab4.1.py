import math

def func1(x):
    if(x > 0):
        return ((math.cos(x)+math.log(abs(x)+1))/(math.pow(math.e, 0.7*x)+math.pow(4, 3.3*x+1))-0.9*math.pow(x, math.sqrt(2*x)))

a = float(input("x:"))
y = func1(a)
print(y)