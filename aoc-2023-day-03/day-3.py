"""
Advent of Code 2023 - Day 3

Start: 3. Dec 2023 - 14:13
Finish: 3. Dec 2023 - 15:09
Notes:
    Took waaaay too long, even though I didn't do any mistakes. I am getting too old for this
"""


def part1():
    print("Solution Part 1")
    schematic = []
    with open("data", "r") as file:
        for line in file:
            schematic.append(list(line.replace("\n", "")))

    parts = []
    for i, row in enumerate(schematic):
        for j, character in enumerate(row):
            if character.isnumeric():
                if j > 0 and row[j-1].isnumeric():
                    continue
                number = ""
                is_part_number = False
                k = j
                while k < len(row):
                    character = row[k]
                    if not character.isnumeric():
                        break
                    number += character
                    for offset_i in range(-1, 2):
                        for offset_k in range(-1, 2):
                            new_i = i + offset_i
                            new_k = k + offset_k
                            if new_i < 0 or new_i >= len(schematic):
                                continue
                            if new_k < 0 or new_k >= len(schematic[new_i]):
                                continue
                            if schematic[new_i][new_k] != "." and not schematic[new_i][new_k].isnumeric():
                                is_part_number = True
                    k += 1
                if is_part_number:
                    parts.append(int(number))
    print(sum(parts))


def part2():
    print("Solution Part 2")
    schematic = []
    with open("data", "r") as file:
        for line in file:
            schematic.append(list(line.replace("\n", "")))

    gear_ratios = []
    for i, row in enumerate(schematic):
        for j, character in enumerate(row):
            if character == "*":
                connected_parts = set()
                for offset_i in range(-1, 2):
                    for offset_j in range(-1, 2):
                        new_i = i + offset_i
                        new_j = j + offset_j
                        if new_i < 0 or new_i >= len(schematic):
                            continue
                        if new_j < 0 or new_j >= len(schematic[new_i]):
                            continue
                        if schematic[new_i][new_j].isnumeric():
                            while new_j >= 0 and schematic[new_i][new_j].isnumeric():
                                new_j -= 1
                            new_j += 1
                            part_location = (new_i, new_j)
                            part_number = ""
                            while new_j < len(schematic[new_i]):
                                digit = schematic[new_i][new_j]
                                if digit.isnumeric():
                                    part_number += digit
                                else:
                                    break
                                new_j += 1
                            connected_parts.add((part_location, int(part_number)))

                if len(connected_parts) == 2:
                    gear_ratio = 1
                    for pos, num in connected_parts:
                        gear_ratio *= num
                    gear_ratios.append(gear_ratio)

    print(sum(gear_ratios))



def main():
    print("Solution for Day 3")
    part1()
    part2()


if __name__ == "__main__":
    main()

