'''BFS implementation of automated design of gear trains'''


class Node:                             #class for defining node
    def __init__(self,gear):
        self.win=100.0;
        self.lastgear = gear
        self.gears = [];
        self.gear_values= [];
        self.wc = 100.0;

    def append_gear(self):              #appends the last gear to the arra
        self.gears.append(self.lastgear)

    def append_gear_value(self):        #appends the last gear value to the array
        self.gear_values.append(self.lastgear.num_of_teeth)

    def calc_wc(self):                  #calculating wc
        i =len(self.gears)
        if(i==1):                       # condition check for evaluating wc. For just one gear, wc becomes win
            self.wc=self.win
        elif(i%2==0):                   # condition check for evaluating wc. For even gears wc becomes negative
            self.wc = 1.0;
            for j in range(0, i):
                if j%2==0:
                    self.wc = self.wc * self.gears[j].num_of_teeth;
                else:
                    self.wc = self.wc / self.gears[j].num_of_teeth;
            self.wc = -1 * self.wc * self.win;
        else:                           # condition check for evaluating wc. For odd gears wc remains positive
            self.wc = 1.0;
            for j in range(0, i-1):
                if j%2==0:
                    self.wc = self.wc * self.gears[j].num_of_teeth;
                else:
                    self.wc = self.wc / self.gears[j].num_of_teeth;
            self.wc = self.wc * self.win;

class Gear:                             #class for defining number of teeth in gear
    def __init__(self, num_of_teeth):
        self.num_of_teeth = num_of_teeth;

class Queue:                            #class for creating queue
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

class BFS:                              #class for BFS impelementation

    def __init__(self, win, wout, gear_values):
        self.win = win;
        self.wout = wout;
        self.gear_values = gear_values;
        self.s = Queue()
        self.isOptimum = False;


    def search(self):                   #defining how to search through the tree
        self.initialize()

        #isOptimum = False;
        while not ((self.s.isEmpty()) or (self.isOptimum)):
            node = self.s.dequeue();
            self.isOptimum = self.evaluation(node);
            if self.isOptimum:           #if goal found then print the gear combination
                print ('Gear combination is: ')
                for gear in node.gears:
                    print(gear.num_of_teeth)
            elif not(len(node.gears) > 9 or self.isOptimum) :   #condition check for depth of tree
                children = self.create_children(node)
                for child in children:
                    self.s.enqueue(child);

    def initialize(self):

        #self.s = Stack();
        for value in self.gear_values:
            gear = Gear(value);
            node = Node(gear);
            node.append_gear();
            node.append_gear_value()
            self.s.enqueue(node);



    def evaluation(self, Node):             #evalauating goal
        #isOptimum = False;
        error = abs(self.wout - Node.wc)/abs(self.wout - self.win) * 100;
        if error <= 2.5:
            self.isOptimum = True;
            print'error is: ',error
        return self.isOptimum;


    def create_children(self,parent):        #creating children nodes and appending values as (kind of) gearbox to each node
        child_nodes = []
        compatible_values = self.find_compatible(parent)
        for value in compatible_values:
            gear = Gear(value)
            node = Node(gear);
            for g in parent.gears:
                node.gears.append(g)
            node.append_gear();
            node.append_gear_value()
            child_nodes.append(node);
            node.calc_wc();
        return child_nodes;



    def find_compatible(self, Node):        #find compatible children values
        remaining_gear_values = [x for x in self.gear_values if x is not Node.lastgear.num_of_teeth];
        if len(Node.gears)%2 !=0:           # check condtiion for mating
            compatible_values = [];
            for value in remaining_gear_values:
                if abs(value - Node.lastgear.num_of_teeth) <= 30:
                    compatible_values.append(value)
        else:                               #check condition for pairing(on same shaft)
            compatible_values = [x for x in self.gear_values if x is not Node.lastgear.num_of_teeth];

        return compatible_values;


def Main():

    w_in = 100;
    gear_values = [11, 23, 31, 47, 59, 71, 83, 97, 109, 127];
    w_out = [-117, 77, 377, -20,-2345,2]


    for value in w_out:
        print 'w_in is: ',w_in
        print 'wout is: ',value
        Search_method = BFS(w_in, value, gear_values);
        Search_method.search();
        print;

Main();
