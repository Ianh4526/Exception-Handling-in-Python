# Exception Handling in Python Guided Project

# Module One Examples
# Example One - Syntax Error
print(15/5))

# Example Two - Exception Division by Zero
print(15/0)

# Example Three - Greeting Name Error Example
greeting='Hello World'
print(greetings)

# Example Four - TypeError Exception
num1 = 5
num2 = 'six'
result = num1+num2


# Module Two Examples
# Example Five - Raising an Exception
name = input("Enter your name?")
age = int(input("Enter your age?"))
print("Your name is: "+name)
if age<18:
    raise ValueError("Error: you need to be over 18")
else:
    print("Your age is: "+str(age))

# Example Six - Raising an Exception - number less than 5
number=4
if number<5:
    raise Exception("Error: number needs to be above 5")


# Module Three Examples
# AssertionError Exception 
x=1
y=0
assert y != 0, "Invalid Operation"
print(x/y)

# AssertionError Exception Example Two
def print_age(age):
    assert age>0, "The value for age has to be greater than zero"
    print("Your age is :"+str(age))

print_age(-10)


# Module Four Examples
# Try and Except Block Example
try:
    num1 = 4
    num2 = 0
    result = num1/num2
    print(result)
except ZeroDivisionError as e:
    print(e)

# Try, Except and Else Example
try:
    num1 = '4'
    num2 = 2
    result = num1 + num2
    print("End of try block")
except TypeError:
    print("TypeError: Value has to be an integer")
else:
    print("No Exception Raised")


# Module Five Example
# The Finally Clause
try:
    f=open("example.txt", encoding='utf-8')
except FileNotFoundError:
    print("FileNotFoundError: The file is not found")
finally:
    f.close()