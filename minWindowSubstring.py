from collections import Counter

def minWindow( input: str, substring: str) -> str:
    left = 0
    right = 0

    subStringTuple = (0,len(input))

    substringSet = set(substring)
    subCounter = Counter(substring)
    output = ''

    while right <= len(input):

        tempString = ''.join([c for c in input[left:right] if c in substringSet])

        tempCounter = Counter(tempString)

        if tempCounter == subCounter and (right - left) <= (subStringTuple[1] - subStringTuple[0]):
            subStringTuple = (left, right)
            output = input[subStringTuple[0] : subStringTuple[1]]
            left +=1
            continue

        if input[right-1] in tempCounter and tempCounter[input[right-1]] > subCounter[input[right-1]]:
            left+=1
            continue
        
        right += 1

    return output

print(minWindow("ADOBECODEBANC", "ABC"))