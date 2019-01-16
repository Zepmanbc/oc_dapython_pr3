#! /usr/bin/env python3
# coding: utf-8

"""Main file of the MacGyver game."""

import pygame
from pygame.locals import K_UP, K_DOWN, K_LEFT, K_RIGHT

from mappy import Mappy
from gui import Display
from items import Angus


def main():
    """Run the main part."""
    mappy = Mappy()
    screen = Display(mappy)
    macgyver = Angus(mappy)

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
                    screen.message = False  # delete instruction messages on first move
                    if event.key == K_DOWN:
                        macgyver.move("DOWN")
                    if event.key == K_UP:
                        macgyver.move("UP")
                    if event.key == K_RIGHT:
                        macgyver.move("RIGHT")
                    if event.key == K_LEFT:
                        macgyver.move("LEFT")

            # compare items' position to MacGyver's
            if mappy.macgyver == mappy.ether:
                macgyver.ether = True
                mappy.ether = None
            if mappy.macgyver == mappy.needle:
                macgyver.needle = True
                mappy.needle = None
            if mappy.macgyver == mappy.tube:
                macgyver.tube = True
                mappy.tube = None
            if mappy.macgyver == mappy.guardian:
                # test if inventory is full
                if not macgyver.is_inventory_full():
                    screen.message = "LOOSE"
                    play = False
            if mappy.macgyver == mappy.exit:
                screen.message = "WIN"
                play = False

        screen.refresh_screen()

if __name__ == "__main__":
    main()
