A = 'A'
B = 'B'
C = 'C'
D = 'D'

Environment = {
    A: 'Dirty',
    B: 'Dirty',
    C: 'Dirty',
    D: 'Dirty',
    'Current': A
}

def REFLEX_VACUUM_AGENT(loc_st):
    if loc_st[1] == 'Dirty':
        return 'Suck'
    if loc_st[0] == A:
        return 'Right'
    if loc_st[0] == B:
        return 'Down'
    if loc_st[0] == D:
        return 'Left'
    if loc_st[0] == C:
        return 'Up'


def Sensors():
    location = Environment['Current']
    return (location, Environment[location])

def Actuators(action):
    location = Environment['Current']
    if action == 'Suck':
        Environment[location] = 'Clean'
    elif action == 'Right' and location == A:
        Environment['Current'] = B
    elif action == 'Down' and location == B:
        Environment['Current'] = D
    elif action == 'Left' and location == D:
        Environment['Current'] = C
    elif action == 'Up' and location == C:
        Environment['Current'] = A

def run(n):
    print('     Current             New')
    print('location    status   action location    status')
    for i in range(1, n):
        (location, status) = Sensors()
        print("{:12s}{:8s}".format(location, status) , end=' ')
        action = REFLEX_VACUUM_AGENT(Sensors())
        Actuators(action)
        (location, status) = Sensors()
        print("{:8s}{:12s}{:8s}".format(action, location, status))

run(20)