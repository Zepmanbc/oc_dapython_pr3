#! /usr/bin/env python3
# coding: utf-8
import pytest

from items import Angus
from map import Map


class Test_angus():

    def setup(self):
        self.map = Map()

    def teardown(self):
        pass

    def test_init(self):
        self.macgyver = Angus(self.map)
        assert self.macgyver.position == (0, 2)

    def test_move(self):
        self.macgyver = Angus(self.map)
        self.macgyver.move("UP")
