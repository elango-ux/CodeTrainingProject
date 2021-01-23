def binarySearch(arr, target):
    left = 0
   # return index of last element
    right = len(arr)-1
    # left index should be always  less  that right and if  it  become greater loop stop
    while(left <= right):
    # find the middle value   
        mid = left + right // 2
    # check  arr[mid] = target if true the  we got output soreturn mid index    
        if(arr[mid] == target):
           return mid
    #arr[mid] < target   increment 1 in the mid index  
        elif (arr[mid] < target):
          left = mid+1
        else:
           right=mid-1
        return -1
arr = [1,2,3,4,5,6]
target = 3

result = binarySearch(arr , target)
if(result != -1):
    print("element is at present index",result)
else:
    print("element is not present in the array",result)

