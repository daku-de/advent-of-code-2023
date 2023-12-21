"""
Advent of Code 2023 - Day 8

Start: 12. Dec 2023 - 09:15
Finish: 21. Dec 2023 - 19:00
Notes:
    Really didn't know how to do 2nd part. So I looked how many steps it takes to
    the next node ending with Z and printing the node.
    I noticed two things:
        - it's always the same node
        - the steps needed to the next z node are always the same
    After I noticed these two things I got to the solution within minutes.
    I don't know why these two things are true though. Does it necessarily always loop?
"""

paths = {}
instructions = []

def read_data():
    global instructions
    with open("data", "r") as file:
        instructions = list(file.readline().replace("\n", ""))
        file.readline()
        for line in file:
            line = line.replace("\n", "").replace("(", "").replace(")", "")
            from_node = line.split(" = ")[0]
            left, right = line.split(" = ")[1].split(", ")
            paths[from_node] = {
                "L": left,
                "R": right
            }


def get_primes(n):
    primes = []
    i = 2
    while n != 1:
        while n%i == 0:
            n = n/i
            primes.append(i)
        i += 1
    return primes


def part1():
    print("⋆⁺₊❅⋆ ⁺₊❆⋆⋆⁺₊❅⋆ ⁺₊❆⋆")
    print("Solution Part 1")

    current = "AAA"
    steps = 0
    i = 0
    while True:
        instruction = instructions[i]
        current = paths[current][instruction]
        steps += 1
        if current == "ZZZ":
            break
        i = (i+1) % len(instructions)
    print(steps)

def part2():
    print("⋆⁺₊❅⋆ ⁺₊❆⋆⋆⁺₊❅⋆ ⁺₊❆⋆")
    print("Solution Part 2")

    goal_nodes = []
    for key in paths:
        if key[2] == "A":
            goal_nodes.append(key)

    steps_to_end = []
    for goal in goal_nodes:
        current = goal
        steps = 0
        i = 0
        while True:
            instruction = instructions[i]
            steps += 1
            current = paths[current][instruction]
            i = (i + 1) % len(instructions)
            if current[2] == "Z":
                steps_to_end.append(steps)
                break

    prime_lists = []
    for step in steps_to_end:
        prime_lists.append(get_primes(step))

    for prime in prime_lists[0]:
        remove = True
        for prime_list in prime_lists:
            if prime not in prime_list:
                remove = False
        if remove:
            for prime_list in prime_lists[1:]:
                prime_list.remove(prime)

    total_steps = 1
    for prime_list in prime_lists:
        for prime in prime_list:
            total_steps *= prime

    print(total_steps)




def main():
    print("⋆⁺₊❅⋆₊☃️ 🎄 ☃️₊❅⁺₊❆⋆")
    print("Solution for Day 8")
    read_data()
    part1()
    part2()
    print("⋆⁺₊❅⋆ ⁺₊❆⋆⋆⁺₊❅⋆ ⁺₊❆⋆")


if __name__ == "__main__":
    main()

