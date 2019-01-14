#! /usr/bin/env python3
# coding: utf-8

"""Display class of the MacGyver Maze."""

import os

import pygame

from spritesheet import Spritesheet


class Display:
    """This module display the GUI.

    It generate the positions and refresh the screen

    Exemple:
        screen = Display(window, map)

    Attributes:
        window is a pygame.display object
        map is an object that contains a list of the maze map and the position of items

    """

    STEP = 20
    TILES = os.path.join("ressource", "floor-tiles-20x20.png")
    FLOOR = (1 * STEP, 0 * STEP, STEP, STEP)
    WALL = (12 * STEP, 5 * STEP, STEP, STEP)
    EXIT = (8 * STEP, 1 * STEP, STEP, STEP)
    MACGYVER = os.path.join("ressource", "MacGyver.png")
    GUARDIAN = os.path.join("ressource", "Gardien.png")
    NEEDLE = os.path.join("ressource", "seringue.png")
    ETHER = os.path.join("ressource", "ether.png")
    TUBE = os.path.join("ressource", "tube_plastique.png")
    WIN = os.path.join("ressource", "win.png")
    LOOSE = os.path.join("ressource", "loose.png")
    INSTRUCTIONS = os.path.join("ressource", "instructions.png")

    def __init__(self, window, mappy):
        """Set the variables and run the first refresh."""
        self.window = window
        self._init_pictures()
        self.mappy = mappy
        self.message = "INSTRUCTIONS"
        self.refresh_screen()

    def refresh_screen(self):
        """Read the mappy and set every tile in the window."""
        switcher = {
            '#': self.wall,
            '_': self.floor,
            'S': self.exit,
            'M': self.macgyver,
            'G': self.guardian,
            'N': self.needle,
            'E': self.ether,
            'T': self.tube
        }
        x_coord, y_coord = 0, 0
        # for line in mappy:
        for line in self.mappy:
            for tile in line:
                # put a floor tile under every tile to use transparency tiles
                self.window.blit(self.floor, (x_coord, y_coord))
                # select the picture used for a tile
                pic = switcher.get(tile)
                if not pic:
                    raise Exception("'{}' is not a valid tile".format(tile))
                self.window.blit(pic, (x_coord, y_coord))
                x_coord += self.STEP
            x_coord = 0
            y_coord += self.STEP
        if self.message:
            self._display_message()
        pygame.display.flip()

    def _display_message(self):
        """Display an image on the screen.

        if self.message is not False set the image corresponding to value
        """
        if self.message == "WIN":
            message_pic = self.WIN
        elif self.message == "LOOSE":
            message_pic = self.LOOSE
        elif self.message == "INSTRUCTIONS":
            message_pic = self.INSTRUCTIONS
        pic = pygame.image.load(message_pic)
        self.window.blit(pic, (0, 0))

    def _init_pictures(self):
        """Load every picture in a variable."""
        _ss = Spritesheet(self.TILES)
        self.wall = _ss.image_at(self.WALL)
        self.floor = _ss.image_at(self.FLOOR)
        self.exit = _ss.image_at(self.EXIT)
        self.macgyver = self._resize_pic(self.MACGYVER)
        self.guardian = self._resize_pic(self.GUARDIAN)
        self.needle = self._resize_pic(self.NEEDLE)
        self.ether = self._resize_pic(self.ETHER)
        self.tube = self._resize_pic(self.TUBE)

    def _resize_pic(self, path):
        """Resize a picture to the tile size."""
        pic = pygame.image.load(path)
        pic.set_alpha(128)  # for keeping transparency
        return pygame.transform.scale(pic, (self.STEP, self.STEP))


# if __name__ == "__main__":
#     window = pygame.display.set_mode((300, 300))
#     from map import Map
#     map = Map()
#     screen = Display(window, map.map)
#     loop = True
#     while loop:
#         for event in pygame.event.get():
#             if event.type == 12:  # pygame.QUIT:
#                 loop = False
