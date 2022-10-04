# this program shows how many given numbers is prime

from functions import is_prime


n = int(input('Enter count of numbers: '))
arr = []

print('Enter numbers: ')
for i in range(n):
    a = int(input())
    arr.append(a)

c = 0
for i in arr:
    if is_prime(i):
        c += 1

print('Prime numbers total: ' + str(c))







