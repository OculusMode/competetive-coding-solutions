# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000434ba1/00000000004347b2#problem
EMP = '.'
WALL = '#'
#                 N  W  S  E  
# robot_states = (0, 1, 2, 3)
states = 'NWSE'

def places_to_check(i, j, state):
    return (
        (i  , j-1), # N
        (i+1, j), # W
        (i, j+1), # S
        (i-1, j), # E
    )[state]
    
for _ in range(int(input())):
    print('Case #' + str(_+1) + ': ', end='' )
    state = 2
    n = int(input())
    maze = [[1 if i == EMP else 0 for i in input()] for i in range(n)]
    x, y, goal_x, goal_y = map(int, input().split())
    if x == n:
        state = 0
    soln = ''
    steps = 0
    max_steps = 10_000
    next_i, next_j = x, y
    while steps<max_steps:
        if next_i == goal_x and next_j == goal_y:
            print(steps)
            print(soln)
            break
        last_i, last_j = next_i, next_j # storing temp
        next_i, next_j = places_to_check(last_i, last_j, state)
        times_checked = 0
        not_found = False
        while next_i-1 < 0 or next_i-1 >= n or next_j-1 < 0 or next_j-1 >= n or maze[next_i-1][next_j-1] == 0:
            if times_checked == 4:
                print('Edison ran out of energy.')
                not_found = True
                break
            state = (state - 1) % 4
            next_i, next_j = places_to_check(last_i, last_j, state)
            times_checked += 1
        if not_found:
            break
        if next_i == last_i - 1:
            state = 0
        elif next_i == last_i + 1:
            state = 2
        elif next_j == last_j - 1:
            state = 1
        else:
            state = 3
        soln+=states[state]
        steps+=1
    else:
        print('Edison ran out of energy.')
