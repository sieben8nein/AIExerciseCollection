A = 'A'
B = 'B'
Clean = 'Clean'
Dirty = 'Dirty'

INITIAL_STATE = (A, 'Dirty', 'Dirty')
GOAL_STATE = (A, 'Clean', 'Clean')
STATE_SPACE = {(A, Dirty, Dirty): [(A, Dirty, Dirty), (A, Clean, Dirty), (B, Dirty, Dirty)],
               (B, Dirty, Dirty): [(A, Dirty, Dirty), (B, Dirty, Dirty), (B, Dirty, Clean)],
               (B, Dirty, Clean): [(B, Dirty, Clean), (A, Dirty, Clean)],
               (A, Dirty, Clean): [(A, Dirty, Clean), (A, Clean, Clean), (B, Dirty, Clean)],
               (A, Clean, Dirty): [(A, Clean, Dirty), (B, Clean, Dirty)],
               (B, Clean, Dirty): [(B, Clean, Dirty), (A, Clean, Dirty), (B, Clean, Clean)],
               (B, Clean, Clean): [(B, Clean, Clean), (A, Clean, Clean)]}

class Node:  # Node has only PARENT_NODE, STATE, DEPTH
    def __init__(self, state, parent=None):
        self.STATE = state
        self.PARENT_NODE = parent

        if parent != None:
            self.pathcost = 1 + parent.pathcost
        else:
            self.pathcost = 0

    def path(self):  # Create a list of nodes from the root to this node.
        current_node = self
        path = [self]
        while current_node.PARENT_NODE:  # while current node has parent
            current_node = current_node.PARENT_NODE  # make parent the current node
            path.append(current_node)   # add current node to path
        return path

    def display(self):
        print(self)

    def __repr__(self):
        return 'State: ' + str(self.STATE) + ' - cost: ' + str(self.pathcost)# + ' parent: ' + str(self.PARENT_NODE)

'''
Search the tree for the goal state and return path from initial state to goal state
'''
def A_STAR_SEARCH():
    fringe = {}
    explored_nodes = []
    initial_node = Node(INITIAL_STATE, None)
    explored_nodes.append(initial_node)
    fringe[initial_node] = initial_node.pathcost
    while len(fringe) > 0:
        c = REMOVE_FIRST(fringe)
        #print(c)
        explored_nodes.append(c)
        if c.STATE == GOAL_STATE:
            return [c.path(), explored_nodes]
        INSERT_ALL(EXPAND(c), fringe)
    return ["not found"]

'''
Expands node and gets the successors (children) of that node.
Return list of the successor nodes.
'''
def EXPAND(node):
    successors = {}
    children = successor_fn(node.STATE)
    for child in children:
        s = Node(child, node)  # create node for each in state list
        successors = INSERT(s, successors)
    return successors

'''
Insert node in to the queue (fringe).
'''
def INSERT(node, queue):
    queue[node] = node.pathcost
    return queue


'''
Insert list of nodes into the fringe
'''
def INSERT_ALL(list, queue):
    for child in list:
        queue[child] = child.pathcost
    return queue



'''
Removes and returns the first element from fringe
'''
def REMOVE_FIRST(queue):
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
    information = A_STAR_SEARCH()
    path = information[0]
    print('Solution path:')
    for node in reversed(path):
        node.display()
    print('total cost:', path[0].pathcost)
    print('explored nodes:', len(information[1]))



if __name__ == '__main__':
    run()
