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
    pygame.time.Clock().tick(30)
    map = Map()
    screen = Display(window, map.map)

    # create player objet
    macgyver = Angus(map)

    loop = True  # main loop
    play = True  # allow moves
    while loop:
        for event in pygame.event.get():
            if event.type == 12:  # pygame.QUIT:
                loop = False
            if event.type == 2:
                if event.key == 113:  # Q
                    loop = False
                if play:
                    screen.message = False  # delete instruction messages
                    if event.key == K_DOWN:
                        macgyver.move("DOWN")
                    if event.key == K_UP:
                        macgyver.move("UP")
                    if event.key == K_RIGHT:
                        macgyver.move("RIGHT")
                    if event.key == K_LEFT:
                        macgyver.move("LEFT")

            # compare items' position to MacGyver's
            if map.macgyver == map.ether:
                macgyver.ether = True
            if map.macgyver == map.needle:
                macgyver.needle = True
            if map.macgyver == map.tube:
                macgyver.tube = True
            if map.macgyver == map.guardian:
                # test if inventory is full
                if not macgyver.is_inventory_full():
                    screen.message = "LOOSE"
                    play = False
            if map.macgyver == map.exit:
                screen.message = "WIN"
                play = False

        screen.refresh_screen()

if __name__ == "__main__":
    main()
