##Calculator

x = int(input("Enter a no: "))
        
sign = (" * for multipication, / for division, + for addition, - for substraction, ** for power ") #Telling user the functions of signs
print(sign)

op = input('Enter sign: ')

y = int(input('Enter other no: '))

def add(x,y):             #for addition
    print(x+y)
def subtract(x,y):        #for substraction
    print(x-y)
def multiply(x,y):        #for multipication
    print(x*y)
def divide(x,y):          #for division
    print(x/y)
def power(x,y):           #for power
    print(x**y)

if (op == '-'):
    subtract(x,y)
elif (op == '+'):
    add(x,y)
elif (op == '*'):
    multiply(x,y)
elif (op == '/'):
    divide(x,y)
elif (op == '**'):
    power(x,y)