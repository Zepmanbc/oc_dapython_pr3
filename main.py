#! /usr/bin/env python3
# coding: utf-8

"""Main file of the MacGyver game."""

import pygame
from pygame.locals import K_UP, K_DOWN, K_LEFT, K_RIGHT

from map import Map
from gui import Display
from items import Angus


def main():
    """Run the main part."""
    window = pygame.display.set_mode((300, 300))
    pygame.display.set_caption("MacGyver vs G")
    map = Map()
    screen = Display(window, map.map)

    # create player objet
    macgyver = Angus(map)

    loop = True
    play = True
    while loop:
        for event in pygame.event.get():
            if event.type == 12:  # pygame.QUIT:
                loop = False
            if event.type == 2:
                if event.key == 113:  # Q
                    loop = False
                if play:
                    if event.key == K_DOWN:
                        macgyver.move("DOWN")
                    if event.key == K_UP:
                        macgyver.move("UP")
                    if event.key == K_RIGHT:
                        macgyver.move("RIGHT")
                    if event.key == K_LEFT:
                        macgyver.move("LEFT")

            # compare items' position to MacGyver's
            if macgyver.position == map.ether:
                macgyver.ether = True
            if macgyver.position == map.needle:
                macgyver.needle = True
            if macgyver.position == map.guardian:
                # test if inventory is full
                if not (macgyver.ether and macgyver.needle):
                    screen.message = "LOOSE"
                    play = False
            if macgyver.position == map.exit:
                screen.message = "WIN"
                play = False

        screen.refresh_screen()

if __name__ == "__main__":
    main()
