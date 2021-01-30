from timeit import timeit

code2 = """
def calculate_xfactor(age):
    if(age < 0):
        # NONE IS Object that represent  no value
         return None
    
    return 10 / age

xfactor =  calculate_xfactor(-1)
if xfactor == None:
    pass
"""
print("code2", timeit(code2,  number = 10000))