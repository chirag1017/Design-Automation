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
    def __init__(self,gear):
        self.wout=wout
        self.GearBox;
        self.error;
        self.lastgear = gear;
        self.gears = [];


    def append_gear(self):
        self.gears.append(self.lastgear)







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

    def __init__(self, w_in, w_out, gear_values):
        self.w_in = w_in;
        self.w_out = w_out;
        self.gear_values = gear_values;
        self.s;


    def search(self):
        self.initialize()

        isOptimum = False;
        while (self.s.size() != 0) and ~isOptimum:
            node = self.s.pop();
            isOptimum = self.evaluation(node);







    def initialize(self):
        self.s = Stack();
        for value in self.gear_values:
            gear = Gear(value);
            node = Node(gear);
            node.append_gear();
            self.s.push(node);



    def evaluation(self, Node):
        isOptimum = False;
        if Node.error <= 2.5:
            isOptimum = True;
        return isOptimum;








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




def Main():

    w_in = 100;
    gear_values = [11, 23, 31, 47, 59, 71, 83, 97, 109, 127];
    w_out = [-117, 77, 377, -20, -2345, 2]

    Search_method = DFS(w_in, w_out, gear_values);









Main();