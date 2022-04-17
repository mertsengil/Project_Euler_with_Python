# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# a2 + b2 = c2
# For example, 32 + 42 = 9 + 16 = 25 = 52.
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.
import math
def Pythagorean(a,b):
    
    c = a**2 + b**2
    c = math.sqrt(c)
    if (a<b<c):
        if(c == int(c)):
            
            return True,c
    return False,c


for a in range (1,1000):
    for b in range (a+1,1000):
         
        if ((Pythagorean(a,b)[0]) and ((Pythagorean(a,b)[1] + a + b) == 1000)):
            
                print(int(a*b*Pythagorean(a,b)[1]))
                break
        
            
    
    
        
        
        



