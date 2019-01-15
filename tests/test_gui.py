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
        mappy = Mappy()
        screen = Display(mappy)

    def test_stop_win(self):
        mappy = Mappy()
        screen = Display(mappy)
        screen.message = "WIN"

    def test_stop_loose(self):
        mappy = Mappy()
        screen = Display(mappy)
        screen.message = "LOOSE"
