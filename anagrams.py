from collections import Counter

strs = ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']

# this function when given a list of strings returns a list of lists of all strings that contain the same letters
def anagrams(strs):
    d = {}
    for s in strs:
        d[tuple(sorted(s))] = d.get(tuple(sorted(s)), []) + [s]
        
    return list(d.values())

list1 = [1,2,3,4]
list2 = [5,6,7,8]
print(list1 + list2)
print(anagrams(strs))