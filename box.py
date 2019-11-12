# coding=UTF-8

import pytest
import sys


def drawBox(w, h):
    # Checks if w and h are positive and raises an exception if they are not
    if w < 0 or h < 0:
        raise Exception("The width and height of a box must be a positive number")
    # rounds any decimal or float numbers down to nearest integer
    w = int(w)
    h = int(h)
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


# Tests if the right sequence of letters are printed to the terminal
def test_characters(capsys):
    drawBox(2, 3)
    out, err = capsys.readouterr()
    assert u"\n\u231C\u231D\n||\n\u231E\u231F" in out


# tests if drawing a large rectangle produces the expected length of output (w*h+h)
def test_draw_large_rectangle(capsys):
    drawBox(5000, 1000)
    out, err = capsys.readouterr()
    assert len(out) == 5001000


# tests if drawing a large square produces the expected length of output
def test_draw_large_square(capsys):
    drawBox(1000, 1000)
    out, err = capsys.readouterr()
    assert len(out) == 1001000


# tests if passing negative arguments raises an exception
def test_draw_negative_square():
    with pytest.raises(Exception):
        assert drawBox(-5, -5)


# tests if drawing a rectangle with a decimal width produces the expected length of output
def test_decimal_width(capsys):
    drawBox(5.6, 40)
    out, err = capsys.readouterr()
    assert len(out) == 240


# tests if drawing a rectangle with a decimal height produces the expected length of output
def test_decimal_height(capsys):
    drawBox(70, 4.976)
    out, err = capsys.readouterr()
    assert len(out) == 284


# tests if drawing a rectangle with a greater width produces the expected length of output
def test_greater_width(capsys):
    drawBox(80, 6)
    out, err = capsys.readouterr()
    assert len(out) == 486


# tests if drawing a rectangle with a greater height produces the expected length of output
def test_greater_height(capsys):
    drawBox(6, 80)
    out, err = capsys.readouterr()
    assert len(out) == 560
