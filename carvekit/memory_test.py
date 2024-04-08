from memory_profiler import profile

@profile
def addition():
    a = [1] * (10 ** 1)
    b = [2] * (3 * 10 ** 2)
    sum = a+b

addition()