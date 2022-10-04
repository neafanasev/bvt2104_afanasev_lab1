# this program shows how many given numbers is prime

from functions import is_prime, is_even


n = int(input('Enter count of numbers: '))
c = 0
e = 0

print('Enter numbers: ')
for i in range(n):
    a = int(input())
    if is_prime(a):
        c += 1
    if is_even(a):
        e += 1


print('Prime numbers total: ' + str(c))
print('Even numbers total: ' + str(e))







