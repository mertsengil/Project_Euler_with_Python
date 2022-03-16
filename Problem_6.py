#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

def sum_of_square():
    total = 0
    for i in range(1,101):
        total += i**2
    return total

def square_of_sum():
    total = 0
    for i in range(1,101):
        total += i
    return total**2

print(square_of_sum() - sum_of_square())
