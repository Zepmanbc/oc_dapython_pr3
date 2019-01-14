#! /usr/bin/env python3
# coding: utf-8

"""Angus class contains the MacGyver's position and inventory."""

class Angus:
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
        self.tile = "M"
        self.ether = False
        self.needle = False
        self.tube = False

    def move(self, direction):
        """Try if the movement is possible.

        Args:
            direction (str): name the direction ["UP, "DOWN", "LEFT", "RIGHT"]
        """
        # self.map = map
        origin = self.map.macgyver
        change = self.MOVES[direction]
        # addition of the 2 tuples
        new_position = tuple([sum(x) for x in zip(*[origin, change])])
        if self.map.is_move_possible(new_position):
            self.map.move(self.tile, self.map.macgyver, new_position)

    def is_inventory_full(self):
        """Return True if MacGyver have all items."""
        if (self.ether and self.needle and self.tube):
            return True
        else:
            return False

if __name__ == "__main__":
    pass
