
def maxVal2(A,inicio,fim):
    if ((fim-inicio)<=1):
        return max(A[inicio],A[fim])
    else:
        m = int((inicio + fim)/2)
        v1 = maxVal2(A,inicio,m)
        v2 = maxVal2(A,m+1,fim)
        return max(v1,v2)