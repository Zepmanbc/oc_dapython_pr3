#! /usr/bin/env python3
# coding: utf-8
import pygame
from spritesheet import Spritesheet


class Display():
    STEP = 20
    TILES = "ressource/floor-tiles-20x20.png"
    FLOOR = (1 * STEP, 0 * STEP, STEP, STEP)
    WALL = (12 * STEP, 5 * STEP, STEP, STEP)
    EXIT = (8 * STEP, 1 * STEP, STEP, STEP)
    MACGYVER = "ressource/MacGyver.png"
    GUARDIAN = "ressource/Gardien.png"
    NEEDLE = "ressource/seringue.png"
    ETHER = "ressource/ether.png"
    WIN = "ressource/win.png"
    LOOSE = "ressource/loose.png"

    def __init__(self, window, map):
        self.window = window
        self.init_pictures()
        self.map = map
        self.refresh_screen()

    def refresh_screen(self):
        "Read the map and set every tile in the window"
        switcher = {
                '#': self.wall,
                '_': self.floor,
                'S': self.exit,
                'M': self.macgyver,
                'G': self.guardian,
                'N': self.needle,
                'E': self.ether
            }
        x_coord, y_coord = 0, 0
        # for line in map:
        for line in self.map:
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
        pygame.display.flip()

    def stop(self, message):
        if message == "WIN":
            stop_pic = self.WIN
        else:
            stop_pic = self.LOOSE
        pic = pygame.image.load(stop_pic)
        self.window.blit(pic, (0, 0))
        pygame.display.flip()

    def init_pictures(self):
        "Set every picture to the right area or size"
        ss = Spritesheet(self.TILES)
        self.wall = ss.image_at(self.WALL)
        self.floor = ss.image_at(self.FLOOR)
        self.exit = ss.image_at(self.EXIT)
        self.macgyver = self.__resize_pic(self.MACGYVER)
        self.guardian = self.__resize_pic(self.GUARDIAN)
        self.needle = self.__resize_pic(self.NEEDLE)
        self.ether = self.__resize_pic(self.ETHER)

    def __resize_pic(self, path):
        "resize a picture to the tile size"
        pic = pygame.image.load(path)
        pic.set_alpha(128)  # for keeping transparency
        return pygame.transform.scale(pic, (self.STEP, self.STEP))


if __name__ == "__main__":
    window = pygame.display.set_mode((300, 300))
    from map import Map
    map = Map()
    screen = Display(window, map.map)
    loop = True
    while loop:
        for event in pygame.event.get():
            if event.type == 12:  # pygame.QUIT:
                loop = False
