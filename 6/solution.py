def get_input(filename):
    text = ''
    with open(filename, 'r', encoding='utf-8') as f:
        text = f.read()

    return text.strip()


def find_unique_signals(buf, num_unique):
    idx = num_unique - 1

    while True:
        check = buf[idx-num_unique+1:idx+1]
        
        unique = [item[1] for item in list(enumerate(check))]
        
        if len(set(unique)) == num_unique:
            return idx+1
        
        if len(buf) > idx + 1:
            idx += 1
        else:
            break


def part_one():
    buf = get_input('input.txt')
    print(find_unique_signals(buf, num_unique=4))
    
    
def part_two():
    buf = get_input('input.txt')
    print(find_unique_signals(buf, num_unique=14))
    
    
part_two()

# easiest so far?