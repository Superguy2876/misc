from collections import defaultdict

def get_input() -> list:
    # firest get the input of each line until a blank line, put each line in a list
    cargo_string_list = []
    with open("AoC2022/day05_input.txt", "r") as f:
        for line in f:
            # append line if not empty
            if line.strip():
                cargo_string_list.append(line)
            # otherwise, yield the list
            else:
                yield cargo_string_list
                break
    
        # then get each line until the end of the file
        move_string_list = []
        for line in f:
            move_string_list.append(line)
        yield move_string_list


def extract_cargo(cargo_string: str, cargo_positions: list):
    cargo_list = []
    for index, position in enumerate(cargo_positions):
        if (len(cargo_string) > position) and (cargo_string[position] != " "):
            cargo_list.append((index, cargo_string[position]))
    return cargo_list

def extract_int(string_in: str):
    """Generator that yields each integer in a string"""
    index = 0
    while index < len(string_in):
        if string_in[index].isdigit():
            int_start = index
            while int_start < len(string_in) and string_in[int_start].isdigit():
                int_start += 1
            yield int(string_in[index:int_start])
            index = int_start
        else:
            index += 1

def find_int_positions(string):
    """Generator that yields the positions of each integer in a string"""
    index = 0
    while index < len(string):
        if string[index].isdigit():
            int_start = index
            while int_start < len(string) and string[int_start].isdigit():
                int_start += 1
            yield index
            index = int_start
        else:
            index += 1

def part1():
    cargo_input, move_input  = get_input()

    cargo_positions = list(find_int_positions(cargo_input.pop()))
    
    cargo_towers = defaultdict(list)

    while len(cargo_input) > 0:
        cargo_string = cargo_input.pop()
        cargo_list = extract_cargo(cargo_string, cargo_positions)
        for cargo in cargo_list:
            cargo_towers[cargo[0]].append(cargo[1])
    
    move_list = []
    for move_string in move_input:
        move_list.append(list(extract_int(move_string)))
    
    # for each move of format [number, from, to] do number pops from the from tower and append to the to tower
    for move in move_list:
        for _ in range(move[0]):
            cargo_towers[move[2] -1].append(cargo_towers[move[1] -1].pop())
        

    # print the thing at the top of each tower
    # for i in range(len(cargo_towers)):
    #     print(cargo_towers[i][-1], end="")


def part2():
    cargo_input, move_input  = get_input()

    cargo_positions = list(find_int_positions(cargo_input.pop()))
    
    cargo_towers = defaultdict(list)

    while len(cargo_input) > 0:
        cargo_string = cargo_input.pop()
        cargo_list = extract_cargo(cargo_string, cargo_positions)
        for cargo in cargo_list:
            cargo_towers[cargo[0]].append(cargo[1])
    
    move_list = []
    for move_string in move_input:
        move_list.append(list(extract_int(move_string)))
    
    # for each move of format [number, from, to] slice number of items from the from tower and append to the to tower
    for move in move_list:
        cargo_towers[move[2] -1].extend(cargo_towers[move[1] -1][-move[0]:])
        cargo_towers[move[1] -1] = cargo_towers[move[1] -1][:-move[0]]
        
        

    # print the thing at the top of each tower
    for i in range(len(cargo_towers)):
        print(cargo_towers[i][-1], end="")

if __name__ == "__main__":
    part1()
    part2()
