# Approach 1
def min_max_elements(A):
    A = sorted(arr)
    minimum_element = A[0]
    maximum_element = A[-1]
    return (minimum_element, maximum_element)


#Approach 2   - TC => O(N)

def max_min_elements(A):
    myMax=A[0]
    myMin=A[0]
    for d in A:
        if(d> myMax):
            myMax=d
        if(d<myMin):
            myMin=d 
    return(myMin,myMax)
