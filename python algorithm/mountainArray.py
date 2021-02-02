class Solution:
    def validMountainArray(self, A):
        
            if len(A) < 3:
                return False
            i = 1
            while i < len(A) and A[i] > A[i-1]:
                
                i += 1
            while i < len(A) and A[i] < A[i-1]:
                i += 1 
                print(i)
                return i == len(A)
ob = Solution()
print(ob.validMountainArray([0, 3, 2, 1]))
