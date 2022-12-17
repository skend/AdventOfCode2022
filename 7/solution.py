class ElfFile:
    def __init__(self, size, filename):
        self.size = int(size)
        self.name = filename
        
        
class ElfFolder:
    def __init__(self, parent, name):
        self.folders : list['ElfFolder'] = []
        self.files : list['ElfFile'] = []
        self.name = name
        self.parent = parent
        self.explored = False
        
        
    def add_file(self, size, filename):
        for f in self.files:
            if f.name == filename and f.size == size:
                return f
        
        new_file = ElfFile(size, filename)
        self.files.append(new_file)
        return new_file
        
        
    def add_folder(self, folder_name):
        for f in self.folders:
            if f.name == folder_name:
                return f
        
        new_dir = ElfFolder(parent=self, name=folder_name)
        self.folders.append(new_dir)
        return new_dir
    
    
    def ls(self):
        for f in self.folders:
            print(f'dir : {f.name}')
            
        for file in self.files:
            print(f'file: {file.name}')
            
            
    def get_full_path(self):
        curr_dir = self
        stack = []
        
        while curr_dir != None:
            stack.insert(0, curr_dir.name)
            curr_dir = curr_dir.parent
            
        return '/'.join(stack)
    
    
    def size_of_all_files(self):
        curr_dir = sum([file.size for file in self.files])
        
        for f in self.folders:
            curr_dir += f.size_of_all_files()
            
        return curr_dir
        
        
def get_commands(filename):
    commands = []
    with open(filename, 'r', encoding='utf-8') as f:
        commands = f.readlines()

    return [command.strip() for command in commands][1:]


def handle_cd(dir_name, current_dir):
    if dir_name == '..':
        return current_dir.parent
    else:
        return current_dir.add_folder(dir_name)


def handle_ls(output, current_dir):
    command_output = []
    for line in output:
        if line.startswith('$'):
            break
        command_output.append(line)
        
    if len(command_output) > 0:
        for out in command_output:
            if out.startswith('dir '):
                folder_name = out[len('dir '):]
                current_dir.add_folder(folder_name)
            else:
                parts = out.split(' ')
                current_dir.add_file(parts[0], parts[1])
        
        output = output[len(command_output):]
    
    return output,current_dir


def handle_command(output, current_line, current_dir):
    if current_line.startswith('$ cd '):
        current_dir = handle_cd(current_line[len('$ cd '):], current_dir)
    else:
        output,current_dir = handle_ls(output, current_dir)
    
    return output,current_dir


def list_of_dir_sizes(folders):
    all_folders = []
    while True:
        if len(folders) == 0:
            break
        
        folder = folders.pop()
        
        if folder.explored == True:
            continue
        
        dir_size = folder.size_of_all_files()
        
        folder.explored = True
        
        all_folders.append((folder.get_full_path(), dir_size))
    
        for f in folder.folders:
            if f.explored == False:
                folders.append(f)
    
    return all_folders


def sizes_of_dirs_greater_than(folders, total_sum, max_size):
    return sum([folder[1] for folder in list_of_dir_sizes(folders) if folder[1] <= max_size])


def largest_size_below_n(folders, n):
    size_of_root = folders[0].size_of_all_files()
    free_space_now = 70000000 - size_of_root
    
    eligible_dirs = [folder for folder in list_of_dir_sizes(folders) if folder[1] + free_space_now >= n]
    
    min_size = 1000000000000
    for e in eligible_dirs:
        if e[1] < min_size:
            min_size = e[1]
    
    return min_size
    
    
def create_dir_structure():
    output = get_commands('input.txt')
    root = ElfFolder(None, '<root>')
    curr_dir = root

    while True:
        if len(output) == 0:
            break
        
        current_line = output.pop(0)
        output,curr_dir = handle_command(output, current_line, curr_dir)
        
    return root


def part_one():
    root = create_dir_structure()
    total_sum = sizes_of_dirs_greater_than([root], 0, 100000)
    print(total_sum)


def part_two():
    root = create_dir_structure()
    max_size = largest_size_below_n([root], 30000000)
    print(max_size)
    
    
part_two()

# most annoying one so far