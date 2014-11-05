import random

DIRT_SQUARE = 1


class VacuumTaskEnvironment(object):
    """
        Task Environment for Vacuum world, world is created with a 2x1 size
        and itiated to be clean. Dirt can be applied randomly with
        place_dirt_on_map_randomly or with place_dirt_on_square. Dirt can be
        removed with remove_dirt_on_square.
    """
    def __init__(self):
        self.set_lifetime(1000)
        self.set_dirt_amount(10)
        self.set_map_size(2, 1)

    def set_lifetime(self, number_of_steps):
        self.lifetime = number_of_steps

    def set_dirt_amount(self, number_of_dirt_squares):
        self.dirt = 10

    def set_map_size(self, map_width, map_height):
        self.width = map_width
        self.height = map_height
        self.area = self.width * self.height
        self.map = [[None for _ in xrange(self.width)] for _ in xrange(self.height)]

    def place_dirt_on_map_randomly(self):
        if self.dirt > self.area:
            self.map = [[DIRT_SQUARE] * self.width] * self.height
            return
        else:
            dirt_placed_on_map = 0
            while True:
                temp_height = random.randint(0, self.height - 1)
                temp_width = random.randint(0, self.width - 1)
                if self.map[temp_width][temp_height] is None:
                    dirt_placed_on_map = dirt_placed_on_map + 1
                    self.map[temp_width][temp_height] = DIRT_SQUARE
                if self.dirt == dirt_placed_on_map:
                    break

    def place_dirt_on_square(self, x_position, y_position):
        self.map[y_position][x_position] = DIRT_SQUARE

    def remove_dirt_on_square(self, x_position, y_position):
        self.map[y_position][x_position] = None
