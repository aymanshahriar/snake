import random

class Point:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.x = 0
        self.y = 0
        self.generate_new_coordinate()

    def generate_new_coordinate(self):
        self.x = random.randint(0, self.width-1)
        self.y = random.randint(0, self.height-1)
        