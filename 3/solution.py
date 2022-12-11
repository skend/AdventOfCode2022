def get_bag_contents_by_compartment():
    lines = []
    with open('input.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()

    lines = [line.strip() for line in lines]
    lines = [[line[:int(len(line)/2)], line[int(len(line)/2):]] for line in lines]
    return lines


# yuck!
def get_bag_contents():
    lines = []
    with open('input.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()

    combined_contents = []
    curr = []
    num = 0

    for line in lines:
        num += 1

        curr.append(line.strip())

        if num == 3:
            combined_contents.append(curr)
            curr = []
            num = 0
    
    return combined_contents


def item_to_priority(item):
    item = ord(item)
    if item >= ord('a') and item <= ord('z'):
        return item - 96
    else:
        return item - 64 + 26


def find_common_compartment_items(first, second):
    return list(set(first).intersection(second))


def find_common_bag_items(bag_group):
    return list(set(bag_group[0]).intersection(bag_group[1]).intersection(bag_group[2]))[0]


def part_one():
    bag = get_bag_contents_by_compartment()

    total = 0
    common_items = []

    for compartment in bag:
        items = find_common_compartment_items(compartment[0], compartment[1])
        common_items.extend(items)
    
    for common in common_items:
        total += item_to_priority(common)

    print(total)


def part_two():
    bag_groups = get_bag_contents()
    priorities = []
    
    for gr in bag_groups:
        badge = find_common_bag_items(gr)
        priorities.append(item_to_priority(badge))

    print(sum(priorities))


part_two()
