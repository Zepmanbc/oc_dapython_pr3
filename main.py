#! /usr/bin/env python3
# coding: utf-8
import pygame

from gui import Display
from map import Map


def main():
    window = pygame.display.set_mode((300, 300))
    map = Map()
    screen = Display(window, map.map)
    loop = True
    while loop:
        for event in pygame.event.get():
            if event.type == 12:  # pygame.QUIT:
                loop = False

        pygame.display.flip()

if __name__ == "__main__":
    main()
