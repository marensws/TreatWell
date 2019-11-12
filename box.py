# coding=UTF-8

import sys


def drawBox(w, h):
    # creates a table row by row, with a XY-axis with origin in the bottom right corner.
    # each coordinate is matched with a character depending on its position relative to the extreme points of the table
    for y in reversed(range(h)):
        # a list of strings representing the characters on each row
        row = []
        for x in range(w):
            # first row of the table
            if y == h-1:
                # for a coordinate (0, h-1) the character '⌜' is appended to the row list
                if x == 0:
                    row.append(u'\u231C')
                # for a coordinate(w-1, h - 1) the character '⌝' is appended to the row list
                elif x == w-1:
                    row.append(u'\u231D')
                # for coordinates between the top corners '-' is appended to the row list
                elif x >0:
                    row.append('-')
            # leftmost column of the table
            elif x == 0:
                # for a coordinate (0, 0) the character '⌞' is appended to the row list
                if y == 0:
                    row.append(u'\u231E')
                # for coordinates on the leftmost column between the corners '|' is appended to the row list
                elif y > 0:
                    row.append('|')
            # rightmost column of the table
            elif x == w-1:
                # for a coordinate (w-1, 0) the character '⌟' is appended to the row list
                if y == 0:
                    row.append(u'\u231F')
                # for coordinates on the rightmost column between the corners '|' is appended to the row list
                elif y > 0:
                    row.append('|')
            # bottom row of the table
            elif y == 0:
                # for coordinates between the bottom corners '-' is appended to the row list
                if x > 0:
                    row.append('-')
            # coordinates who are not on the edge of the table ' ' is appended to the row list
            else:
                row.append(' ')
        # After going through each row, the row list is printed to the terminal
        print('')
        for i in row:
            sys.stdout.write(i)

