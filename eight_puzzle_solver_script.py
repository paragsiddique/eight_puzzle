# -*- coding: utf-8 -*-
"""
Created on Sun Jan  5 10:40:15 2020

@author: parag
"""

def eight_puzzle_solver(start_node):
    """
    INPUT
    start_node: a starting position for the 8 puzzle game
                e.g., [0, 1, 3, 4, 2, 5, 7, 8, 6]
    
    Return: a path to goal node
    
    goal_node = [1, 2, 3, 4, 5, 6, 7, 8, 0]
    """
    try:
        explored, path = eight_puzzle_bfs(start_node)

        print(explored)

        path_formatted = [[] for i in range(len(path))]
        for i in range(len(path)):
            path_formatted[i] = [x[1] for x in path[i]]

        for i, x in enumerate(path_formatted):
            print("{0:0=2d}".format(i), ' : ', x)
    except:
        print("Path not found")
        
def eight_puzzle_bfs(start_node):

    grid = [31, 32, 33, 21, 22, 23, 11, 12, 13]
    
    goal_node = [1, 2, 3, 4, 5, 6, 7, 8, 0]
    
    start_state = tuple((zip(grid, start_node)))
    goal_state = tuple((zip(grid, goal_node)))
    
    #frontier
    queue = [start_state]
    
    #explored nodes
    explored = set()
    
    #tracking parent child
    parent_child = {}
        
    while queue:
        current_state = queue.pop(0)
        if current_state == goal_state:
            #winner_state = current_state
            path = reconstruct_path(parent_child, start_state, goal_state)
            return 'Path found after exploring '+ str(len(explored)) + ' nodes', path
                    
        explored.add(current_state)
        
        legal_moves = possible_moves(current_state, grid)
        
        neighbours = eight_puzzle_neighbours(current_state, legal_moves)
        
        #parent_child.append((current_state, set(neighbours)))
        
        for neighbour in neighbours:
            if neighbour not in explored and neighbour not in queue:
                queue.append(neighbour)
                parent_child[neighbour] = current_state
              
    return 'Path not found after exploring '+ str(len(explored)) + ' nodes'

def reconstruct_path(came_from, start, goal):
    current = goal
    path = []
    while current != start:
        path.append(current)
        current = came_from[current]
    path.append(start) 
    path.reverse() 
    return path

def eight_puzzle_neighbours(state, legal_moves):
    list_of_neighbour_states = []
    for x in legal_moves:
        list_of_neighbour_states.append(neighbour_state_generate(state, x))
    return list_of_neighbour_states

def possible_moves(current_state, grid):
    for items in current_state:
        if items[1] == 0:
            zero_cell = items[0]

    move_up = zero_cell + 10
    move_down = zero_cell - 10
    move_right = zero_cell + 1
    move_left = zero_cell - 1

    moves = [move_up, move_down, move_right, move_left]
    legal_moves = [x for x in grid if x in moves]
    
    return legal_moves

def neighbour_state_generate(state, legal_move_cell):
    
    pre_neighbour_state = [list(x) for x in state]

    for x in pre_neighbour_state:
        if x[0] == legal_move_cell:
            value_to_be_swapped = x[1]


    for x in pre_neighbour_state:
        if x[1] == 0:
            x[1] = value_to_be_swapped

    for x in pre_neighbour_state:
        if x[0] == legal_move_cell:
            x[1] = 0

    neighbour_state = tuple([tuple(x) for x in pre_neighbour_state])
    
    return neighbour_state
