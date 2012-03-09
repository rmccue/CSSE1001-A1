"""
CSSE1001 - Assignment 1

Student Name: Ryan McCue
Student Number: xxxxxxxx

----

Copyright (c) 2012 Ryan McCue <me@ryanmccue.info>

This software will be available from
https://github.com/rmccue/CSSE1001-A1 from 2012-04-07. Please avoid
distributing until that time.

Permission to use, copy, modify, and/or distribute this software for any
purpose with or without fee is hereby granted, provided that the above
copyright notice and this permission notice appear in all copies.

THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY
SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER
RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT,
NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION WITH THE
USE OR PERFORMANCE OF THIS SOFTWARE.

"""

# Help text
HELP = """? - Help.
N - move North one square.
S - move South one square.
E - move East one square.
W - move West one square.
R - Reset to the beginning.
B - Back up a move.
L - List all possible legal directions from the current position.
Q - Quit.
"""

# Valid commands
COMMANDS = ('?', 'N', 'S', 'E', 'W', 'R', 'B', 'L', 'Q')

def load_maze(filename):
	"""
	Load a maze map from filename into a list of rows, which are a
	list of cells, which have values 'X' for a invalid move, 'O' for a
	valid move, and 'F' for the finish point. All other values are
	considered to be invalid moves, except for leading and
	trailing whitespace.
	"""

	# This is a horrible function, as all it does is split the string
	# This means that the data is in maze[y][x] which makes zero sense
	# and makes everything so much more confusing later.
	#
	# In addition, the order/position of these actually matters, so
	# we should be using tuples here instead.
	#
	# My last issue with this is that we don't really gain much.
	# Instead of this, we should be using better values than 'X', 'O'
	# and 'F', as that's really mapping data, not data we want.
	#
	# But I digress.

	file = open(filename, 'rU')
	maze = []
	for line in file:
		# Strip leading/trailing whitespace
		line = line.strip()

		# Ignore blank lines
		if len(line) < 1:
			pass

		row = []
		for char in line:
			row.append(char)
		maze.append(row)
	return maze

def get_position_in_direction(position, direction):
	"""
	Turn a relative direction into an absolute direction from a position and
	return the new position as a tuple of (pos_row, pos_col)
	"""
	# position is (y, x)
	# Again, backwards, see load_maze
	direction = direction.upper()

	if direction == 'N':
		return (position[0] - 1, position[1])

	if direction == 'S':
		return (position[0] + 1, position[1])

	if direction == 'E':
		return (position[0], position[1] + 1)

	if direction == 'W':
		return (position[0], position[1] - 1)

	raise ValueError('direction must be one of N, S, E, W')

def move(maze, position, direction):
	"""
	Move from current position in a direction in a maze and returns
	information on the move as a tuple of
	(can_user_move_to_position, is_position_finish, (pos_row, pos_col))
	"""
	can_move = False
	is_finished = False

	new_position = get_position_in_direction(position, direction)

	# Make sure they can't move outside the boundaries
	if new_position[0] < 0 or new_position[1] < 0 \
		or new_position[0] >= len(maze) \
		or new_position[1] >= len(maze[ new_position[0] ]):
			return (False, False, position)

	# This is backwards, see load_maze for why
	pos_type = maze[ new_position[0] ][ new_position[1] ]

	# Do we have an open space?
	if pos_type == 'O':
		can_move = True

	# OK, is it the finish then?
	elif pos_type == 'F':
		can_move = True
		is_finished = True

	# All other characters are an invalid move
	else:
		new_position = position

	return (can_move, is_finished, new_position)

def get_legal_directions(maze, position):
	"""
	Find all legal moves for the player from their current position
	and return as a list.
	"""
	return [dir for dir in ['N', 'S', 'E', 'W'] \
		if move(maze, position, dir)[0]]

def is_valid_command(command):
	"""
	Check whether command is valid.
	"""
	return command in COMMANDS

def interact():
	"""
	Main interaction loop. Uses a text-based interface via the interpreter.
	"""
	position = (1, 1)
	history = []
	maze = []

	try:
		filename = raw_input("Maze File: ").strip()
		maze = load_maze(filename)

		while True:
			print "You are at position ({0}, {1})".format(position[0], position[1])

			command = raw_input("Command: ").strip().upper()

			if not is_valid_command(command):
				print "Invalid Command: {0}".format(command)
				continue

			# Meta commands
			if command == '?':
				print HELP
				continue

			if command == 'Q':
				confirm = raw_input("Are you sure you want to quit? [y] or n: ")
				if confirm.strip().lower() != "n":
					break
				continue

			# History commands
			if command == 'R':
				position = (1, 1)
				continue

			if command == 'B':
				try:
					position = history.pop()
				except IndexError:
					position = (1, 1)
				continue

			# Map
			if command == 'L':
				print ','.join(get_legal_directions(maze, position))
				continue

			# Movement
			if command not in ['N', 'S', 'E', 'W']:
				print "Invalid Command: {0}".format(command)

			result = move(maze, position, command)

			# Check validity
			if not result[0]:
				print "You can't go in that direction"
				continue

			# Check if it's the finish
			if result[1]:
				print "Congratulations - you made it!"
				break

			# Normal move, add previous to history
			history.append(position)
			position = result[2]
	except KeyboardInterrupt:
		pass

# Only run main loop if not imported
if __name__ == '__main__':
	interact()