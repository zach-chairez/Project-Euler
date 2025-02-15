''' Sum Square Difference '''

''' Prompt ''' 
# The sum of squares of the first ten natural numbers is:
# 1^2 + 2^2 + ... + 10^2 = 385

# The square of the sum of the first ten natuarl numbers is:
# (1 + 2 + ... + 10)^2 = 55^2 = 3025

# The difference between the sum of squares of the first 
# ten natural numbers and the square sum is:
# 3025 - 385 = 2640

''' Question ''' 
# Find the difference between the sum of the squares of the first 
# n-natural numbers and the square of the sum.

def sum_square_difference(n):

    sum_square = n*(n+1)*(2*n+1)/6
    square_sum = sum(range(n+1))**2
    
    return square_sum - sum_square       

sum_square_difference(10) # Output:  2,640
sum_square_difference(20) # Output:  41,230
sum_square_difference(100) # Output: 25,164,150  
        
