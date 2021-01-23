# when we pass **as parameter WE can pass multiple key value pair
def save_user(**user):
    print(user)
    # to get value of  various key in dictionary
    print(user["id"])

#it return object are dictionary
    save_user(id=1,name="jhon", age= 22)
  