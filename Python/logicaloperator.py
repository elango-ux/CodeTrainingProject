
#and operator
high_income = True
good_credit = False
if high_income and good_credit:
    print("eligible")
else: 
    print("not eligible")
# or operator
    high_income = True
good_credit = False
if high_income or good_credit:
    print("eligible")
else: 
    print("not eligible") 
#not operator
high_income = True
good_credit = False
student = True
if not student:
    print("eligible")
else: 
    print("not eligible") 
# complex 
high_income = True
good_credit = False
student = False
if(high_income or good_credit) and not student:
    print("eligible")
else:
    print("not eligible")
    
 
   