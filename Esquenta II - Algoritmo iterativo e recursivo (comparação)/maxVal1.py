
def maxVal1(A,n):    
    maxi= A[0]
    for i in range(n):
        if(A[i]>maxi):
            maxi=A[i]
    return maxi