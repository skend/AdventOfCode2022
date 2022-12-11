def get_lines():
    with open('input.txt', 'r', encoding='utf-8') as f:
        return f.readlines()

lines = get_lines()

def part_one():
    most_cals = -1
    curr_cals = 0

    for line in lines:
        line = line.strip()
        
        if len(line) == 0:
            if curr_cals > most_cals:
                most_cals = curr_cals
            curr_cals = 0
        else:
            curr_cals += int(line)

    print(most_cals)

def part_two():
    curr_cals = 0
    elves = []

    for line in lines:
        line = line.strip()
        
        if len(line) == 0:
            elves.append(curr_cals)
            curr_cals = 0
        else:
            curr_cals += int(line)

    elves = sorted(elves, reverse=True)
    print(sum(elves[:3]))


part_two()