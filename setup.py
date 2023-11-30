'''
Notes:
    w
   w
'''
import os


for i in range(1, 25):
    folder_name = f'aoc-2023-day-{i:02}'
    os.makedirs(folder_name)

    file_name = f'{folder_name}/day-{i}.py'
    with open(file_name, 'w') as file:
        file.write('"""\n')
        file.write(f'Advent of Code 2023 - Day {i}\n\n')
        file.write(f'Start: {i}. Dec 2023 - \n')
        file.write(f'Finish: {i}. Dec 2023 - \n')
        file.write('Notes:\n')
        file.write('    \n')
        file.write('"""\n\n')
        file.write('def main():\n')
        file.write(f'    print("Solution for Day {i}")\n\n\n')

        file.write('if __name__ == "__main__":\n')
        file.write('    main()\n\n')
