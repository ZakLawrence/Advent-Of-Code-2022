
class Elf(object):
    def __init__(self,vals = []):
        self.vals = vals
        self.tot = sum(vals)

    def total(self):
        return self.tot


def read_file(path):
    with open(path,'r') as file:
        lines = file.readlines()
    lines = [line.strip() for line in lines]
    return lines 

def group(inputs):
    elves = []
    elf_val = []
    for i in inputs:
        if i == '':
            elf = Elf(elf_val)
            elves.append(elf.total())
            elf_val.clear()
        else:
            elf_val.append(float(i))
    return elves 


Inputs = read_file('Input.txt')
elves =  group(Inputs)
print('Max Elf',max(elves))
elves.sort(reverse=True)

print(elves[0],elves[1],elves[2])
print(sum([elves[0],elves[1],elves[2]]))
