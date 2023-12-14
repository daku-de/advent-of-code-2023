"""
Advent of Code 2023 - Day 9

Start: 14. Dec 2023 - 18:55
Finish: 14. Dec 2023 - 19:08
Notes:
    
"""

histories = []

def read_data():
    with open("data", "r") as file:
        for line in file:
            line = line.replace("\n", "")
            histories.append(list(map(int, line.split(" "))))

def part1():
    print("⋆⁺₊❅⋆ ⁺₊❆⋆⋆⁺₊❅⋆ ⁺₊❆⋆")
    print("Solution Part 1")
    extrapolated_sum = 0
    for history in histories:
        #TODO recursively difference between i and i+1
        differences = [[el for el in history]]
        while True:
            new_differences = []
            last_differences = differences[len(differences)-1]
            if last_differences.count(0) == len(last_differences):
                break
            for i in range(len(last_differences)-1):
                new_differences.append(last_differences[i+1]-last_differences[i])
            differences += [new_differences]

        for i in range(1, len(differences)):
            index = len(differences) - i - 1
            next_differences = differences[index+1]
            current_differences = differences[index]
            current_differences.append(current_differences[len(current_differences)-1] + next_differences[len(next_differences)-1])
        new_history = differences[0]
        extrapolated_sum += new_history[len(new_history)-1]
    print(extrapolated_sum)



def part2():
    print("⋆⁺₊❅⋆ ⁺₊❆⋆⋆⁺₊❅⋆ ⁺₊❆⋆")
    print("Solution Part 2")
    extrapolated_sum = 0
    for history in histories:
        #TODO recursively difference between i and i+1
        differences = [[el for el in history]]
        while True:
            new_differences = []
            last_differences = differences[len(differences)-1]
            if last_differences.count(0) == len(last_differences):
                break
            for i in range(len(last_differences)-1):
                new_differences.append(last_differences[i+1]-last_differences[i])
            differences += [new_differences]

        for i in range(1, len(differences)):
            index = len(differences) - i - 1
            next_differences = differences[index+1]
            current_differences = differences[index]
            differences[index] = [current_differences[0] - next_differences[0]] + current_differences

        new_history = differences[0]
        extrapolated_sum += new_history[0]
    print(extrapolated_sum)


def main():
    print("⋆⁺₊❅⋆₊☃️ 🎄 ☃️₊❅⁺₊❆⋆")
    print("Solution for Day 9")
    read_data()
    part1()
    part2()
    print("⋆⁺₊❅⋆ ⁺₊❆⋆⋆⁺₊❅⋆ ⁺₊❆⋆")


if __name__ == "__main__":
    main()

