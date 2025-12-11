
Assessments
Instructions
You are given a 2D grid representing a maze, where each cell is either an empty space (0) or a wall (1). Your task is to implement a Python program that uses Iterative Deepening Depth-First Search (IDDFS) to determine whether a valid path exists from a given start cell to a specified target cell. You may move up, down, left, or right to adjacent empty cells, but you cannot pass through walls, and each cell may be visited only once during a single path exploration.

Case#1Input:
4 4
0 0 1 0
1 0 1 0
0 0 0 0
1 1 0 1
Start: 0 0
Target: 2 3

Case#1Output:
Path found at depth 5 using IDDFS
Traversal Order: [(0,0), (0,1), (1,1), (2,1), (2,2), (2,3)]

Case#2Input:
3 3
0 1 0
0 1 0
0 1 0
Start: 0 0
Target: 2 2

Case#2Output:
Path not found at max depth 6 using IDDFS

Instructions
Prepare your lab report and include the GitHub link (with a proper README).
Submit only the lab report as a PDF; do not submit any other file formats.
Rename the file as ID-CSE316-223D4-LabReport01-IDDFS.
Violation of any instruction will result in mark deduction.
Any form of copying will result in a ZERO.
If you have any questions, feel free to ask.
