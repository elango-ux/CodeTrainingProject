
# problem: moving zero to end of the array and non zero at begining
arr = [0, 1, 0, 3, 12]
# increamting 
j = 0
#loop over arr list
for num in arr:
    # num != 0 check  eixstence of non zero integer
    if num != 0:
        # it bring non zero integer to begining one by one in sequence
        arr[j] = num
        # increment j by 1  
        j += 1
# to loop  range between j and arr list length because to to put zero to next of non zero integer 
for i in range(j,len(arr)):
    # it put sequence  0 next to non zero number
    arr[i] = 0
print(arr)


         



    