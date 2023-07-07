## CSINTSY Major Course Output 1: Searching

A dynamic model and implementation of the Breadth First Search algorithm that simulates optimal path finding.

### Instructions for using the BFS Program

1. Start by adding nodes to the graph. The nodes are labeled alphabetically, but if you need more than 26 nodes, the program will use special characters like "[" and "^" to accommodate them.
2. Once you have added all the nodes you need, press the "Lock in the nodes" button to lock their positions.
3. Now you can begin connecting the nodes. To connect two nodes, simply click on the first node, then click on the second node.
4. Once you have connected all the nodes you need, press the "Lock the graph" button to lock the connections.
5. Next, set the start and goal nodes. To do this, type in the letter of the start node and press Enter, then type in the letter of the goal node and press Enter.
6. Finally, press the "Find BFS" button to run the BFS algorithm.

### Labels

* The **Pointer** label indicates the final node the program stopped the search.
* The **Result** label showcases the nodes that the program searched sequentially. For example, if the program checked nodes A, B, C, and D, the result label would show "A B C D".
* The **Queue** label shows whenever there are leftover nodes to be searched in the queue.

### Dependencies

The following dependencies are needed to run this program:

* Python 3.x
* simpleguitk

You can install these dependencies using the following commands:

```
python3 -m pip install simpleguitk
```

Once you have installed the dependencies, you can run the program by typing the following command into the terminal:

```
python3 bfs.py
```

---
Created by: Shem Salih, Angelo Guerra, Adrian Yung Cheng, Aaron Nicolas, and Hans Tuballa<br>
Date Submitted: July 2023
