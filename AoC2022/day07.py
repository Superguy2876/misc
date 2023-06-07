from dataclasses import dataclass, field
from pprint import pprint

@dataclass
class directory:
    name: str
    parent: 'directory' = None
    children: dict = field(default_factory=dict)

    def __init__(self, name: str, parent = None) -> None:
        self.name = name
        if parent == None:
            self.parent = self
        else:
            self.parent = parent
        
        self.children = {}

    def size(self):
        return sum (child.size() for child in self)
    
    def __iter__(self):
        return iter(self.children.values())

@dataclass
class file:
    name: str
    _size: int
    parent: 'directory'

    def __init__(self, size: int, name: str, parent = None) -> None:
        self._size = size
        self.name = name
        self.parent = parent

    def size(self):
        return self._size

def detect_type(line: str):
    # possible line start: "$", "dir", or a file in the format "size filename"
    # "$" is a command either "ls" or "cd"
    # "cd" is followed by a directory name or ".."
    # "dir" is followed by a directory name
    if line.startswith("$ cd"):
        return "cd"
    elif line.startswith("$ ls"):
        return "ls"
    elif line.startswith("dir"):
        return "dir"
    else:
        return "file"



def get_input():
    with open("AoC2022/day07_input.txt") as f:
        return list([line.strip() for line in f.readlines()])

def get_directory_size_list(folder: directory):
    return get_directory_size_helper(folder, [])

def get_directory_size_helper(folder: directory, size_list: list):
    for item in folder:
        if isinstance(item, directory):
            size_list.append((item.name, item.size()))
            size_list = get_directory_size_helper(item, size_list)
    return size_list
        

def part1():
    input  = get_input()
    root = directory("/")
    current_dir = root
    # remove the first line
    input.pop(0)

    for line in input:
        line_type = detect_type(line)
        if line_type == "cd":
            if line.endswith(".."):
                current_dir = current_dir.parent
            else:
                dir_name = line.split(" ")[2]
                current_dir = current_dir.children[dir_name]
        elif line_type == "ls":
            pass
        elif line_type == "dir":
            dir_name = line.split(" ")[1]
            current_dir.children[dir_name] = directory(dir_name, current_dir)
        elif line_type == "file":
            file_size, file_name = line.split(" ")
            current_dir.children[file_name] = file(int(file_size), file_name, current_dir)

    size_list = get_directory_size_list(root)
    # filter for all directories with size < 100000
    size_list = list(filter(lambda x: x[1] < 100000, size_list))
    print(size_list)

    # sum the sizes of all directories with size < 100000
    print(sum([x[1] for x in size_list]))
    

def part2():
    total_disk_size = 70000000
    unused_disk_target = 30000000

    input  = get_input()
    root = directory("/")
    current_dir = root
    # remove the first line
    input.pop(0)

    for line in input:
        line_type = detect_type(line)
        if line_type == "cd":
            if line.endswith(".."):
                current_dir = current_dir.parent
            else:
                dir_name = line.split(" ")[2]
                current_dir = current_dir.children[dir_name]
        elif line_type == "ls":
            pass
        elif line_type == "dir":
            dir_name = line.split(" ")[1]
            current_dir.children[dir_name] = directory(dir_name, current_dir)
        elif line_type == "file":
            file_size, file_name = line.split(" ")
            current_dir.children[file_name] = file(int(file_size), file_name, current_dir)

    size_list = get_directory_size_list(root)

    # sum the sizes of all directories
    used_disk = sum([x[1] for x in size_list])
    print(f"Used disk: {used_disk}")

    # calculate the unused disk
    unused_disk = total_disk_size - used_disk
    print(f"Unused disk: {unused_disk}")

    # sort the size list by size in acending order
    size_list.sort(key=lambda x: x[1])

    for directory in size_list:
        if used_disk - directory[1] < unused_disk_target:
            print(f"Directory {directory[0]} can be deleted")
            break

    pass

if __name__ == "__main__":
    # part1()
    part2()