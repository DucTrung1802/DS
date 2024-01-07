from math import sqrt


def isPrime(input):
    if input == 0:
        return False
    if input == 1:
        return False
    for i in range(2, int(sqrt(input)) + 1):
        if input % i == 0:
            return False
    return True


# for i in range(100):
#     print(str(i) + ": " + str(isPrime(i)))

