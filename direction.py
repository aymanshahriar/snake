from enum import Enum

# each direction corresponds to the change in the x coordinate and y coordinate
class Direction(Enum):
    LEFT = (-1, 0)
    RIGHT = (1, 0)
    UP = (0, -1)
    DOWN = (0, 1)

    def is_opposite(self, other: Enum):
        return {self, other} in ({Direction.LEFT, Direction.RIGHT}, {Direction.UP, Direction.DOWN})

