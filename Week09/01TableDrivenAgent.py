A = 'A'
B = 'B'
percepts = []
table = {
    ((A, 'Clean'), ): 'Right',
    ((A, 'Dirty'), ): 'Suck',
    ((B, 'Clean'), ): 'Left',
    ((B, 'Dirty'), ): 'Suck',

    ((A, 'Clean'), (A, 'Clean')): 'Right',
    ((A, 'Clean'), (A, 'Dirty')): 'Suck',

    ((A, 'Clean'), (A, 'Clean'), (A, 'Clean') ): 'Right',
    ((A, 'Clean'), (A, 'Clean'), (A, 'Dirty'),): 'Suck',
    ((A, 'Clean'), (A, 'Dirty'), (B, 'Clean'), ): 'Left',
}

def LOOKUP(percepts, table):
    action = table.get(tuple(percepts))
    return action

def TABLE_DRIVEN_AGENT(percept):
    percepts.append(percept)
    action = LOOKUP(percepts, table)
    return action

def run():
    print('Action\tPercepts')
    print(TABLE_DRIVEN_AGENT((A, 'Clean')), '\t', percepts)
    print(TABLE_DRIVEN_AGENT((A, 'Dirty')), '\t', percepts)
    print(TABLE_DRIVEN_AGENT((B, 'Clean')), '\t', percepts)
    print(TABLE_DRIVEN_AGENT((B, 'Clean')))

run()

'''
Question 1:
..
Question 2:
    the result is none, because it doesnt know what to with with this percept, since it is not in the table

Question 3:
    4, the initial 4 in the table

Question 4:
    4 to the power of T

'''