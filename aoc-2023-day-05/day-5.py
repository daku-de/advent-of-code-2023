"""
Advent of Code 2023 - Day 5

Start: 5. Dec 2023 - 18:20
Finish: 8. Dec 2023 - 16:55
Notes:
    Couldn't solve part 2 immediately and took a break from aoc
"""


seeds = []
mappings = []
def read_data():
    global seeds, mappings
    with open("data", "r") as file:
        line = file.readline()
        line = line.replace("\n", "")
        seeds = list(map(int, filter(None, line.split(":")[1].split(" "))))

        while True:
            line = file.readline()
            if line == "":
                break
            if ":" in line:
                mapping = []
                line = file.readline()
                line = line.replace("\n", "")
                while line != "":
                    dest, src, range = list(map(int, filter(None, line.split(" "))))
                    mapping.append((dest, src, range))
                    line = file.readline()
                    line = line.replace("\n", "")
                mappings.append(mapping)


def part1():
    print("⋆⁺₊❅⋆ ⁺₊❆⋆⋆⁺₊❅⋆ ⁺₊❆⋆")
    print("Solution Part 1")
    paths = []
    for seed in seeds:
        path = [seed]
        current = seed
        for mapping in mappings:
            for (dst, src, rng) in mapping:
                if src <= current < src+rng:
                    current = current - src + dst
                    break
            path.append(current)
        paths.append(path)
    min_location = 0
    for path in paths:
        location = path[len(path)-1]
        if min_location == 0 or location < min_location:
            min_location = location
    print(min_location)


def part2():
    print("⋆⁺₊❅⋆ ⁺₊❆⋆⋆⁺₊❅⋆ ⁺₊❆⋆")
    print("Solution Part 2")

    seed_ranges = []
    for i in range(0, len(seeds), 2):
        seed_ranges.append((seeds[i], seeds[i]+seeds[i+1]))

    new_seed_ranges = []
    for mapping in mappings:
        new_seed_ranges = []
        while len(seed_ranges) > 0:
            seed_range = seed_ranges.pop()
            if seed_range == (0, 0):
                continue

            altered = False
            for (dst, src, rng) in mapping:
                if src <= seed_range[0] < src+rng:
                    if src+rng <= seed_range[1]:
                        new_seed_ranges.append((dst + seed_range[0] - src, dst+rng))
                        seed_ranges.append((src+rng, seed_range[1]))
                    else:
                        new_seed_ranges.append((dst + seed_range[0] - src, dst + seed_range[1] - src))
                    altered = True
                    break
                elif seed_range[0] < src < seed_range[1]:
                    seed_ranges.append((seed_range[0], src))
                    if src+rng <= seed_range[1]:
                        new_seed_ranges.append((dst, dst + seed_range[1] - src))
                        seed_ranges.append((src+rng, seed_range[1]))
                    else:
                        new_seed_ranges.append((seed_range[0], src))
                    altered = True
                    break
            if not altered:
                new_seed_ranges.append(seed_range)
        seed_ranges = new_seed_ranges

    print(min(map(lambda x: x[0], new_seed_ranges)))

def main():
    print("⋆⁺₊❅⋆₊☃️ 🎄 ☃️₊❅⁺₊❆⋆")
    print("Solution for Day 5")
    read_data()
    #part1()
    part2()
    print("⋆⁺₊❅⋆ ⁺₊❆⋆⋆⁺₊❅⋆ ⁺₊❆⋆")


if __name__ == "__main__":
    main()

