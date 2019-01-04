#! /usr/bin/env python3
# coding: utf-8
import pytest
import pygame

from spritesheet import Spritesheet


class Test_spritesheet():
    STEP = 20
    TILES = "ressource/floor-tiles-20x20.png"
    FLOOR = (1 * STEP, 0 * STEP, STEP, STEP)
    WALL = (12 * STEP, 5 * STEP, STEP, STEP)

    def setup(self):
        pass

    def teardown(self):
        pass

    def test_init(self):
        ss = Spritesheet(self.TILES)
        floor = ss.image_at(self.FLOOR, -1)

    def test_multi(self):
        ss = Spritesheet(self.TILES)
        [wall, floor] = ss.images_at([self.WALL, self.FLOOR])

    def test_strips(self):
        ss = Spritesheet(self.TILES)
        result = ss.load_strip((0, 0, self.STEP, self.STEP), 8)
        assert len(result) == 8

    # def test_init_fail(self):
    #     with pytest.raises(TypeError):
    #         ss = Spritesheet("spritesheet.py")
