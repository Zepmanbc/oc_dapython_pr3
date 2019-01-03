#! /usr/bin/env python3
# coding: utf-8
import pygame
from pygame.locals import K_UP, K_DOWN, K_LEFT, K_RIGHT
from gui import Display
from map import Map
from items import Angus


def main():
    window = pygame.display.set_mode((300, 300))
    map = Map()
    screen = Display(window, map.map)

    # create player objet
    macgyver = Angus(map)

    loop = True
    end_message = ""
    while loop:
        for event in pygame.event.get():
            if event.type == 12:  # pygame.QUIT:
                loop = False
            if event.type == 2:
                if event.key == 113:  # Q
                    loop = False
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
                    end_message = "LOOSE"
                    loop = False
            if macgyver.position == map.exit:
                end_message = "WIN"
                loop = False

            screen.refresh_screen()

            if end_message:
                screen.stop(end_message)
    if end_message:
        loop = True
        while loop:
            for event in pygame.event.get():
                if event.type == 12:  # pygame.QUIT:
                    loop = False
                if event.type == 2:
                    if event.key == 113:  # Q
                        loop = False

if __name__ == "__main__":
    main()
