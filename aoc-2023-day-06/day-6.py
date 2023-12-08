"""
Advent of Code 2023 - Day 6

Start: 8. Dec 2023 - 17:05
Finish: 8. Dec 2023 - 17:19
Notes:
    Of course could actually calculate the ranges by just solving the quadratic equation but
    because the input is very small it doesn't really matter. The runtime is still low enough
    and my head is hurting so I cba
"""


durations = []
records = []
def read_data():
    global durations, records
    with open("data", "r") as file:
        durations = list(map(int, filter(None, file.readline().replace("\n", "").split(":")[1].split(" "))))
        records = list(map(int, filter(None, file.readline().replace("\n", "").split(":")[1].split(" "))))


def part1():
    print("⋆⁺₊❅⋆ ⁺₊❆⋆⋆⁺₊❅⋆ ⁺₊❆⋆")
    print("Solution Part 1")

    record_beating_ways = 1
    for race in range(len(durations)):
        ways_to_win = 0
        duration = durations[race]
        record = records[race]
        for button_time in range(duration):
            distance = (duration-button_time) * button_time
            if distance > record:
                ways_to_win += 1
        record_beating_ways *= ways_to_win
    print(record_beating_ways)

def part2():
    print("⋆⁺₊❅⋆ ⁺₊❆⋆⋆⁺₊❅⋆ ⁺₊❆⋆")
    print("Solution Part 2")
    duration = int("".join(list(map(lambda x: "%d" % x, durations))))
    record = int("".join(list(map(lambda x: "%d" % x, records))))
    ways_to_win = 0
    for button_time in range(duration):
        distance = (duration - button_time) * button_time
        if distance > record:
            ways_to_win += 1
    print(ways_to_win)


def main():
    print("⋆⁺₊❅⋆₊☃️ 🎄 ☃️₊❅⁺₊❆⋆")
    print("Solution for Day 6")
    read_data()
    part1()
    part2()
    print("⋆⁺₊❅⋆ ⁺₊❆⋆⋆⁺₊❅⋆ ⁺₊❆⋆")


if __name__ == "__main__":
    main()

