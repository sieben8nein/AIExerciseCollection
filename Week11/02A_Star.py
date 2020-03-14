A = 'A'
B = 'B'
C = 'C'
D = 'D'
E = 'E'
F = 'F'
G = 'G'
H = 'H'
I = 'I'
J = 'J'
K = 'K'
L = 'L'
# (position, distance to goal, distance from last node)
INITIAL_STATE = (A, 6, 0)
STATE_SPACE = {(A, 6, 0): [ (B, 5, 1), (C, 5, 2), (D, 2, 4)],
               (B, 5, 1): [(F, 5, 5), (E, 4, 4)],
               (C, 5, 2): [(E, 4, 1)],
               (D, 2, 4): [(H, 1, 1), (I, 2, 4), (J, 1, 2)],
               (E, 4, 4): [(G, 4, 2), (H, 1, 3)],
               (E, 4, 1): [(G, 4, 2), (H, 1, 3)],
               (F, 5, 5): [(G, 4, 1)],
               (G, 4, 1): [(K, 0, 6)],
               (G, 4, 2): [(K, 0, 6)],
               (H, 1, 3): [(K, 0, 6), (L, 0, 5)],
               (H, 1, 1): [(K, 0, 6), (L, 0, 5)],
               (I, 2, 4): [(L, 0, 3)],
               (J, 1, 2): [(J, 1, 2)]}

class Node:  # Node has only PARENT_NODE, STATE, DEPTH
    def __init__(self, state, parent):
        self.state = state
        self.parent = parent

        if parent != None:
            self.pathcost = state[2] + parent.pathcost
            self.heuristic = state[1] + self.pathcost

        else:
            self.pathcost = state[2]
            self.heuristic = state[1] + self.pathcost

    def path(self):  # Create a list of nodes from the root to this node.
        current_node = self
        path = [self]
        while current_node.parent != None:  # while current node has parent
            current_node = current_node.parent  # make parent the current node
            path.append(current_node)  # add current node to path
        return path

    def display(self):
        print(self)

    def __repr__(self):
        return 'name: ' + str(self.state[0]) + ' - Heu: ' + str(self.heuristic)

'''
Search the tree for the goal state and return path from initial state to goal state
'''
def GREEDY_SEARCH(state):
    fringe = {}
    initial_node = Node(INITIAL_STATE, None)
    fringe[initial_node] = initial_node.heuristic
    while len(fringe) > 0:
        c = REMOVE_FIRST(fringe)
        if c.state[1] == 0:
            return c.path()
        INSERT_ALL(EXPAND(c), fringe)
    return ["not found"]

'''
Expands node and gets the successors (children) of that node.
Return list of the successor nodes.
'''
def EXPAND(node):
    successors = {}
    children = successor_fn(node.state)
    for child in children:
        s = Node(child, node)  # create node for each in state list
        successors = INSERT(s, successors)
    return successors

'''
Insert node in to the queue (fringe).
'''

def INSERT(node, queue):
    queue[node] = node.heuristic
    return queue

'''
Insert list of nodes into the fringe
'''
def INSERT_ALL(list, queue):
    for child in list:
        key = child
        heur = child.heuristic
        queue[child] = child.heuristic
    return queue

'''
Removes and returns the first element from fringe
'''
def REMOVE_FIRST(queue):
    #x = sorted(queue.items(), key = lambda item: item[0])[0]
    x = sorted(queue.items(), key=lambda item: item[1])[0]
    try:
        del queue[x[0]]
    except KeyError:
        print("Key not found")
    return x[0]

'''
Successor function, mapping the nodes to its successors
'''
def successor_fn(state):  # Lookup list of successor states
    return STATE_SPACE[state]  # successor_fn( 'C' ) returns ['F', 'G']

'''
Run tree search and display the nodes in the path to goal node
'''
def run():
    path = GREEDY_SEARCH(INITIAL_STATE)
    print('Solution path:')
    for node in reversed(path):
        node.display()

if __name__ == '__main__':
    run()
