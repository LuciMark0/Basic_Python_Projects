maze = [
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1],
    [0, 1, 0, 1, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 0, 0]
]

maze_len = [len(maze), len(maze[0])]
finish_pos = (0, 4)


def find_exit():
    current_pos = input("Enter the start point row,column: ")
    passed_pos = {}
    true_path = [current_pos]
    turnout = []
    tmp_turnouts = [[]]

    while True:
        if tuple(current_pos) == finish_pos:
            for turn_out in tmp_turnouts:
                for pos in turn_out:
                    true_path.append(str_current_pos(pos))
            return true_path

        avaliable_ways = look_around(current_pos, passed_pos)

        if len(avaliable_ways) > 1:
            passed_pos[str_current_pos(current_pos)] = True
            current_pos = avaliable_ways[-1]
            tmp_turnouts.append([])
            tmp_turnouts[-1].append(current_pos)
            turnout.append(avaliable_ways[:-1])
        elif len(avaliable_ways) == 1:
            passed_pos[str_current_pos(current_pos)] = True
            current_pos = avaliable_ways[0]
            if tmp_turnouts[-1]:
                tmp_turnouts[-1].append(current_pos)
            else:
                true_path.append(str_current_pos(current_pos))
        else:
            if len(turnout[-1]) >= 1:
                tmp_turnouts.pop()
                tmp_turnouts.append([])
                current_pos = turnout[-1][-1]
                tmp_turnouts[-1].append(current_pos)
                turnout[-1].pop()
            else:
                passed_pos[str_current_pos(current_pos)] = True
                tmp_turnouts.pop()
                tmp_turnouts.pop()
                tmp_turnouts.append([])
                turnout.pop()
                current_pos = turnout[-1][-1]
                tmp_turnouts[-1].append(current_pos)
                


def look_around(current_pos, passed_pos):
    pos_row, pos_column = map(int, str_current_pos(current_pos).split(","))
    ways = [
        [pos_row, pos_column + 1],
        [pos_row, pos_column - 1],
        [pos_row + 1, pos_column],
        [pos_row - 1, pos_column]
    ]
    ways = [way for way in ways if 0 <= way[0] <= maze_len[0] - 1 and 0 <= way[1] <= maze_len[1] - 1]
    avaliable_ways = [way for way in ways if maze[way[0]][way[1]] == 0 and not passed_pos.get(f"{way[0]},{way[1]}", False)]
    return avaliable_ways


def str_current_pos(current_pos):
    return ",".join(list(map(str, current_pos))) if type(current_pos) == list else current_pos


print(find_exit())

# TODO: make the code find optimal path , not just the first path it finds and return it
