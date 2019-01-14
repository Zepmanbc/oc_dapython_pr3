#! /usr/bin/env python3
# coding: utf-8
import pytest
import pygame

from spritesheet import Spritesheet
from gui import Display
from mappy import Mappy


class Test_gui():

    def setup(self):
        pass

    def teardown(self):
        pass

    def test_display(self):
        window = pygame.display.set_mode((300, 300))
        mappy = Mappy()
        screen = Display(window, mappy.mappy)

    def test_stop_win(self):
        window = pygame.display.set_mode((300, 300))
        mappy = Mappy()
        screen = Display(window, mappy.mappy)
        screen.message = "WIN"

    def test_stop_loose(self):
        window = pygame.display.set_mode((300, 300))
        mappy = Mappy()
        screen = Display(window, mappy.mappy)
        screen.message = "LOOSE"
