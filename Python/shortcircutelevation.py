# and short circuit
high_income = True
good_credit = False
student = False
if high_income and good_credit  and  not student:
  print("eligible")
else:
    print("not eligible")
 # or short circuit
high_income = True
good_credit = False
student = False
if high_income or good_credit or not student:
    print("eligible")