import os
import time
from math import floor, sin, cos, pi

# This is the Canvas class. It defines some height and width, and a 
# matrix of characters to keep track of where the TerminalScribes are moving
class Canvas:
    def __init__(self, width, height):
        self._x = width
        self._y = height
        """This is a grid that contains data about where 
        the TerminalScribes have visited"""
        self._canvas = [[' ' for y in range(self._y)] for x in range(self._x)]
    def hits_Vertical_Wall(self, point):
        return round(point[0]) < 0 or round(point[0]) >= self._x

    def hits_Horizontal_Wall(self, point):
        return round(point[1]) < 0 or round(point[1]) >= self._y

    def hit_the_wall(self, point):
        return self.hits_Vertical_Wall(point) or self.hits_Horizontal_Wall(point)

    def get_Reflection(self, point):
        return [-1 if self.hits_Vertical_Wall(point) else 1, -1 if self.hits_Horizontal_Wall(point) else 1]
    # Set the given position to the provided character on the canvas
    def setPos(self, pos, mark):
        self._canvas[pos[0]][pos[1]] = mark

    # Clear the terminal (used to create animation)
    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    # Clear the terminal and then print each line in the canvas
    def print(self):
        self.clear()
        for y in range(self._y):
            print(' '.join([col[y] for col in self._canvas]))

class TerminalScribe:
    def __init__(self, canvas, bounce = False):
        self.canvas = canvas
        self.bounce = bounce
        self.trail = '.'
        self.mark = '.'
        self.framerate = 0.001
        self.pos = [0, 0]
        self.pos_with_angle = [0, 0]

    def set_start_point(self, pos = [0, 0]):
        self.pos = pos
    
    def right(self, times):
        for _ in range(times):
            new_pos = [self.pos[0] + 1, self.pos[1]]
            self.draw(new_pos)

    def left(self, times):
        for _ in range(times):
            new_pos = [self.pos[0] - 1, self.pos[1]]
            self.draw(new_pos)

    def up(self, times):
        for _ in range(times):
            new_pos = [self.pos[0], self.pos[1] - 1]
            self.draw(new_pos)
    
    def down(self, times):
        for _ in range(times):
            new_pos = [self.pos[0], self.pos[1] + 1]
            self.draw(new_pos)

    def set_spesific_point(self, pos, char = None):
        if not char:
            return self.draw(pos)

        self.canvas.setPos(pos, char)
        self.canvas.print()
        time.sleep(self.framerate)

    def fix_last_mark(self):
        self.set_spesific_point(self.pos, self.trail)

    def move_with_angle(self, angle, times):
        changeReflected = [1, 1]  # Initialize outside the loop
        if angle < 0 or angle > 360:
            raise Exception("Angle must be between 0 and 360")
        for _ in range(times):
            if self.canvas.hit_the_wall(self.pos) and self.bounce:
                changeReflected = list(map(lambda x,y: x*y,changeReflected,self.canvas.get_Reflection(self.pos)))
            self.pos_with_angle = sum_two_list(self.pos_with_angle, [sin(angle/180*pi)*changeReflected[0],
                                                                    -cos(angle/180*pi)*changeReflected[1]]) 
            self.pos = [round(self.pos_with_angle[0]), round(self.pos_with_angle[1])]
            self.draw(self.pos)
            time.sleep(self.framerate)        
    
    def draw(self, pos):
        if not self.canvas.hit_the_wall(pos):
            
            # Set the old position to the "trail" symbol
            self.canvas.setPos(self.pos, self.trail)
            # Update position
            self.pos = pos
            # Set the new position to the "mark" symbol
            self.canvas.setPos(self.pos, self.mark)
            # Print everything to the screen
            self.canvas.print()
            # Sleep for a little bit to create the animation
            time.sleep(self.framerate)
    

    def draw_square(self, size):
        ways = [self.right, self.down, self.left, self.up]
        for way in ways:
            way(size)
        self.fix_last_mark()
    
    
    def draw_cube(self, size):
        self.draw_square(size)
        pos_z_len = floor(size/2)
        scribe.set_start_point(list(map(lambda x,y: x+y, self.pos, [pos_z_len, pos_z_len])))
        self.draw_square(size)

        edges = {
            "left-up":[self.pos[0], self.pos[1]],
            "left-down":[self.pos[0], self.pos[1]+size],
            "right-up":[self.pos[0]+size, self.pos[1]],
            "right-down":[self.pos[0]+size, self.pos[1]+size]
        }
        edge_minus = -1
        for _ in range(pos_z_len-1):
            for key,edge in dict(edges).items():
                self.set_spesific_point(sum_two_list(edge, [edge_minus, edge_minus]), ".")
                edges[key] = sum_two_list(edge, [edge_minus, edge_minus])

def sum_two_list(list1, list2):
        return list(map(lambda x,y: x+y, list1, list2))

canvas = Canvas(20, 20)
scribe = TerminalScribe(canvas, bounce=True)

scribe.move_with_angle(165, 120)

# scribe.draw_cube(8)
