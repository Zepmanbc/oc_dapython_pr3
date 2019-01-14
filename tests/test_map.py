#! /usr/bin/env python3
# coding: utf-8
import pytest

from mappy import Mappy


class Test_map():
    """
    MacGyver: (0, 2)
    Guardian: (11, 13)
    Exit: (11, 14)
    Floor: (0, 1)
    Wall: (1, 2)
    """
    def setup(self):
        self.mappy = Mappy()

    def teardown(self):
        pass

    def test_position_macgyver(self):
        assert self.mappy.macgyver == (0, 2)

    def test_is_move_possible_false(self):
        assert not self.mappy.is_move_possible((1, 2))

    def test_is_move_possible_true(self):
        assert self.mappy.is_move_possible((0, 1))

    def test_hide(self):
        self.mappy.hide((1, 2))
        # this was a Wall
        assert self.mappy.is_move_possible((1, 2))

    def test_is_move_possible_out(self):
        assert not self.mappy.is_move_possible((15, 5))

    def test_move(self):
        self.mappy.move("M", (0, 2), (0, 1))
