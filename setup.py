import os


for i in range(1, 26):
    folder_name = f'aoc-2023-day-{i:02}'
    os.makedirs(folder_name)

    file_name = f'{folder_name}/day-{i}.py'
    with open(file_name, 'w', encoding='utf-8') as file:
        file.write('"""\n')
        file.write(f'Advent of Code 2023 - Day {i}\n\n')
        file.write(f'Start: {i}. Dec 2023 - \n')
        file.write(f'Finish: {i}. Dec 2023 - \n')
        file.write('Notes:\n')
        file.write('    \n')
        file.write('"""\n\n\n')
        file.write('def read_data():\n')
        file.write('    with open("data", "r") as file:\n')
        file.write('        for line in file:\n')
        file.write('            pass\n\n\n')
        file.write('def part1():\n')
        file.write('    print("⋆⁺₊❅⋆ ⁺₊❆⋆⋆⁺₊❅⋆ ⁺₊❆⋆")\n')
        file.write('    print("Solution Part 1")\n\n\n')
        file.write('def part2():\n')
        file.write('    print("⋆⁺₊❅⋆ ⁺₊❆⋆⋆⁺₊❅⋆ ⁺₊❆⋆")\n')
        file.write('    print("Solution Part 2")\n\n\n')
        file.write('def main():\n')
        file.write('    print("⋆⁺₊❅⋆₊☃️ 🎄 ☃️₊❅⁺₊❆⋆")\n')
        file.write(f'    print("Solution for Day {i}")\n')
        file.write('    part1()\n')
        file.write('    part2()\n')
        file.write('    print("⋆⁺₊❅⋆ ⁺₊❆⋆⋆⁺₊❅⋆ ⁺₊❆⋆")\n\n\n')

        file.write('if __name__ == "__main__":\n')
        file.write('    main()\n\n')

    with open(f'{folder_name}/data', 'w') as file:
        file.write('')
