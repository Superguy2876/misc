# You begin with a number N. You can do one of two operations:

# Operation 1: Divide the number N by 2 (Note that if N is odd this would not result in an integer, and it would be impossible to reach 1)

# Operation 2: Subtract 1 from N

# However, you only can do operation 1, dividing N by 2, a maximum of A times.
# You want to reach the number 1 in the minimum operations. Print X, the lowest number of operations it takes.

n = int(input())
a = int(input())

count = 0
while n > 1:
    if n % 2 == 1:
        n -= 1
        a -= 1
    if n % 2 == 0:
        n = n // 2
        a -= 1
    count += 1

print(count)

