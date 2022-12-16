import re

# who needs classes lol

def get_input(filename):
    lines = []
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    lines = [line[0:-1] for line in lines]
    return lines


def get_starting_config(lines):
    stack = []
    count = 0
    while True:
        if len(lines[count]) == 0:
            break
        stack.append(lines[count])
        count += 1
    return stack


def populate_stack(idx, lines):
    stack = []
    for line in lines:
        letter = line[(idx * 4) + 1]
        if letter == ' ':
            continue
        else:
            stack.append(letter)
    return stack


def parse_moves(lines):
    moves = []
    
    for line in lines:
        moves.append(re.findall(r"move ([0-9]+) from ([0-9]+) to ([0-9]+)", line)[0])
    
    return moves


def apply_moves_9000(moves, stacks):
    for move in moves:
        for i in range(0, int(move[0])):
            if len(stacks[int(move[1])-1]) > 0:
                item = stacks[int(move[1])-1][0]
                stacks[int(move[1])-1] = stacks[int(move[1])-1][1:]
                stacks[int(move[2])-1].insert(0, item)
            else:
                break
            
    return stacks


def apply_moves_9001(moves, stacks):
    for move in moves:
        if int(move[0]) == 0:
            continue
        else:
            crates_to_move = min(int(move[0]), len(stacks[int(move[1])-1]))
            items = stacks[int(move[1])-1][:crates_to_move]
            stacks[int(move[1])-1] = stacks[int(move[1])-1][crates_to_move:]
            stacks[int(move[2])-1][0:0] = items  
            
    return stacks


def process_input():
    lines = get_input('input.txt')

    starting_arrangement = get_starting_config(lines)
    num_stacks = int(starting_arrangement[-1][-2])
    starting_arrangement = starting_arrangement[0:-1]
    stacks = []
    
    print("Crates at the beginning")

    for i in range(0, num_stacks):
        stacks.append(populate_stack(i, starting_arrangement))
        print(stacks[i])
        
    print("\n-----------------------------------\n")

    moves_txt = lines[len(starting_arrangement)+2:]
    moves = parse_moves(moves_txt)
    
    return moves,stacks


def part_one():
    moves,stacks = process_input()
    
    print("Crates at the end")
    
    stacks = apply_moves_9000(moves, stacks)
    
    print("\n-----------------------------------\n")
    
    for stack in stacks:
        print(stack)
        
        
def part_two():
    moves,stacks = process_input()
    
    print("Crates at the end")
    
    stacks = apply_moves_9001(moves, stacks)
    
    print("\n-----------------------------------\n")
    
    for stack in stacks:
        print(stack)


part_two()
