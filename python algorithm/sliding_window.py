def maxsum(arr, window_size):
    # to find length of array
    arraysize = len(arr)
    #arraysize is greater than window_size then invalid operation 
    if arraysize <= window_size:
        print("invalid operation")
        return -1
    # findsum of window size 2 but could not understand why bracket [] is used
    windowsum = sum([arr[i]  for i in range(window_size)])
    print(windowsum)
    maxsum = windowsum
    # delete first element in subarray by  and add next element in the array
    for i in range(arraysize-window_size):
       print(arr[i])

      





# sum of maximum subarray size 2
#step 1 declare array
arr = [80,-50,90,100]
# subarray of size 2
k = 2
answer = maxsum(arr, k)
print(answer)
