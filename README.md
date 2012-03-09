# CSSE1001 Assignment 1
This is Assignment 1 for CSSE1001 at UQ, for Semester 1 2012, by
[Ryan McCue](http://ryanmccue.info/).

This repository should be made available from
https://github.com/rmccue/CSSE1001-A1 from 2012-04-07. Please avoid
distributing until that time.


## Note for Fellow Students

This project is being put online as I feel that others may be able to
learn from it. It is not made public simply to be plagiarised for your
course, and as I retain copyright, if you remove the copyright notice,
you will be infringing on my copyright. You're perfectly fine to use
and modify it with my copyright notice left intact, but I doubt that
your marker will be very happy about that.


## Usage

	$ python assign1.py
	Maze File:

Follow the onscreen prompts. For help, use ?. The "Maze File:" prompt
expects a filename (and possibly path) to a maze-layout file.

It can also be used as a module:

	$ python
	>>> import assign1
	>>> assign1.interact() # Start the main loop

This can also be used to inspect the functions in the module.

You can quit the game in two ways: either use the `q` command and
answer `y` to quit, or simply use Ctrl-C to quit.


## Maze Layout Format

The Maze Layout Format (MLF) follows the specification laid out in the
assignment document. It is a simple text-based format, and describes a
grid of points.

The following values are defined:

* `X` represents an invalid position (such as a wall)
* `O` represents a valid position (a pathway)
* `F` represents the end(s) of the maze

Any other values are treated as invalid positions (i.e. are synonymous
with an `X` value), however, leading and trailing whitespace is
stripped, and blank lines are ignored. The edges of the layout (i.e.
before the first character and after the last character) are also
taken to be invalid positions, so you can avoid creating a border if
you'd prefer.

The starting position of the maze is always at (1, 1), so the minimum
valid maze is:

	XX
	XO

Of course, it's probably a good idea to also include a finish point to
allow a player to actually interact with it.


## License

Copyright (c) 2012 Ryan McCue <me@ryanmccue.info>

This software will be available from
https://github.com/rmccue/CSSE1001 from 2012-04-07. Please avoid
distributing until that time.

Permission to use, copy, modify, and/or distribute this software for
any purpose with or without fee is hereby granted, provided that the
above copyright notice and this permission notice appear in
all copies.

THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL
WARRANTIES WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE
AUTHOR BE LIABLE FOR ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL
DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR
PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR OTHER
TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR
PERFORMANCE OF THIS SOFTWARE.