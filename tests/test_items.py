"""Pytest for item.py."""
#! /usr/bin/env python3
# coding: utf-8
import pytest

from items import Angus
from mappy import Mappy


class Test_angus():
    """Pytest for item.Angus()."""

    def setup(self):
        """Set up Pytest method."""
        self.mappy = Mappy()

    def teardown(self):
        """Teardown test method."""
        pass

    def test_init(self):
        """Test initial position."""
        self.macgyver = Angus(self.mappy)
        assert self.mappy.macgyver == (0, 2)

    def test_move(self):
        """Test the position after some moves.

        initial: (0, 2)
        UP: (0, 1)
        RIGHT: WALL same position
        UP: (0, 0)
        UP: out of screen same position
        RIGHT: (1, 0)
        """
        self.macgyver = Angus(self.mappy)
        self.macgyver.move("UP")
        self.macgyver.move("RIGHT")
        self.macgyver.move("UP")
        self.macgyver.move("UP")
        self.macgyver.move("RIGHT")
        assert self.mappy.macgyver == (1, 0)

    def test_is_inventory_full_false(self):
        """All 3 items are False."""
        self.macgyver = Angus(self.mappy)
        assert self.macgyver.is_inventory_full() == False

    def test_is_inventory_full_false2(self):
        """1/3 items is True."""
        self.macgyver = Angus(self.mappy)
        self.macgyver.ether = True
        assert self.macgyver.is_inventory_full() == False

    def test_is_inventory_full_true(self):
        """All items are True."""
        self.macgyver = Angus(self.mappy)
        self.macgyver.ether = True
        self.macgyver.needle = True
        self.macgyver.tube = True
        assert self.macgyver.is_inventory_full() == True

