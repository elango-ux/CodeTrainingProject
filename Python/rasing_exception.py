def calculate_xfactor(age):
    if(age < 0):
        # IF YOU NEED to throw your own exception message  you can use rasie keyword and valueERROR- TYPE OF ERROR  AND CURLEY BRACKET   DISplay message
        raise ValueError("AGE CANNOT BE LESS THAN ZERO")
    
    return 10 / age
try:
    calculate_xfactor(-1)
except ValueError as error:
    print(error)


