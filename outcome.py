from math import factorial




# function for combinations
def combinations(n, k):
    return factorial(n) / (factorial(k) * factorial(n - k))


# function for binomial distribution
def binomial(n, p, k):
    return combinations(n, k) * (p ** k) * ((1 - p) ** (n - k))


print(binomial(10, 0.003, 2) * 100)
print(binomial(10, 0.003, 3) * 100)
print(binomial(10, 0.003, 4) * 100)
print(binomial(10, 0.003, 5) * 100)
print(binomial(10, 0.003, 6) * 100)
print(binomial(10, 0.003, 7) * 100)
print(binomial(10, 0.003, 8) * 100)
print(binomial(10, 0.003, 9) * 100)
print(binomial(10, 0.003, 10) * 100)
