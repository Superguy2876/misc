def part1():
    import os
    rpsDictionary = {}

    # A = Rock, B = Paper, C = Scissors
    # X = Rock, Y = Paper, Z = Scissors

    # X = 1 point, Y = 2 points, Z = 3 points

    # Also for each round, a loss is 0 points, a draw is 3 point, and a win is 6 points

    # your score for the round is the sum of your choice and the outcome.

    # add possible rounds to the dictionary
    # A = Rock, and X = Rock, so you get 1 point for choosing Rock and 3 points for drawing.
    rpsDictionary["A X"] = 4

    # A = Rock, and Y = Paper, so you get 2 point for choosing Rock and 6 points for winning.
    rpsDictionary["A Y"] = 8

    # A = Rock, and Z = Scissors, so you get 3 point for choosing Scissors and 0 points for losing.
    rpsDictionary["A Z"] = 3

    # B = Paper, and X = Rock, so you get 1 point for choosing Rock and 0 points for losing.
    rpsDictionary["B X"] = 1

    # B = Paper, and Y = Paper, so you get 2 point for choosing Paper and 3 points for drawing.
    rpsDictionary["B Y"] = 5

    # B = Paper, and Z = Scissors, so you get 3 point for choosing Scissors and 6 points for winning.
    rpsDictionary["B Z"] = 9

    # C = Scissors, and X = Rock, so you get 1 point for choosing Rock and 6 points for winning.
    rpsDictionary["C X"] = 7

    # C = Scissors, and Y = Paper, so you get 2 point for choosing Paper and 0 points for losing.
    rpsDictionary["C Y"] = 2

    # C = Scissors, and Z = Scissors, so you get 3 point for choosing Scissors and 3 points for drawing.
    rpsDictionary["C Z"] = 6

    #print current directory
    print(os.getcwd())


    # read file from AoC2022 directory
    with open('AoC2022\day2_01_input.txt') as file:
        # map the file to the dictionary, and sum the results, stripping the new line character
        print(sum(map(lambda x: rpsDictionary[x.strip()], file)))

def part2():
    # A = Rock, B = Paper, C = Scissors
    # X = Choose lose, Y = Choose draw, Z = Choose win

    # rock = 1 point, paper = 2 points, scissors = 3 points
    # lose = 0 points, draw = 3 point, win = 6 points

    # your score for the round is the sum of your choice and the outcome.

    rpsDictionary = {}

    # add possible rounds to the dictionary
    # A = Rock, and X = Choose lose, so you get 3 point for choosing scissor and 0 points for losing.
    rpsDictionary["A X"] = 3

    # A = Rock, and Y = Choose draw, so you get 1 point for choosing rock and 3 points for drawing.
    rpsDictionary["A Y"] = 4

    # A = Rock, and Z = Choose win, so you get 2 point for choosing paper and 6 points for winning.
    rpsDictionary["A Z"] = 8

    # B = Paper, and X = Choose lose, so you get 1 point for choosing rock and 0 points for losing.
    rpsDictionary["B X"] = 1

    # B = Paper, and Y = Choose draw, so you get 2 point for choosing paper and 3 points for drawing.
    rpsDictionary["B Y"] = 5

    # B = Paper, and Z = Choose win, so you get 3 point for choosing scissors and 6 points for winning.
    rpsDictionary["B Z"] = 9

    # C = Scissors, and X = Choose lose, so you get 2 points for choosing paper and 0 points for losing.
    rpsDictionary["C X"] = 2

    # C = Scissors, and Y = Choose draw, so you get 3 point for choosing scissors and 3 points for drawing.
    rpsDictionary["C Y"] = 6

    # C = Scissors, and Z = Choose win, so you get 1 point for choosing rock and 6 points for winning.
    rpsDictionary["C Z"] = 7

    # read file from AoC2022 directory
    with open('AoC2022\day2_01_input.txt') as file:
        # map the file to the dictionary, and sum the results, stripping the new line character
        print(sum(map(lambda x: rpsDictionary[x.strip()], file)))

if __name__ == "__main__":
    part1()
    part2()