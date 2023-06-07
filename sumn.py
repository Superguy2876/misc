# Given a number N sum up all even numbers from 2 to N.
n = int(input())

sum = 0
for i in range(2, n+1, 2):
    sum += i

print(sum)

print("K")