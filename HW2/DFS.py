'''DFS implementation of automated design of gear trains'''

gears= [11,23,31,47,59,71,83,97,109,127]
wout= [-117,77,377,-20,-2345,2]

'''class Node:
    def __init__(self,gears,wout):
        self.gears= gears
        self.wout=wout '''
cond = 'true'

'''while cond=='true':'''


class Node:
    def __init__(self,gears,wout):
        self.gears=gears
        self.wout=wout
        self.GearBox;
        self.error;








class Gear:
    def __init__(self, num_of_teeth, shaft):
        self.num_of_teeth = num_of_teeth;
        self.shaft = shaft;

class Gearbox:
    def __init__(self):
        self.gearlist = [];
        self.w_c;


class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


class DFS:

    w_in = 100;
    gears = [11, 23, 31, 47, 59, 71, 83, 97, 109, 127]
    w_out = [-117, 77, 377, -20, -2345, 2]
    s = Stack()

    


    def create_children(self,parent):





class BFS:

    def __init__(self):
        '''TO DO'''

class UCS:
    def __init__(self):
        '''TO DO'''

class A_star:
    def __init__(self):

        '''TO DO'''