#! /usr/bin/env python3
# coding: utf-8


class Angus():
    def __init__(self, position, map):
        self.map = map
        self.position = position
        self.tile = "M"
        self.ether = False
        self.needle = False

    #     self.visible = True

    # def hide(self):
    #     self.visible = False
    #     self.map.hide(self.position)

    def up(self):
        if self.map.is_move_possible(self.position, "UP"):
            (x_coord, y_coord) = self.position
            new_position = (x_coord, y_coord - 1)
            self.map.move(self.tile, self.position, new_position)
            self.position = new_position

    def down(self):
        if self.map.is_move_possible(self.position, "DOWN"):
            (x_coord, y_coord) = self.position
            new_position = (x_coord, y_coord + 1)
            self.map.move(self.tile, self.position, new_position)
            self.position = new_position

    def left(self):
        if self.map.is_move_possible(self.position, "LEFT"):
            (x_coord, y_coord) = self.position
            new_position = (x_coord - 1, y_coord)
            self.map.move(self.tile, self.position, new_position)
            self.position = new_position

    def right(self):
        if self.map.is_move_possible(self.position, "RIGHT"):
            (x_coord, y_coord) = self.position
            new_position = (x_coord + 1, y_coord)
            self.map.move(self.tile, self.position, new_position)
            self.position = new_position


if __name__ == "__main__":
    pass
