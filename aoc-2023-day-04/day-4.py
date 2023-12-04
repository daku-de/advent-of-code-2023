"""
Advent of Code 2023 - Day 4

Start: 4. Dec 2023 - 21:42
Finish: 4. Dec 2023 - 22:10
Notes:
    
"""
import math


def part1():
    print("Solution Part 1")
    with open("data", "r") as file:
        worth = 0
        for line in file:
            winners = 0

            line = line.replace("\n", "")
            line = line.split(":")[1]
            winning = list(map(int, filter(None, line.split("|")[0].split(" "))))
            have = list(map(int, filter(None, line.split("|")[1].split(" "))))

            for number in have:
                if number in winning:
                    winners += 1

            score = int(math.pow(2, winners-1))
            worth += score
        print(worth)


def part2():
    print("Solution Part 2")
    scratchcards = []
    with open("data", "r") as file:
        for line in file:
            scratchcard = {
                "count": 1,
                "winning": [],
                "have": [],
                "hits": 0
            }
            line = line.replace("\n", "")
            line = line.split(":")[1]
            scratchcard["winning"] = list(map(int, filter(None, line.split("|")[0].split(" "))))
            scratchcard["have"] = list(map(int, filter(None, line.split("|")[1].split(" "))))

            for number in scratchcard["have"]:
                if number in scratchcard["winning"]:
                    scratchcard["hits"] += 1
            scratchcards.append(scratchcard)

    for index, scratchcard in enumerate(scratchcards):
        for j in range(scratchcard["hits"]):
            j += 1
            if j < len(scratchcards):
                scratchcards[index+j]["count"] += scratchcard["count"]

    total = 0
    for scratchcard in scratchcards:
        total += scratchcard["count"]
    print(total)


def main():
    print("Solution for Day 4")
    part1()
    part2()


if __name__ == "__main__":
    main()

