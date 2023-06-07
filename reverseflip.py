def reverseflip(input):
    # string to lowercase
    input = input.lower()
    # alphabet as a string
    s = "abcdefghijklmnopqrstuvwxyz"
    # reverse alphabet
    rs = s[::-1]

    # read input, then reverse the input
    input = input[::-1]
    # then map the input to the reverse alphabet
    output = [rs[s.index(c)] for c in input]
    # then join the output
    output = "".join(output)
    return output

print(reverseflip(input('Enter a string: ')))