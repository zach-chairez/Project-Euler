''' Prompt:
    If we list all the natural numbers below 10 that 
    are multiples of 3 or 5, we get 3,5,6, and 9.  The sum
    of these multiples is 23.

    Question:  Find the sum of all the multiples of 3 or 5 below 1000:      
 '''

import time 
 
def method_one(N1,N2,large_N):
    
    sum_N1 = sum(range(0,large_N+1,N1))
    sum_N2 = sum(range(0,large_N+1,N2))
    sum_N1N2 = sum(range(0,large_N+1,N1*N2))

    return sum_N1+sum_N2-sum_N1N2

method_one_time = time.time()
method_one(3,5,1000)
method_one_time = time.time() - method_one_time

print("Method 1 took " + str(method_one_time) + " seconds")


     