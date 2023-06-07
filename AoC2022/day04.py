
def get_input() -> list:
    # get the input from the file
    input_list : list = []
    with open("AoC2022/day04_input.txt", "r") as f:
        for line in f:
            # each line has the form 67-84,66-87
            # add each line to the list as a tuple of ranges
            input_list.append(tuple(map(lambda x: range(int(x.split("-")[0]), int(x.split("-")[1]) + 1), line.strip().split(","))))
    
    return input_list

        
def is_range_within(inner_range, outer_range):
    return outer_range.start <= inner_range.start and inner_range.stop <= outer_range.stop

def is_range_overlap(range1, range2):
    return range1.stop > range2.start and range1.start < range2.stop

def part1():
    ranges = get_input()
    
    # compare each range to see if it is within the other range
    contained = 0
    print(len(ranges))
    for pair in ranges:
        if is_range_within(pair[0], pair[1]) or is_range_within(pair[1], pair[0]):
            contained += 1
    
    print(contained)
        

def part2():
    ranges = get_input()
    
    # compare each range to see if it overlaps with the other range
    overlap = 0
    for pair in ranges:
        if is_range_overlap(pair[0], pair[1]) or is_range_overlap(pair[1], pair[0]):
            overlap += 1
    
    print(overlap)






if __name__ == "__main__":
    part1()
    part2()