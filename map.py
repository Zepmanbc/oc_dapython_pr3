#! /usr/bin/env python3
# coding: utf-8
import os
from random import choice


class Map():
    def __init__(self):
        # Read map file
        self.map = list()
        f = open("map", "r")
        for line in f:
            self.map.append(line[:-1])
        # creation position for every items
        self.macgyver = self.__get_position("M")
        self.guardian = self.__get_position("G")
        self.exit = self.__get_position("S")
        self.needle = self.__random_position("N")
        self.ether = self.__random_position("E")

    def __get_position(self, ref_tile):
        "Read each coordinates of self.map to get the tile coordinates"
        x_coord, y_coord = 0, 0
        for line in self.map:
            for tile in line:
                if tile == ref_tile:
                    return (x_coord, y_coord)
                x_coord += 1
            x_coord = 0
            y_coord += 1
        return False

    def __set_position(self, tile, position):
        "modify the tile at position in self.map"
        (x_coord, y_coord) = position
        row = list(self.map[y_coord])
        row[x_coord] = tile
        self.map[y_coord] = "".join(row)

    def __get_tile(self, position):
        "return tile type at coordinates in self.map"
        (x_coord, y_coord) = position
        return self.map[y_coord][x_coord]

    def __random_position(self, tile):
        "test a random position in self.map if it is floor"
        random_list = [x for x in range(0, 15)]
        while 1:
            position = (choice(random_list), choice(random_list))
            if self.__get_tile(position) == '_':
                self.__set_position(tile, position)
                return position
                # break

    def is_move_possible(self, new_position):
        "Test if the move is ok"
        (x_coord, y_coord) = new_position
        # Verify if not out of screen
        if not (0 <= x_coord <= 14 and 0 <= y_coord <= 14):
            return False
        # Get type of tile
        if self.__get_tile(new_position) == "#":
            return False
        # all seems to be good
        return True

    def hide(self, position):
        "Set the position as a floor tile"
        self.__set_position("_", position)

    def move(self, tile, last_pos, new_pos):
        "Hide previous position and set the tile to new position"
        self.hide(last_pos)
        self.__set_position(tile, new_pos)

if __name__ == "__main__":
    map = Map()
    print(map.map)
    print(map.macgyver)
    print(map.guardian)
    print(map.exit)
    print(map.needle)
    print(map.ether)

    map.move("M", (0, 2), (0, 1))
    print(map.map)
    print(map.macgyver)
