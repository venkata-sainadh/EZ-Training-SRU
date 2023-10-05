#Neon Numbers
def is_neon(n):
    square = n * n
    sum_of_digits = 0
    while square > 0:
        sum_of_digits += square % 10
        square //= 10
    return sum_of_digits == n
n=int(input())
print(is_neon(n))
