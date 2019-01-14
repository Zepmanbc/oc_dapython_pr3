#! /usr/bin/env python3
# coding: utf-8

"""Class that generate the map and get the position of each items."""

import os
from random import choice


class Map:
    """Generate the map object."""

    def __init__(self):
        """Init the map object."""
        # Read the map file
        self.map = list()
        f = open("map", "r")
        for line in f:
            self.map.append(line[:-1])
        # creation position for every items
        self.macgyver = self._get_position("M")
        self.guardian = self._get_position("G")
        self.exit = self._get_position("S")
        self.needle = self._random_position("N")
        self.ether = self._random_position("E")
        self.tube = self._random_position("T")

    def _get_position(self, ref_tile):
        """Read each coordinates of self.map to get the tile coordinates.

        Args:
            ref_tile (str): a letter for each sprite

        Returns:
            tuple: (x_coord, y_coord)

        """
        x_coord, y_coord = 0, 0
        for line in self.map:
            for tile in line:
                if tile == ref_tile:
                    return (x_coord, y_coord)
                x_coord += 1
            x_coord = 0
            y_coord += 1
        return False

    def _set_position(self, tile, position):
        """Modify the tile at position in self.map.
        
        Args:
            tile (str): sprite letter.
            position (tuple): (X, y) coordinates.
        """
        (x_coord, y_coord) = position
        row = list(self.map[y_coord])
        row[x_coord] = tile
        self.map[y_coord] = "".join(row)

    def _get_tile(self, position):
        """Return tile type at coordinates in self.map.
        
        Args:
            position (tuple): (x, y) coordinates.
        """
        (x_coord, y_coord) = position
        return self.map[y_coord][x_coord]

    def _random_position(self, tile):
        """Return a free (floor) random position in self.map.
        
        Set the item letter in map
        
        Args:
            tile (str): sprite letter.
        
        Returns:
            position (tuple): (x, y) coordinates.
        
        """
        random_list = [x for x in range(0, 15)]
        while 1:
            position = (choice(random_list), choice(random_list))
            if self._get_tile(position) == '_':
                self._set_position(tile, position)
                return position
                # break

    def is_move_possible(self, new_position):
        """Test if the move is ok.
        
        Args:
            new_position (tuple): (x, y) coordinates

        Returns:
            boolean
            
        """
        (x_coord, y_coord) = new_position
        # Verify if not out of screen
        if not (0 <= x_coord <= 14 and 0 <= y_coord <= 14):
            return False
        # Get type of tile
        if self._get_tile(new_position) == "#":
            return False
        # all seems to be good
        return True

    def hide(self, position):
        """Set the position as a floor tile.
        
        Args:
            position (tuple): (x, y) coordinates
        """
        self._set_position("_", position)

    def move(self, tile, last_pos, new_pos):
        """Hide previous position and set the tile to new position.
        
        Args:
            tile (str): a letter that define the kind of sprite
            las_pos (tuple): (x, y) coordinates (current)
            new_pos (tuple): (x, y) coordinates (next)
        """
        self.hide(last_pos)
        self._set_position(tile, new_pos)
        if tile == "M":
            self.macgyver = new_pos

# if __name__ == "__main__":
#     map = Map()
#     print(map.map)
#     print(map.macgyver)
#     print(map.guardian)
#     print(map.exit)
#     print(map.needle)
#     print(map.ether)

#     map.move("M", (0, 2), (0, 1))
#     print(map.map)
#     print(map.macgyver)
