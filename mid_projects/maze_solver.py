# Define a 2D array representation of a maze
maze = [
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 1, 0, 1, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 0, 0]
]

# Determine the dimensions of the maze
maze_len = [len(maze), len(maze[0])]
# Set the finish position of the maze
finish_pos = (0, 4)


def find_exit():
    """
    Function to find an exit in a maze given a start position.
    The function accepts the start position from user input.
    """
    start_pos = input("Enter the start point row,column: ")
    current_pos = start_pos
    # Keep track of already passed positions
    passed_pos = {}
    # True path through the maze
    true_path = []
    # Temporary storage for a true path
    tmp_true_path = [current_pos]
    # Turnout holds alternative paths when a decision point is met
    turnout = []
    tmp_turnouts = [[]]
    # Check for available ways at the current position
    check_available_ways = True
    while True:
        # Check if the current position is the finish position
        if tuple(current_pos) == finish_pos:
            for turn_out in tmp_turnouts:
                for pos in turn_out:
                    tmp_true_path.append(str_current_pos(pos))
            # Decision point handling
            if len(turnout[0]) == 1 and passed_pos.get(str_current_pos(turnout[0][0]), False):
                turnout.pop()
            # Path optimisation, keep only the shortest path
            if len(true_path) == 0 or len(tmp_true_path) < len(true_path):
                true_path = tmp_true_path
            tmp_true_path = [start_pos]
            if turnout == []:
                return true_path
            check_available_ways = False
            
        if check_available_ways:
            avaliable_ways = look_around(current_pos, passed_pos)
        else:
            check_available_ways = True
            avaliable_ways = []
        # Check for decision points
        if len(avaliable_ways) > 1:
            passed_pos[str_current_pos(current_pos)] = True
            current_pos = avaliable_ways[-1]
            tmp_turnouts.append([])
            tmp_turnouts[-1].append(current_pos)
            turnout.append(avaliable_ways[:-1])
        # Move forward if only one way is available
        elif len(avaliable_ways) == 1:
            passed_pos[str_current_pos(current_pos)] = True
            current_pos = avaliable_ways[0]
            if tmp_turnouts[-1]:
                tmp_turnouts[-1].append(current_pos)
            else:
                true_path.append(str_current_pos(current_pos))
        # Dead-end handling
        else:
            # Backtrack if at a dead-end
            if len(turnout[-1]) >= 1:
                tmp_turnouts.pop()
                tmp_turnouts.append([])
                current_pos = turnout[-1][-1]
                tmp_turnouts[-1].append(current_pos)
                turnout[-1].pop()
            else:
                if tuple(current_pos) != finish_pos:
                    passed_pos[str_current_pos(current_pos)] = True
                tmp_turnouts.pop()
                tmp_turnouts.pop()
                tmp_turnouts.append([])
                turnout.pop()
                current_pos = turnout[-1][-1]
                tmp_turnouts[-1].append(current_pos)
                


def look_around(current_pos, passed_pos):
    """
    Function to look around the current position in the maze.
    It returns the available positions around the current position (up, down, left, right).
    """
    pos_row, pos_column = map(int, str_current_pos(current_pos).split(","))
    # Define possible ways to go from the current position
    ways = [
        [pos_row, pos_column + 1],  # Right
        [pos_row, pos_column - 1],  # Left
        [pos_row + 1, pos_column],  # Down
        [pos_row - 1, pos_column]   # Up
    ]
    # Keep only those positions that are within the maze boundaries
    ways = [way for way in ways if 0 <= way[0] <= maze_len[0] - 1 and 0 <= way[1] <= maze_len[1] - 1]
    # Filter out ways that are blocked or already passed
    avaliable_ways = [way for way in ways if maze[way[0]][way[1]] == 0 and not passed_pos.get(f"{way[0]},{way[1]}", False)]
    return avaliable_ways


def str_current_pos(current_pos):
    """
    Function to convert current position into string format.
    """
    return ",".join(list(map(str, current_pos))) if type(current_pos) == list else current_pos


print(find_exit())