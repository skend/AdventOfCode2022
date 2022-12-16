def get_input():
    lines = []
    with open('input.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()

    lines = [line.strip().split(',') for line in lines]
    lines = [[[int(line[0].split('-')[0]), int(line[0].split('-')[1])], [int(line[1].split('-')[0]), int(line[1].split('-')[1])]] for line in lines]
    return lines


def part_one():
    lines = get_input()
    full_overlaps = 0
    for line in lines:
        if line[1][0] >= line[0][0] and line[1][1] <= line[0][1]:
            full_overlaps += 1
            print(f'1: {line}')
        elif line[0][0] >= line[1][0] and line[0][1] <= line[1][1]:
            full_overlaps += 1
            print(f'2: {line}')
    
    print(full_overlaps)


def overlap_count(line):
    range0 = range(line[0][0], line[0][1]+1)
    range1 = range(line[1][0], line[1][1]+1)

    return len(set(range0).intersection(range1))


def part_two():
    lines = get_input()
    overlaps = 0
    for line in lines:
        overlaps += overlap_count(line) > 0

    print(overlaps)


part_two()