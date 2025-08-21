# #Kvadrat
def kvadrat(x):
    return x**2
#
# #kub
def kub(x):
    return x**3
#
# #ildiz
def ildiz(x):
    return x**0.5

# TUB son
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def tub_son(num):
    if is_prime(num):
        print(num, "is a prime number.")
    else:
        print(num, "is not a prime number.")


def tub_son(num):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                print(num, "is not a prime number.")
            break
        else:
            print(num, "is a prime number.")

    else:
        print(num, "is not a prime number.")
