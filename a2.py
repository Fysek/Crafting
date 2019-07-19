# Do not import any modules. If you do, the tester may reject your submission.

# Constants for the contents of the maze.

# The visual representation of a wall.
WALL = '#'

# The visual representation of a hallway.
HALL = '.'

# The visual representation of a brussels sprout.
SPROUT = '@'

# Constants for the directions. Use these to make Rats move.

# The left direction.
LEFT = -1

# The right direction.
RIGHT = 1

# No change in direction.
NO_CHANGE = 0

# The up direction.
UP = -1

# The down direction.
DOWN = 1

# The letters for rat_1 and rat_2 in the maze.
RAT_1_CHAR = 'J'
RAT_2_CHAR = 'P'


class Rat:
    """ A rat caught in a maze. """
    # Write your Rat methods here.
	
	def __init__(self, symbol, row, col):
	"""(Rat, str, int, int) -> NoneType
	symbol: the 1-character symbol for the rat
	row: the row where the rat is located
	col: the column where the rat is located
	num_sprouts_eaten: the number of sprouts that this rat has eaten, which is initially 0.
	"""
		self.symbol = symbol
		self.row = row
		self.col = col
		self.num_sprouts_eaten = 0
	
	def set_location(self, row, col):
	"""(Rat, int, int) -> NoneType
	"""
		self.row = row
		self.col = col
	
	def eat_sprout(self):
	"""(Rat) -> NoneType
	"""
		self.num_sprouts_eaten += 1
	
	def __str__(self):
	"""(Rat) -> str
	’J at(4,3)ate 2 sprouts.’ no new line
	"""	
		s = "{0} at ({1}, {2}) ate {3} sprouts.".format(self.symbol,self.row,self.col,self.num_sprouts_eaten)
        return s
	
class Maze:
    """ A 2D maze. """

    # Write your Maze methods here.
	def __init__(self, ):
	"""(Maze, list of list of str, Rat, Rat) -> NoneType
    """
	
	def is_wall:
	"""(Maze, int, int) -> bool
    """
	
	def get_character:
	"""(Maze, int, int) -> str
	"""
	
	def move:
	"""(Maze, Rat, int, int) ->bool
	"""
	
	def __str__:
	"""(Maze) -> str
	"""
	
	