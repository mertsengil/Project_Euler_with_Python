# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.
def palindrome(x):
    
    if(str(x) == str(x)[::-1]):           
        return True
    else:
        return False
            
number_list = []
for i in range(100,1000):
    for j in range(100,1000):
        number_list.append(i*j)
        
palindrome_l = []

for k in number_list:
    if(palindrome(k)):
        palindrome_l.append(k)

print(max(palindrome_l))
        



                
        
    
