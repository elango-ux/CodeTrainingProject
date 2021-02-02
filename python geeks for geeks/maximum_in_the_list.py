class Maximum:
    def largest(self, A):
        max = A[0]
        
        for i in range(1,len(A)):
            if A[i] > max:
                max = A[i]

        return max



ma = Maximum()
largest_number = ma.largest([23, 43,56])
print(largest_number)