class Stack(object):
    def __init__(self,stack_no,stack_pos) -> None:
        self.number = stack_no
        self.position = stack_pos
        self.crates = []
    
    def get_stack_number(self):
        return self.number
    
    def get_stack_position(self):
        return self.position
    
    def append_crate(self,crate):
        self.crates.append(crate)
    
    def prepend_crate(self,crate):
        self.crates.insert(0,crate)
    
    def remove_element(self,indx):
        self.crates.pop(indx)

    def get_crates(self):
        return self.crates

def read_file(fpath):
    file = open(fpath)
    return file.readlines()

def read_moves(fpath):
    moves = []
    for line in read_file(fpath):
        _,move,_,orig,_,dest = line.split(' ')
        moves.append({"move":int(move.strip()),"orig":int(orig.strip()),"dest":int(dest.strip())})
    return moves

def read_stacks(fpath):
    stacks = []
    for index,line in enumerate(reversed(read_file(fpath))):
        if index == 0: 
            stack_nos = [int(l) for l in line.split(' ') if l]
            stack_poss = [int(line.rfind(str(l))) for l in stack_nos]
            for num,pos in zip(stack_nos,stack_poss):
                stacks.append(Stack(num,pos))
        else:
            crates = [c.strip().replace('[','').replace(']','') for c in line.split(' ') if c.strip()]
            for stack in stacks:
                for crate in crates:
                    #print(line.rfind(crate))
                    if line.rfind(crate,stack.position,stack.position+1) != -1:# == stack.position:
                        stack.append_crate(crate)
                        break
    return stacks

def make_move(stack1,stack2,nmove):
    for i in range(0,nmove):
        c1 = stack1.get_crates()[-1]
        stack2.append_crate(c1)
        stack1.remove_element(-1)
    return stack1,stack2

def make_move_v2(stack1,stack2,nmove):
    c1 = stack1.get_crates()[-nmove:]
    for c in c1:
        stack2.append_crate(c)
    for i in range(nmove):
        stack1.remove_element(-1)
    return stack1,stack2



def apply_moves(stacks,moves):
    for move in moves:
        #print(move)
        orig = stacks[move["orig"]-1] 
        dest = stacks[move["dest"]-1]
        #print(orig.get_crates(),dest.get_crates())
        stacks[move["orig"]-1],stacks[move["dest"]-1] = make_move_v2(orig,dest,move["move"])
    return stacks

stacks = read_stacks("Crates.txt")
for stack in stacks:
    print(stack.get_crates()) 

stacks = apply_moves(read_stacks("Crates.txt"),read_moves("Moves.txt"))

print(''.join([stack.get_crates()[-1] for stack in stacks]))

