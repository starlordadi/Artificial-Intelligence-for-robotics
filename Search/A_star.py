#! usr/bin/env python
# ----------
# User Instructions:
# 
# Define a function, search() that returns a list
# in the form of [optimal path length, row, col]. For
# the grid shown below, your function should output
# [11, 4, 5].
#
# If there is no valid path from the start point
# to the goal, your function should return the string
# 'fail'
# ----------

# Grid format:
#   0 = Navigable space
#   1 = Occupied space

grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0]]

heuristic = [[9, 8, 7, 6, 5, 4],
             [8, 7, 6, 5, 4, 3],
             [7, 6, 5, 4, 3, 2],
             [6, 5, 4, 3, 2, 1],
             [5, 4, 3, 2, 1, 0]]
init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]
# goal = [1,4]
cost = 1
delta = [[-1, 0], # go up
         [ 0,-1], # go left
         [ 1, 0], # go down
         [ 0, 1]] # go right

delta_name = ['^', '<', 'v', '>']

def search(grid,init,goal,cost,heuristic):
    # ----------------------------------------
    # insert code here
    # ----------------------------------------
    closed = [[0 for row in range(len(grid[0]))] for col in range(len(grid))]
    closed[init[0]][init[1]] = 1
    expand = [[-1 for row in range(len(grid[0]))] for col in range(len(grid))]
    path = [[' ' for row in range(len(grid[0]))] for col in range(len(grid))]
    action = [[0 for row in range(len(grid[0]))] for col in range(len(grid))]


    count = 0
    x = init[0]
    y = init[1]
    g = 0
    h = heuristic[x][y]
    f = g + h

    open_list = [[f, g, h, x, y]]
    # print len(open_list)
    Found = False
    Resign = False

    while Found is False and Resign is False:
        if len(open_list) == 0:
            Resign = True
            print "False"

        else:
            open_list.sort()
            open_list.reverse()
            next = open_list.pop()

            x = next[3]
            y = next[4]
            g = next[1]
            expand[x][y] = count
            count += 1
            if x == goal[0] and y == goal[1]:
                Found = True
                print next

            else:
                for i in range(len(delta)):
                    x2 = x + delta[i][0]
                    y2 = y + delta[i][1]
                    if x2 >= 0 and x2 < len(grid) and y2 >= 0 and y2 < len(grid[0]):
                        if closed[x2][y2] == 0 and grid[x2][y2] == 0:
                            g2 = g + cost
                            h2 = heuristic[x2][y2]
                            f2 = g2 + h2
                            open_list.append([f2, g2, h2, x2, y2])
                            closed[x2][y2] = 1
                            action[x2][y2] = i
                # count = count + 1

    x = goal[0]
    y = goal[1]
    path[x][y] = '*'
    while x != init[0] or y != init[1]:
        x2 = x - delta[action[x][y]][0]
        y2 = y - delta[action[x][y]][1]
        path[x2][y2] = delta_name[action[x][y]]
        x = x2
        y = y2
    for i in range(len(path)):
        print path[i]
    return expand

print search(grid,init,goal,cost,heuristic)