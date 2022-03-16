# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

def prime_check(x):
    for i in range(2,int(x ** 0.5) + 1):
        if x%i ==0:
            return False
    return True

biggest_prime = 1
for i in range(2,int(600851475143 ** 0.5)):
    if (600851475143 % i == 0 and prime_check(i)):
        biggest_prime = i

print(biggest_prime)
