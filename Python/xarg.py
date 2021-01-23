# *numbers is a collection of arguments and it return (2,3,4,4,5) and it is iterablelike list
def multiply(*numbers):
    total = 1
    for number in numbers:
        print(number)
        total *= number 
    
    return total



print(multiply(2,3,4,4,5))