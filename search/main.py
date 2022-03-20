"""
COMP30024 Artificial Intelligence, Semester 1, 2022
Project Part A: Searching

This script contains the entry point to the program (the code in
`__main__.py` calls `main()`). Your solution starts here!
"""

import sys
import json
import math
from copy import deepcopy
from time import sleep

# If you want to separate your code into separate files, put them
# inside the `search` directory (like this one and `util.py`) and
# then import from them like this:
# from search.util import board_to_dict, print_board, print_coordinate
from search.util import *

class PriorityQueue():

  def __init__(self):
    self.store = {}

  def enq(self, element, weight):
    if weight in self.store:
      self.store[weight].append(element)
    else:
      self.store[weight] = [element]

  def deq(self):
    if len(self.store.keys()) == 0:
      return None
    max_weight = sorted(self.store.keys())[0]
    element = self.store[max_weight].pop(0)
    if len(self.store[max_weight]) == 0:
      del self.store[max_weight]
    return element

class Node():
    def __init__(self, cell, g, h):
        self.cell = cell
        self.g = g
        self.h = h
        self.f = g + h

def distance_between(cell_a, cell_b):
    size = 1 / math.sqrt(3)
    width = math.sqrt(3) * size
    height = 2 *  size
    vert_adjacent = height * 3/4
    q_dist = cell_a[1] - cell_b[1]
    r_dist = cell_a[0] - cell_b[0]
    vertical_dist = vert_adjacent * r_dist
    horizontal_offset = r_dist * width / 2
    horizontal_move = q_dist * width
    horizontal_dist = horizontal_offset + horizontal_move
    return round(math.sqrt(vertical_dist * vertical_dist + horizontal_dist * horizontal_dist), 1)

def get_adj_cells(cell, board, n):
    # can't incremenet or decrement both at same time
    # cell isn't adjacent to itself
    # can't go beyond board boundary
    # can't be an occupied cell
    cell_r = cell[0]
    cell_q = cell[1]
    adjacent_cells = []
    for r in range(cell_r - 1, cell_r + 2):
        for q in range(cell_q - 1, cell_q + 2):
            # double increment/decrement case
            if abs((cell_r - r) + (cell_q - q)) == 2:
                continue
            # outside boundary case
            if r < 0 or q < 0 or r == n or q == n:
                continue
            # same cell case
            if cell_r == r and cell_q == q:
                continue
            # occupied cell case
            if (r, q) in board:
                if board[(r, q)] != "G":
                    continue
            # append cell coordinates to list
            adjacent_cells.append((r, q))
    return adjacent_cells

def get_cleared_board(n):
    board = {}
    for q in range(n):
        for r in range(n):
            board[(r, q)] = ""
    return board

def populate_board(board, pq, n):
    npq = deepcopy(pq)
    this_node = npq.deq()
    while(this_node):
        board[this_node.cell] = this_node.f
        this_node = npq.deq()
    return board

def search(pq, goal_cell, board, n, previous, found):
    current_node = pq.deq()
    if current_node.cell == goal_cell:
        found = True
    if not current_node or found:
        return previous
    board[current_node.cell] = 'e'
    adj_cells = get_adj_cells(current_node.cell, board, n)
    for cell in adj_cells:
        previous[cell] = current_node.cell
        g = current_node.g + 1
        h = distance_between(cell, goal_cell)
        child_node = Node(cell, g, h)
        pq.enq(child_node, child_node.f)
    # print_board(n, populate_board(board, pq, n))
    populate_board(board, pq, n)
    # sleep(0.8)
    return search(pq, goal_cell, board, n, previous, False)

def main():
    try:
        with open(sys.argv[1]) as file:
            data = json.load(file)
    except IndexError:
        print("usage: python3 -m search path/to/input.json", file=sys.stderr)
        sys.exit(1)

    board = board_to_dict(data['board'])
    start_cell = tuple(data["start"])
    goal_cell = tuple(data["goal"])
    board[goal_cell] = "G"
    n = data['n']
    pq = PriorityQueue()
    start_node = Node(start_cell, 0, distance_between(start_cell, goal_cell))
    pq.enq(start_node, start_node.f)
    previous = search(pq, goal_cell, board, n, {}, False)
    if goal_cell not in previous:
        print("Goal cell unreachable")
        return
    route = []
    prev_cell = previous[goal_cell]
    while prev_cell != start_cell:
        route.append(prev_cell)
        prev_cell = previous[prev_cell]
    route.reverse()
    route.insert(0, start_cell)
    route.insert(len(route), goal_cell)
    print(len(route))
    for cell in route:
        print(cell)

    solution_board = get_solution_board(board_to_dict(data['board']), route)
    print_board(n, solution_board, "Solution Board")
        


    # TODO:
    # Find and print a solution to the board configuration described
    # by `data`.
    # Why not start by trying to print this configuration out using the
    # `print_board` helper function? (See the `util.py` source code for
    # usage information).
