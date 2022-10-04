# this program shows how many given numbers is prime

from functions import is_prime


n = int(input('Enter count of numbers: '))
c = 0

print('Enter numbers: ')
for i in range(n):
    if is_prime(int(input())):
        c += 1

print('Prime numbers total: ' + str(c))







