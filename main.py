#! /usr/bin/env python3
# coding: utf-8
import pygame


def main():
    screen = pygame.display.set_mode((300, 300))
    loop = True
    while loop:
        for event in pygame.event.get():
            if event.type == 12:  # pygame.QUIT:
                loop = False

        pygame.display.flip()

if __name__ == "__main__":
    main()
