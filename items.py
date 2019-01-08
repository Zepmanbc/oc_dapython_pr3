"""Angus class contains the MacGyver's position and inventory."""

#! /usr/bin/env python3
# coding: utf-8


class Angus(): 
    """Get MacGyver's position from the map object and set the invetory."""

    MOVES = {
        "UP": (0, -1),
        "DOWN": (0, 1),
        "LEFT": (-1, 0),
        "RIGHT": (1, 0)
    }

    def __init__(self, map):
        """Set variables of position and inventory."""
        self.map = map
        self.position = self.map.macgyver
        self.tile = "M"
        self.ether = False
        self.needle = False

    def move(self, direction):
        """Try if the movement is possible.

        If so, caclculate the new position, 
        set it and modify the map table.
        """
        origin = self.position
        change = self.MOVES[direction]
        # addition of the 2 tuples
        new_position = tuple([sum(x) for x in zip(*[origin, change])])
        if self.map.is_move_possible(new_position):
            self.map.move(self.tile, self.position, new_position)
            self.position = new_position


if __name__ == "__main__":
    pass
