# AI_Coursework
Coursework to Dr Harrient by Mwebesa Johnson


This repository contains Python implementations for two algorithm-based problem-solving tasks:
Maze Solver using Breadth-First Search (BFS)

Ambulance Dispatch System using A* Search Algorithm

Files
1. maze_solver.py
Description: Solves a 5x5 grid maze using Breadth-First Search algorithm.

Features:

Finds the shortest path from start to goal in a maze

Handles walls and obstacles

Returns the complete path coordinates

Usage:

python
python maze_solver.py
Maze Representation:

'S' = Start position

'G' = Goal position

0 = Free path

1 = Wall/Obstacle

Example Maze:

text
0 S 0 0 0
1 1 0 1 1
0 0 0 0 0
1 0 1 1 0
0 0 0 0 G
2. ambulance_dispatch.py
Description: Implements an AI system for ambulance dispatch in a city using A* search algorithm.

Features:

Models city as a graph with travel times between locations

Handles multiple ambulances and emergencies

Prioritizes emergencies based on severity

Finds optimal routes considering travel time

Usage:

python
python ambulance_dispatch.py
Key Components:

State space: Ambulance locations, emergency calls, traffic conditions

Actions: Dispatch, re-route, or keep ambulances in place

Goal: Minimize response time to emergencies

Path cost: Travel time, emergency priority, distance

Requirements
Python 3.6+

No external dependencies required

How to Run
Clone the repository:

bash
git clone <repository-url>
cd algorithm-problem-solving-assignment
Run the maze solver:

bash
python maze_solver.py
Run the ambulance dispatch system:

bash
python ambulance_dispatch.py
Algorithms Implemented
Breadth-First Search (BFS)
Used for maze solving

Guarantees shortest path in unweighted grids

Explores all neighbors at current depth before moving deeper

A* Search Algorithm
Used for ambulance dispatch

Optimal and complete pathfinding

Uses heuristic function to guide search

Efficient for route planning with constraints

Sample Output
Maze Solver Output:
text
Maze Solution using BFS:
Start: (0, 1)
Goal: (4, 4)
Path: [(0, 1), (0, 2), (0, 3), (0, 4), (1, 4), (2, 4), (2, 3), (2, 2), (2, 1), (2, 0), (3, 0), (4, 0), (4, 1), (4, 2), (4, 3), (4, 4)]
Ambulance Dispatch Output:
text
Emergency Dispatch System:
==================================================
First dispatch: Dispatch ambulance A2 to (2, 0). Path: [(1, 1), (2, 1), (2, 0)]. Estimated time: 10
Second dispatch: Dispatch ambulance A1 to (0, 2). Path: [(0, 0), (0, 1), (0, 2)]. Estimated time: 10
Third dispatch: No emergencies
Customization
For Maze Solver:
Modify the maze grid in the code

Change start and goal positions

Adjust maze size (update row and column counts)

For Ambulance Dispatch:
Add more nodes to city_map

Modify travel times between locations

Add more ambulances or hospitals

Adjust emergency priority levels

Author
[Your Name]
[Your Contact Information]
