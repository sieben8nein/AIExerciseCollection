import math
from collections import Counter


def minmax_decision(state):
    def max_value(state):
        if is_terminal(state):
            return utility_of(state)
        v = -infinity
        for (a, s) in successors_of(state):
            v = max(v, min_value(s))
        print('V: ' + str(v))
        return v

    def min_value(state):
        if is_terminal(state):
            return utility_of(state)
        v = infinity
        for (a, s) in successors_of(state):
            v = min(v, max_value(s))
        return v

    infinity = float('inf')
    action, state = argmax(successors_of(state), lambda a: min_value(a[1]))
    return state


def is_terminal(state):
    """
    returns True if the state is either a win or a tie (board full)
    :param state: State of the checkerboard. Ex: [0; 1; 2; 3; X; 5; 6; 7; 8]
    :return:
    """
    print("state ", state)
    return max(state) <= 2


def utility_of(state):
    """
    returns +1 if winner is X (MAX player), -1 if winner is O (MIN player), or 0 otherwise
    :param state: State of the checkerboard. Ex: [0; 1; 2; 3; X; 5; 6; 7; 8]
    :return:
    """
    utility = 0
    if len(state) % 2 == 0:
        utility = -1
    else:
        utility = 1

    return utility


def successors_of(state):
    """
    returns a list of tuples (move, state) as shown in the exercise slides
    :param state: State of the checkerboard. Ex: [0; 1; 2; 3; X; 5; 6; 7; 8]
    :return:
    """
    successors = []
    for position in range(len(state)):
        for first_value in range(1, math.floor(state[position] / 2) + 1):
            second_value = state[position] - first_value
            if first_value != second_value:
                state_copy = state.copy()
                state_copy[position:position + 1] = [first_value, second_value]
                successors.append((position, state_copy))
    print(successors)
    return successors


def display(state):
    print("-----")
    print(state)


def main():
    value = [7]
    # print(is_terminal(testBoard))
    winner = "player 2"
    while not is_terminal(value):
        print("----------- player 1 ----------------")
        value = minmax_decision(value)
        if not is_terminal(value):
            display(value)
            print("----------- player 2")
            # value = minmax_decision(value)
            player_input(value)
        else:
            winner = "player 1"
    print(winner)
    display(value)


def player_input(value):
    position = int(input("enter position: "))
    first_value = int(input("enter first value: "))
    second_value = int(input("enter second value: "))
    value[position:position + 1] = [first_value, second_value]


def argmax(iterable, func):
    return max(iterable, key=func)


if __name__ == '__main__':
    main()
