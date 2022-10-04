# optimal version of the function

def is_prime(n):
    c = 2
    while c < int(n**0.5 + 1):
        if n % c == 0:
            return False
    return True

