"""
Advent of Code 2023 - Day 1

Start: 1. Dec 2023 - 14:15
Finish: 1. Dec 2023 - 14:50
Notes:
    Cringe how long I took for part 2, but I replaced the spelled numbers
    in order of their value first, e.g.
    eightwo3sdas3 -> eigh23sdas3
"""


def part1():
    print("Solution Part 1")
    sum = 0
    with open("data", "r") as file:
        for line in file:
            first_num = -1
            last_num = 0
            for char in line:
                if char.isnumeric():
                    if first_num == -1:
                        first_num = int(char)
                    last_num = int(char)
            sum += first_num * 10 + last_num
    print(sum)


def part2():
    print("Solution Part 2")
    spelled = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    sum = 0
    with open("data", "r") as file:
        for line in file:
            first_num = -1
            last_num = 0
            for i in range(len(line)):
                val = -1
                if line[i].isnumeric():
                    val = int(line[i])
                else:
                    for index, replacement in enumerate(spelled):
                        if line[i:].startswith(replacement):
                            val = index+1
                if val >= 0:
                    if first_num == -1:
                        first_num = val
                    last_num = val
            sum += first_num * 10 + last_num
    print(sum)

def main():
    print("Solution for Day 1")
    part1()
    part2()



if __name__ == "__main__":
    main()

