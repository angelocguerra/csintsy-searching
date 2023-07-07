"""
    Title: CSINTSY Major Course Output 1: Searching
    Group members:
    1. Nicolas, Aaron
    2. Cheng, Adrian
    3. Guerra, Angelo
    4. Tuballa, Hans
    5. Salih, Shems

    A dynamic model and implementation of the Breadth First Search algorithm that simulates optimal path finding.
    Original author: Ryan Gilera 
    Github repository link: https://github.com/Daytron/graph-bfs-dfs-gui

    The group have modified the code to suit the requirements of the project.

"""


import simpleguitk as simplegui

# Constants
HEIGHT = 400
WIDTH = 500
NODE_SPACE_ALLOWANCE = 20
EDGE_COLOR = "Blue"
EDGE_SIZE = 2
NODE_LABEL_COLOR = "White"
NODE_COLOR = "Green"
NODE_MARK_COLOR = "Orange"

# Global variables
start = 0
goal = 0
placeNodes = True
setNodesRelation = False
draw_relations = False
draw_mark_relations = False
setGoal = False
setStart = False
displayResult = False
lock_nodes = False
nodes = []

pos1 = [0, 0]
pos2 = [0, 0]
pos_lock = False
indx = 0
letter_label_default = '@'
letter_pos = 1
current_node_letters_low = []
current_node_letters_up = []


class Point:
    def __init__(self, pos, node_colour, node_mark_colour):
        self.pos = pos
        self.children = []
        self.radius = 5
        self.colour = node_colour
        self.mark_colour = node_mark_colour
        self.index = 0
        self.is_mark = False
        self.label = '@'

    def draw(self, canvas):
        if self.is_mark == False:
            canvas.draw_circle(self.pos, self.radius, 6, self.colour)
        else:
            canvas.draw_circle(self.pos, self.radius, 6, self.mark_colour)

# This function is called when the user clicks the mouse on the canvas. 
# It handles the logic for placing nodes, setting node relations, and creating edges between nodes based on user input.
def mouseclick(pos):
    global pos1, pos2, pos_lock, indx, draw_relations, draw_mark_relations, nodes, indx_mark_color
    global letter_label_default, letter_pos

    # Creates new instance of point(node) if the last position of
    # the mouseclick is not on  top of a previous node
    allow_place_node = True

    if placeNodes:
        if nodes:  # Checks if the nodes are not empty
            for p, location in enumerate(nodes):
                if (((nodes[p].pos[0] - NODE_SPACE_ALLOWANCE) <= pos[0] <= (
                        nodes[p].pos[0] + NODE_SPACE_ALLOWANCE)) and
                        ((nodes[p].pos[1] - NODE_SPACE_ALLOWANCE) <= pos[1] <= (
                                nodes[p].pos[1] + NODE_SPACE_ALLOWANCE))):
                    print("Warning: Cannot create node on top of another node!")
                    allow_place_node = False
                    break
            # Creates new instance of Point class if no nodes detected in 
            # the vicinity of mouseclick position
            if allow_place_node:
                nodes.append(Point(pos, NODE_COLOR, NODE_MARK_COLOR))
                nodes[-1].label = chr(ord(letter_label_default) + letter_pos)
                letter_pos += 1
        # Else creates a node for first time 
        else:
            nodes.append(Point(pos, NODE_COLOR, NODE_MARK_COLOR))
            nodes[-1].label = chr(ord(letter_label_default) + letter_pos)
            letter_pos += 1

    # Sets up the edges or links
    if setNodesRelation == True:

        # If mouseclick pos is on top of a current node mark that node
        for i, position in enumerate(nodes):
            if (((nodes[i].pos[0] - NODE_SPACE_ALLOWANCE) <= pos[0] <= (
                    nodes[i].pos[0] + NODE_SPACE_ALLOWANCE)) and
                    ((nodes[i].pos[1] - NODE_SPACE_ALLOWANCE) <= pos[1] <= (
                            nodes[i].pos[1] + NODE_SPACE_ALLOWANCE))):
                if pos_lock == False:
                    pos1[0] = pos[0]
                    pos1[1] = pos[1]

                    indx = i
                    indx_mark_color = i
                    pos_lock = True
                    draw_mark_relations = True
                    break

                else:
                    # If it is the second node that is not the same of 
                    # the first marked node, then creates a new relation/edge
                    if i != indx:
                        pos2[0] = pos[0]
                        pos2[1] = pos[1]
                        nodes[indx].children.append(i)
                        nodes[i].children.append(indx)

                        pos_lock = False
                        draw_relations = True
                        draw_mark_relations = False
                        break
                    else:
                        print("Warning: Recursion or self loop is not allowed.")

# This function is called when the "Reset edge drawing" button is clicked. 
# It resets the variables related to drawing edges between nodes.
def button_refresh_new_relation():
    global pos_lock, pos1, pos2, nodes, draw_relations, draw_mark_relations

    if lock_nodes == False and setNodesRelation == True:
        pos_lock = False
        draw_mark_relations = False
        draw_relations = False
        pos1[0] = 0
        pos1[1] = 0
        pos2[0] = 0
        pos2[1] = 0

        # This empties the list of children attribute of Point class
        for i, child in enumerate(nodes):
            del nodes[i].children[:]
    else:
        print("Warning: This action is not allowed.")

# This function is called when the "Lock in the nodes" button is clicked. 
# It locks the placement of nodes and enables the setting of node relations.
def button_lock_nodes():
    global placeNodes, setNodesRelation, current_node_letters_up, nodes, current_node_letters_low

    # Can only lock nodes if the set-up is right
    # Prevents locking nodes later in the program
    if placeNodes == True and setNodesRelation == False and setStart == False and setGoal == False:
        placeNodes = False
        setNodesRelation = True

        # Fills two new lists of all node labels(letters) 
        # for later use in input start and goal
        if nodes:
            for n, obj in enumerate(nodes):
                current_node_letters_up.append(nodes[n].label)

            for let in current_node_letters_up:
                current_node_letters_low.append(let.lower())

        print("The nodes are now locked in!")
    else:
        print("Warning: This action is not allowed.")

# This function is called when the "Lock in the graph" button is clicked. 
# It locks the graph and sets the index attribute of each node for later reference.
def button_lock_graph():
    global placeNodes, setNodesRelation, nodes, lock_nodes

    if setNodesRelation is True:
        placeNodes = False
        setNodesRelation = False
        lock_nodes = True

        # Sets the index of nodes list and apply it to each index attribute of Point class
        # for index/element reference only, for later use in BFS and DFS functions
        for d, dot in enumerate(nodes):
            nodes[d].index = d
            print("node" + str(d + 1) + ":", nodes[d].label)

            # This is important
            # This sorts the elements of children attribute list in ascending order
            nodes[d].children.sort()

        print("Graph is now set!")
    else:
        print("Warning: This action is not allowed.")

# This function is called when the user enters a start node. 
# It handles the logic for setting the start node based on user input (either a number or a letter).
def input_start_handler(start_string):
    global start, nodes, setStart

    setStart = False
    if start_string.isdigit():
        # Allows number as input for starting node
        # 1 for A, 2 for B and so on and so forth
        temp_start = int(start_string) - 1
        for element, num in enumerate(nodes):
            if temp_start == element:
                # Minus one because node label starts at 1 not zero(index)
                start = temp_start
                print("Start:", chr(start + 65))
                setStart = True
                break
        if setStart == False:
            print("Warning: This number is outside of the nodes!")
    else:
        # Allows letter as input for starting node
        if start_string in current_node_letters_up:
            start = ord(start_string) - 65
            setStart = True
            print("Start:", chr(start + 65))
        else:
            if start_string in current_node_letters_low:
                start = ord(start_string) - 97
                setStart = True
                print("Start:", chr(start + 65))
            else:
                print("Warning: Unknown input. Enter a number or the node letter.")

# This function is called when the user enters a goal node. 
# It handles the logic for setting the goal node based on user input (either a number or a letter).
def input_goal_handler(goal_string):
    global goal, nodes, setGoal

    setGoal = False
    if goal_string.isdigit():

        # Allows number as input for goal node
        # 1 for A, 2 for B and so on and so forth
        temp_goal = int(goal_string) - 1
        for element, num in enumerate(nodes):
            if temp_goal == element:
                # minus one because node label starts at 1 not zero(index)
                goal = temp_goal
                print("Goal:", chr(goal + 65))
                setGoal = True
                break
        if setGoal == False:
            print("Warning: This number is outside of the nodes!")
    else:
        # Allows letter as input for goal node
        if goal_string in current_node_letters_up:
            goal = ord(goal_string) - 65
            setGoal = True
            print("Goal:", chr(goal + 65))
        else:
            if goal_string in current_node_letters_low:
                goal = ord(goal_string) - 97
                setGoal = True
                print("Goal:", chr(goal + 65))
            else:
                print("Warning: Unknown input. Enter a number or the node letter.")

# This function is called when the "Find BFS" button is clicked. 
# It performs the breadth-first search algorithm on the graph to find the optimal path from the start node to the goal node.
def button_breadth_first_search():

    # Global variables.
    global nodes, displayResult, result_string, queue_string, pointer_string

    displayResult = False
    pointer_string = ""

    # Resets all nodes markings (color).
    for d, marking_obj in enumerate(nodes):
        nodes[d].is_mark = False

    in_queue_result = False

    # Checks if the following conditions are met:
    #   * The user is not placing nodes.
    #   * The user is not setting the relations between nodes.
    #   * The user has set the start node.
    #   * The user has set the goal node.

    if placeNodes == False and setNodesRelation == False and setStart == True and setGoal == True:

        print(" ")
        print("BFS starts here:")

        # Checks if the `queue` variable is defined. If it is, then the function empties the list. Otherwise, the function creates a new list.
        try:
            queue = []
        except:
            queue = []
        else:
            del queue[:]

        # Appends the start node to the `queue` list and marks the start node as visited.
        queue.append(nodes[start])
        queue[0].is_mark = True

        try:
            result = []
        except:
            result = []
        else:
            del result[:]

        # While the `queue` list is not empty:
        while queue:
            
            # Removes the first node from the `queue` list and stores it in the `pointer` variable.
            pointer = queue.pop(0)

            # Marks the `pointer` node as visited.
            pointer.is_mark = True

            # Prints the `pointer` node.
            print(" ")
            print("Pointer:", pointer.label)

            if pointer.index == goal:
                pointer_string = "Pointer: " + pointer.label
                result_string = "Result: "
                queue_string = "Queue: "

                for obj in result:
                    result_string += str(obj.label)
                    result_string += " "
                for objt in queue:
                    queue_string += str(objt.label)
                    queue_string += " "

                displayResult = True
                print("SUCCESS!")
                break
            else:
                result.append(pointer)

                for neighbor in pointer.children:
                    in_queue_result = False
                    for i in queue:
                        # print "neighbor:", neighbor+1, "queue:", i.index+1
                        if neighbor == i.index:
                            in_queue_result = True

                    for j in result:
                        # print "neighbor:", neighbor+1, "result:", j.index+1
                        if neighbor == j.index:
                            in_queue_result = True

                    if not in_queue_result:
                        for objct in nodes:
                            if objct.index == neighbor:
                                queue.append(nodes[objct.index])

        # Sets the `pointer_string`, `result_string`, and `queue_string` variables to the strings that represent the BFS algorithm's path to the goal node, the nodes that have been visited, and the nodes that are still in the queue, respectively.
        result_string = "Result: "
        queue_string = "Queue: "
        for obj in result:
            result_string += str(obj.label)
            result_string += " "
        print(result_string)

        for objt in queue:
            queue_string += str(objt.label)
            queue_string += " "
        print(queue_string)


# This function is called to draw the nodes, edges, and results on the canvas. It also updates the display when necessary.
def draw_handler(canvas):

    # Global variables.
    global result_string, queue_string, pointer_string
    global placeNodes, setNodesRelation, setStart, setGoal, pos1

    # Draws nodes.
    if draw_mark_relations == True and setNodesRelation == True:
        canvas.draw_circle(nodes[indx_mark_color].pos, 15, 3, "Yellow", "Black")

    if nodes:
        for i, vertex in enumerate(nodes):

            # Draws the node.
            vertex.draw(canvas)

            # Draws the node's label.
            canvas.draw_text(vertex.label, (vertex.pos[0] - 30, vertex.pos[1]), 20, NODE_LABEL_COLOR)

    # Draws edges.
    if draw_relations:
        for n, point in enumerate(nodes):

            # Checks if the node has any children.
            if nodes[n].children:

                # Iterates through the node's children.
                for child in nodes[n].children:

                    # Draws a line between the node and its child.
                    canvas.draw_line(nodes[n].pos, nodes[child].pos, EDGE_SIZE, EDGE_COLOR)

    # Displays the results of the BFS algorithm.
    if displayResult:

        # Draws the text that represents the BFS algorithm's path to the goal node.
        canvas.draw_text(pointer_string, (30, 345), 15, NODE_LABEL_COLOR)

        # Draws the text that represents the nodes that have been visited.
        canvas.draw_text(result_string, (30, 370), 15, NODE_LABEL_COLOR)

        # Draws the text that represents the nodes that are still in the queue.
        canvas.draw_text(queue_string, (30, 395), 15, NODE_LABEL_COLOR)



# Creates the frame window
frame = simplegui.create_frame("Graph Node Search with BFS", WIDTH, HEIGHT)

frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw_handler)

# Button, input and label controls for the frame window
button1 = frame.add_button('Lock in the nodes', button_lock_nodes)
label1 = frame.add_label(' ')

button2 = frame.add_button('Lock in the graph', button_lock_graph)
label2 = frame.add_label(' ')

button3 = frame.add_button('Reset edge drawing', button_refresh_new_relation)
label3 = frame.add_label(' ')

input_start = frame.add_input('Set start', input_start_handler, 50)
label4 = frame.add_label(' ')

input_goal = frame.add_input('Set goal', input_goal_handler, 50)
label5 = frame.add_label(' ')

button4 = frame.add_button('Find BFS', button_breadth_first_search)


# Program starts here
frame.start()
