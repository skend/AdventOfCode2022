from enum import Enum


class Hand(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


def get_lines():
    lines = []
    with open('input.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()

    lines = [line.strip().split(' ') for line in lines]
    return lines


def translate(letter):
    if letter == 'A' or letter == 'X':
        return Hand.ROCK
    elif letter == 'B' or letter == 'Y':
        return Hand.PAPER
    else:
        return Hand.SCISSORS


def go(a, b):
    if a == b:
        return 3
    elif (a == Hand.ROCK and b == Hand.SCISSORS) or \
         (a == Hand.SCISSORS and b == Hand.PAPER) or \
         (a == Hand.PAPER and b == Hand.ROCK):
         return 0
    else:
        return 6


def part_one():
    lines = get_lines()
    total = 0

    for line in lines:
        opponent = translate(line[0])
        me = translate(line[1])

        total += go(opponent, me) + int(me.value)

    print(total)


def find_losing(opponent):
    if opponent == Hand.ROCK:
        return Hand.SCISSORS
    elif opponent == Hand.SCISSORS:
        return Hand.PAPER
    else:
        return Hand.ROCK


def find_winning(opponent):
    if opponent == Hand.ROCK:
        return Hand.PAPER
    elif opponent == Hand.SCISSORS:
        return Hand.ROCK
    else:
        return Hand.SCISSORS


def part_two():
    lines = get_lines()
    total = 0

    for line in lines:
        opponent = translate(line[0])
        
        if (line[1] == "X"):
            me = find_losing(opponent)
        elif (line[1] == "Y"):
            me = opponent
        else:
            me = find_winning(opponent)

        total += go(opponent, me) + int(me.value)

    print(total)


part_two()