# read a file
with open('day1_01_input.txt') as file:
    # read the file into a list of lists, splitting on an empty line and converting each line to an int
    current_elf = []
    elf_list = []
    for line in file:
        try:
            current_elf.append(int(line))
        except ValueError:
            elf_list.append(current_elf)
            current_elf = []
    elf_list.append(current_elf)
    
    elf_sum = [sum(elf) for elf in elf_list]
    

    print(sum( sorted( elf_sum )[-3:] ))