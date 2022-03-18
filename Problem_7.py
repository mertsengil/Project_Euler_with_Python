# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?
def prime_checking(x):

    if x == 1:
        return False
    elif x == 2:
        return True
    else:
        for i in range(2,x):
            if x % i ==0:
                return False
                
        return True

x = 1
counter = 0
while True:
    if (prime_checking(x)):
        counter +=1
    if counter == 10001:
        print(x)
        break

    x+=1


        
