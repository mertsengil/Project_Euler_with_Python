# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.
import math
def prime_finder(x):
    if x == 1:
        return False,int(x)
    elif x == 2:
        return True,int(x)
    else:
        for i in range(2,int(math.sqrt(x)+1)):
            if (x%i == 0):
                return False,int(x)
                break
            
        return True,int(x)
    
total = 0
for i in range(1,2000000):
    
    if(prime_finder(i)[0]):

        total += prime_finder(i)[1]


print(total)
    
        

        

