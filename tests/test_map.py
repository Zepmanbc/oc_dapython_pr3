#! /usr/bin/env python3
# coding: utf-8
import pytest

from map import Map


class Test_map():
    """
    MacGyver: (0, 2)
    Guardian: (11, 13)
    Exit: (11, 14)
    Floor: (0, 1)
    Wall: (1, 2)
    """
    def setup(self):
        self.map = Map()

    def teardown(self):
        pass

    def test_position_macgyver(self):
        assert self.map.macgyver == (0, 2)

    def test_is_move_possible_false(self):
        assert not self.map.is_move_possible((1, 2))

    def test_is_move_possible_true(self):
        assert self.map.is_move_possible((0, 1))

    def test_hide(self):
        self.map.hide((1, 2))
        # this was a Wall
        assert self.map.is_move_possible((1, 2))

    def test_is_move_possible_out(self):
        assert not self.map.is_move_possible((15, 5))

    def test_move(self):
        self.map.move("M", (0, 2), (0, 1))
