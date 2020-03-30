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
    return action


def is_terminal(state):
    """
    returns True if the state is either a win or a tie (board full)
    :param state: State of the checkerboard. Ex: [0; 1; 2; 3; X; 5; 6; 7; 8]
    :return:
    """
    StateIsTerminal = False

    if state.count('X') + state.count('O') >= len(state):
        return True
    for x in range(0, len(state) - 1, 3):
        horizontalX = state[x:(x + 3)].count('X') == 3
        horizontalO = state[x:(x + 3)].count('O') == 3

        verticalX = [state[math.floor(x / 3)], state[math.floor(x / 3) + 3], state[math.floor(x / 3) + 6]].count(
            'X') == 3
        verticalO = [state[math.floor(x / 3)], state[math.floor(x / 3) + 3], state[math.floor(x / 3) + 6]].count(
            'O') == 3

        if verticalX or horizontalX or verticalO or horizontalO:
            # display(state)
            return True

    leftToRightX = [state[0], state[4], state[8]].count('X') == 3
    leftToRightO = [state[0], state[4], state[8]].count('O') == 3
    rightToLeftX = [state[2], state[4], state[6]].count('X') == 3
    rightToLeftO = [state[2], state[4], state[6]].count('O') == 3

    if leftToRightX or leftToRightO or rightToLeftX or rightToLeftO:
        # display(state)
        return True

    return StateIsTerminal


def utility_of(state):
    """
    returns +1 if winner is X (MAX player), -1 if winner is O (MIN player), or 0 otherwise
    :param state: State of the checkerboard. Ex: [0; 1; 2; 3; X; 5; 6; 7; 8]
    :return:
    """
    utility = 0

    for x in range(0, len(state) - 1, 3):
        horizontalX = state[x:(x + 3)].count('X') == 3
        horizontalO = state[x:(x + 3)].count('O') == 3

        verticalX = [state[math.floor(x / 3)], state[math.floor(x / 3) + 3], state[math.floor(x / 3) + 6]] \
                        .count('X') == 3
        verticalO = [state[math.floor(x / 3)], state[math.floor(x / 3) + 3], state[math.floor(x / 3) + 6]] \
                        .count('O') == 3

        if verticalX or horizontalX:
            utility = 1
        elif verticalO or horizontalO:
            utility = -1

    leftToRightX = [state[0], state[4], state[8]].count('X') == 3
    leftToRightO = [state[0], state[4], state[8]].count('O') == 3
    rightToLeftX = [state[2], state[4], state[6]].count('X') == 3
    rightToLeftO = [state[2], state[4], state[6]].count('O') == 3
    if leftToRightX or rightToLeftX:
        utility = 1
    elif leftToRightO or rightToLeftO:
        utility = -1

    return utility


def successors_of(state):
    """
    returns a list of tuples (move, state) as shown in the exercise slides
    :param state: State of the checkerboard. Ex: [0; 1; 2; 3; X; 5; 6; 7; 8]
    :return:
    """
    count = Counter(state)
    turn = 'O'
    if count['X'] <= count['O']:
        turn = 'X'
    successors = []
    counter = 0
    for x in range(0, len(state)):
        if state[x] != 'X' and state[x] != 'O':
            duplicate = state.copy()
            duplicate[x] = turn
            successors.append((x, duplicate))
            counter += 1
    return successors


def display(state):
    print("-----")
    for c in [0, 3, 6]:
        print(state[c + 0], state[c + 1], state[c + 2])


def main():
    board = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    # testBoard = ['X', 1, 2, 3, 4, 5, 'X', 7, 8]
    # print(is_terminal(testBoard))
    while not is_terminal(board):
        board[minmax_decision(board)] = 'X'
        if not is_terminal(board):
            display(board)
            board[int(input('Your move? '))] = 'O'
    display(board)


def argmax(iterable, func):
    return max(iterable, key=func)


if __name__ == '__main__':
    main()
