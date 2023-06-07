# read the characters from the standard input and print them in the requested order. there are 3 inputs, the number of characters as int, the list of characters as a string, and the order of characters to be printed from the string as a list of ints. the output is the string of characters in the order specified by the list of ints.
# line 1: n
# line 2: string of characters
# line 3: list of ints

n = int(input())
s = input()
order = [int(x) for x in input().split()]
for i in order:
    print(s[i], end="")

