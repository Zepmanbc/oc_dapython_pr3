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

    # init items
    macgyver = Angus(map.macgyver, map)

    loop = True
    while loop:
        for event in pygame.event.get():
            if event.type == 12:  # pygame.QUIT:
                loop = False
            if event.type == 2:
                if event.key == 113:  # Q
                    loop = False
                if event.key == K_DOWN:
                    macgyver.down()
                if event.key == K_UP:
                    macgyver.up()
                if event.key == K_RIGHT:
                    macgyver.right()
                if event.key == K_LEFT:
                    macgyver.left()

            # verification items position
            if macgyver.position == map.ether:
                macgyver.ether = True
                print("got ether!")
            if macgyver.position == map.needle:
                macgyver.needle = True
                print("got needle!")
            if macgyver.position == map.guardian:
                if not (macgyver.ether and macgyver.needle):
                    print("loose")
            if macgyver.position == map.exit:
                print("win")

        screen.refresh_screen()
        # pygame.display.flip()

if __name__ == "__main__":
    main()
