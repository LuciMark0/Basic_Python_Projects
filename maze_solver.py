maze = [[0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 1, 0, 0, 1],
        [0, 1, 0, 1, 0],
        [0, 0, 0, 0, 0]]
maze_len = [len(maze), len(maze[0])]
finish_pos = (0,4)


def find_exit():
  current_pos=input("enter start point row,column: ")
  passed_pos = {}
  true_path = [current_pos]
  turnout = []
  while True:
    if tuple(current_pos) == finish_pos:
      passed_pos[str_current_pos(current_pos)] = True
      return passed_pos.keys()
    avaliable_ways = look_around(current_pos, passed_pos)
    if len(avaliable_ways) > 1:
      passed_pos[str_current_pos(current_pos)] = True
      current_pos = avaliable_ways[-1]
      turnout.append(avaliable_ways[:-1]) 
    elif len(avaliable_ways) == 1:
      passed_pos[str_current_pos(current_pos)] = True
      current_pos = avaliable_ways[0]
      true_path.append(current_pos)
    else:
      if len(turnout[-1]) > 1:
        current_pos = turnout[-1][-1]
        turnout[-1].pop()
      else:
        passed_pos[str_current_pos(current_pos)] = True
        current_pos = turnout[-1][-1]
        turnout.pop()


def look_around(current_pos, passed_pos):
    pos_row, pos_column = map(int,str_current_pos(current_pos).split(","))

    ways = [[pos_row, pos_column + 1], [pos_row, pos_column - 1], [pos_row + 1, pos_column], [pos_row - 1, pos_column]]
    for way in list(ways):
        if way[0] < 0 or way[0] > maze_len[0]-1 or way[1] < 0 or way[1] > maze_len[1]-1:
            ways.remove(way)
    
    avaliable_ways = []
    for way in ways:
       if maze[way[0]][way[1]] == 0 and not passed_pos.get(str_current_pos(current_pos), False):
            avaliable_ways.append(way)
    return avaliable_ways


def str_current_pos(current_pos):
    return ",".join(list(map(str,current_pos))) if type(current_pos) == list else current_pos


print(find_exit())

# TODO: make the true path to be just contains path that start to finish directly
#       make the code find optimal path , not just the first path it finds and return it
#       make the code more readable