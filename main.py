from functions import is_prime, is_even
from func1 import *

n = int(input('Enter count of numbers: '))
c, e, s = 0, 0, 0

print('Enter numbers: ')
for i in range(n):
    a = int(input())
    if is_prime(a):
        c += 1
    if is_even(a):
        e += 1
    if is_square(a):
        s += 1

print('Prime numbers total: ' + str(c))
print('Even numbers total: ' + str(e))
print('Special numbers total: ' + str(s))







