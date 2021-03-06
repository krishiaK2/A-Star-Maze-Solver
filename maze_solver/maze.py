
class Maze():
    """
    This is a representation of a maze
    """
    # Maze representation
    maze = [[]]

    # Maze tile values
    TILE_TYPES = []

    def set_maze_size(self, length, width):
        """
        Accepts length and width and initializes maze
        to given size.
        """
        # TODO
        pass

    def get_tile(self, x, y):
        """
        Accepts coordinates and returns the specified
        tile in the maze.
        """
        return self.maze[x][y]

    def set_tile(self, x, y, value):
        """
        Accepts coordinates and a value and sets
        the value of the tile in the maze. Returns the
        value of the tile if set is successful. Throws
        an exception if value in invalid.
        """
        if self.value_is_valid(value):
            self.maze[x][y] = value
        else:
            # Throw error
            # TODO
            pass

        return self.maze[x][y]

    def value_is_valid(self, value):
        """
        Accepts a value and checks if value is a valid
        maze value.
        """
        # TODO
        pass

    def is_traversable(self, x, y):
        """
        Accepts coordinates and return if tile can
        be traversed or not.
        """
        # TODO
        pass


class WeightedMaze(Maze):
    weights = [[]]

    def get_weight(self, x, y):
        """
        Accepts coordinates and returns weight
        the tile in the maze.
        """
        return weights[x][y]

    def set_weight(self, x, y, value):
        """
        Accepts coordinates and a value and sets tile
        to weight value. Returns the value of the tile
        if set is successful.
        """
        self.weights[x][y] = value

        return self.weights[x][y]
