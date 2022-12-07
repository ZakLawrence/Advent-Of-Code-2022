class file_node(object):
    def __init__(self,name,size = 0,parent=None) -> None:
        self.name = name
        self.size = size
        self.parent = parent
        self.children: list[file_node] = []
    
    def __str__(self):
        return f'{self.name} ({self.size})'

    def __name__(self):
        return self.name

    def __size__(self):
        return self.size
    
    def __parent__(self):
        return self.parent   

class tree(object):
    def __init__(self) -> None:
        self.root: file_node = file_node("/",0,None)
        self.pwd: file_node = self.root
        self.dirs: list[file_node] = []
    
    def __pwd__(self):
        return self.pwd
    
    def set_pwd(self,dir):
        self.pwd = dir
    
    def add_node(self,name,size=0):
        node = file_node(name, size, self.pwd)
        self.pwd.children.append(node)
        if size == 0: #its a file 
            self.dirs.append(node)
            self.pwd = node
    
    def go_up(self):
        self.pwd = self.pwd.parent
    
    def calculate_size(self):
        for child in self.root.children:
            self.root.size += self.update_child_size(child)

    def update_child_size(self,node):
        for child in node.children:
            node.size += self.update_child_size(child)
        return node.size

def split_num(s):
    return ''.join([c for c in s if not c.isdigit()]),''.join([c for c in s if c.isdigit()])

def parse_commands(fpath):
    file_tree = tree()
    for command in open(fpath).read().split("$"):
        command = command.replace(" ","").replace("\n"," ")
        if ("cd" in command):
            dir = command.replace("cd","").strip()
            if dir == "..":
                file_tree.go_up()
            else:
                file_tree.add_node(dir)
        if ("ls" in command):
            files =  [split_num(f) for f in  (command.replace("ls","").replace("dir","").strip()).split(" ")]
            for file in files: 
                if file[1]: 
                    file_tree.add_node(name=file[0],size=float(file[1]))
    file_tree.calculate_size()
    return file_tree

def dir_to_delete(file_tree,file_system_size,space_needed):
    unused_space = file_system_size - file_tree.root.size
    space_to_free = space_needed-unused_space
    print(min([file.size for file in file_tree.dirs if file.size >= space_to_free]))

file_tree = parse_commands("Inputs.txt")
print(sum([file.size for file in file_tree.dirs if file.size < 100000]))
dir_to_delete(file_tree,70000000,30000000)