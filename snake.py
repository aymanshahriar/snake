from collections import deque
from direction import Direction

class Snake:
    '''
    Variables: list of coordinates of the snake (ordered by start of snake to end), 

    Methods: get length (returns the number of coordinates of the snake), expand (add a new coordinate to the snake),
    move up, down left, right (removes the last coordinate and add a new coordiante).

    '''

    def __init__(self, starting_coord):
        self.coordinates = deque([starting_coord])  # instance variable
        self.direction = None

    def get_length(self):
        return len(self.coordinates)

    def expand(self, new_direction):
        if self.direction and self.direction.is_opposite(new_direction):
            return
        
        x_offset, y_offset = new_direction.value
        head_x, head_y = self.coordinates[-1]

        new_coord = (head_x + x_offset, head_y + y_offset)
        self.coordinates.append(new_coord)
        self.direction = new_direction

    def move(self, new_direction):
        if self.direction and self.direction.is_opposite(new_direction):
            return
        self.expand(new_direction)
        self.coordinates.popleft()
    