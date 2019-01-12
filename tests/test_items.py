"""Pytest for item.py."""
#! /usr/bin/env python3
# coding: utf-8
import pytest

from items import Angus
from map import Map


class Test_angus():
    """Pytest for item.Angus()."""

    def setup(self):
        """Set up Pytest method."""
        self.map = Map()

    def teardown(self):
        """Teardown test method."""
        pass

    def test_init(self):
        """Test initial position."""
        self.macgyver = Angus(self.map)
        assert self.map.macgyver == (0, 2)

    def test_move(self):
        """Test the position after some moves.

        initial: (0, 2)
        UP: (0, 1)
        RIGHT: WALL same position
        UP: (0, 0)
        UP: out of screen same position
        RIGHT: (1, 0)
        """
        self.macgyver = Angus(self.map)
        self.macgyver.move("UP")
        self.macgyver.move("RIGHT")
        self.macgyver.move("UP")
        self.macgyver.move("UP")
        self.macgyver.move("RIGHT")
        assert self.map.macgyver == (1, 0)
