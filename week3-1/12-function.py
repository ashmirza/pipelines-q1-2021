#Functions only run when called
number1 = int(input("User input: "))
number2 = int(input("User input: "))
def add(num1, num2):
    sumOfNums = num1 + num2
    return sumOfNums

value = add(number1, number2)
print(value)

sumOfNums = add(80, 20)

print(sumOfNums)

# Function definition is here
#def printme( str ):
   #"This prints a passed string into this function"
   #print(str)
   #return;

# Now you can call printme function
#printme("I'm first call to user defined function!")
#printme("Again second call to the same function")