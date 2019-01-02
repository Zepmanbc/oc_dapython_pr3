#! /usr/bin/env python3
# coding: utf-8
import os

import pygame
from spritesheet import Spritesheet


class Screen():
    STEP = 20
    TILES = "ressource/floor-tiles-20x20.png"
    FLOOR = (1 * STEP, 0 * STEP, STEP, STEP)
    WALL = (12 * STEP, 5 * STEP, STEP, STEP)
    EXIT = (8 * STEP, 1 * STEP, STEP, STEP)
    MACGYVER = "ressource/MacGyver.png"
    GUARDIAN = "ressource/Gardien.png"
    NEEDLE = "ressource/seringue.png"
    ETHER = "ressource/ether.png"

    def __init__(self):
        self.window = pygame.display.set_mode((300, 300))
        self.init_pictures()
        map = self.read_map()
        self.refresh_screen(map)
        print("ok")

    def read_map(self):
        map = list()
        f = open("map", "r")
        for line in f:
            map.append(line[:-1])
        return map

    def refresh_screen(self, table):
        switcher = {
                '#': self.wall,
                '_': self.floor,
                'S': self.exit,
                'M': self.macgyver,
                'G': self.guardian,
            }
        x_coord, y_coord = 0, 0
        for line in table:
            for tile in line:
                pic = switcher.get(tile)
                if not pic:
                    raise Exception("'{}' is not a valid tile".format(tile))
                self.window.blit(self.floor, (x_coord, y_coord))
                self.window.blit(pic, (x_coord, y_coord))
                x_coord += self.STEP
            x_coord = 0
            y_coord += self.STEP

        pygame.display.flip()

    def init_pictures(self):
        ss = Spritesheet(self.TILES)
        self.wall = ss.image_at(self.WALL)
        self.floor = ss.image_at(self.FLOOR)
        self.exit = ss.image_at(self.EXIT)
        self.macgyver = self.__resize_pic(self.MACGYVER)
        self.guardian = self.__resize_pic(self.GUARDIAN)
        self.needle = self.__resize_pic(self.NEEDLE)
        self.ether = self.__resize_pic(self.ETHER)

    def __resize_pic(self, pic):
        temp_pic = pygame.image.load(pic)
        temp_pic.set_alpha(128)
        return pygame.transform.scale(temp_pic, (self.STEP, self.STEP))


if __name__ == "__main__":
    screen = Screen()
    loop = True
    while loop:
        for event in pygame.event.get():
            if event.type == 12:  # pygame.QUIT:
                loop = False
