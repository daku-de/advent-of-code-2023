"""
Advent of Code 2023 - Day 2

Start: 2. Dec 2023 - 14:05
Finish: 2. Dec 2023 - 14:35
Notes:
    
"""

colors = ["red", "green", "blue"]

def part1():
    print("Solution Part 1")
    max_color = {
        colors[0]: 12,
        colors[1]: 13,
        colors[2]: 14
    }
    possible_games = []
    with open("data", "r") as file:
        for line in file:
            game_id = int(line.split(":")[0][5:])
            is_valid = True
            line = line[line.index(":") + 1:]
            line = line.replace("\n", "")
            for draw in line.split(";"):
                drawn = {
                    colors[0]: 0,
                    colors[1]: 0,
                    colors[2]: 0
                }
                drawn_colors = draw.split(",")
                for drawn_color in drawn_colors:
                    count, color = list(filter(None, drawn_color.split(" ")))
                    drawn[color] = int(count)
                for key in drawn:
                    if drawn[key] > max_color[key]:
                        is_valid = False
            if is_valid:
                possible_games.append(game_id)
    print(sum(possible_games))


def part2():
    print("Solution Part 2")
    powers = []
    with open("data", "r") as file:
        for line in file:
            min_colors = {
                colors[0]: 0,
                colors[1]: 0,
                colors[2]: 0
            }
            power = 1
            line = line[line.index(":") + 1:]
            line = line.replace("\n", "")
            for draw in line.split(";"):
                drawn = {
                    colors[0]: 0,
                    colors[1]: 0,
                    colors[2]: 0
                }
                drawn_colors = draw.split(",")
                for drawn_color in drawn_colors:
                    count, color = list(filter(None, drawn_color.split(" ")))
                    count = int(count)
                    drawn[color] = count
                    if count > min_colors[color]:
                        min_colors[color] = count

            for color in colors:
                power *= min_colors[color]
            powers.append(power)
        print(sum(powers))

def main():
    print("Solution for Day 2")
    part1()
    part2()





if __name__ == "__main__":
    main()

