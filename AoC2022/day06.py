def get_input():
    with open("AoC2022/day06_input.txt") as f:
        return f.readline()

def part1():
    input_string = get_input()
    four_group = []
    for index, character in enumerate(input_string):
        while character in four_group:
            four_group.pop(0)
        four_group.append(character)
        print(four_group)
        if len(four_group) == 4:
            print(f"Four group found at {index + 1} characters")
            break

def part2():
    input_string = get_input()
    fourteen_group = []
    for index, character in enumerate(input_string):
        while character in fourteen_group:
            fourteen_group.pop(0)
        fourteen_group.append(character)
        print(fourteen_group)
        if len(fourteen_group) == 14:
            print(f"Four group found at {index + 1} characters")
            break

if __name__ == "__main__":
    part1()
    part2()