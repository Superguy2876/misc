

def get_rucksack() -> list:
    rucksack : list = []
    with open("AoC2022/day3_01_input.txt", "r") as f:
        for line in f:
            rucksack.append(line.strip())

    return rucksack

def get_letter_number(letter: str) -> int:
    # dictionary that maps lowercase letters to numbers 1-26 and uppercase letters to numbers 27-52
    letterDictionary = {}
    for i in range(1, 27):
        letterDictionary[chr(i + 96)] = i
        letterDictionary[chr(i + 64)] = i + 26

    return letterDictionary[letter]


def part1():
    # dictionary that maps lowercase letters to numbers 1-26 and uppercase letters to numbers 27-52
    letterDictionary = {}
    for i in range(1, 27):
        letterDictionary[chr(i + 96)] = i
        letterDictionary[chr(i + 64)] = i + 26


    rucksack : list = get_rucksack()

    print(rucksack)

    priority_total: int = 0

    # for each thing in the rucksack, split it into half
    for thing in rucksack:
        # get the length of the thing
        length = len(thing)
        # get the first half of the thing
        firstHalf = thing[:length // 2]
        # get the second half of the thing
        secondHalf = thing[length // 2:]

        # find the letter that is in both halves
        for letter in firstHalf:
            if letter in secondHalf:
                # if the letter is in both halves, then print the letter
                print(letter)
                
                priority_total += letterDictionary[letter]
                break

    print (priority_total)


def part2():
    rucksack = get_rucksack()
    print(len(rucksack))
    
    total = 0
    while len(rucksack) >= 3:
       
        group = [set(rucksack.pop(0)),set(rucksack.pop(0)),set(rucksack.pop(0))]
        # print (group)

        # find the intersection of the first three sets
        intersection = group[0].intersection(group[1], group[2]).pop()
    
        # add the intersection to the total
        total += get_letter_number(intersection)
    
    print (total)
        








part1()
part2()