#! /usr/bin/env python3
# coding: utf-8
import pytest
import threading

from pynput.keyboard import Key, Controller

import main


class Test_main():

    def setup(self):
        self.keyboard = Controller()

    def teardown(self):
        pass

    def test_main(self):
        # threading.Thread(main.main()).start()
        threading.Thread(self.press_Q())

    def press_Q(self):
        self.keyboard.press('q')
        self.keyboard.release('q')
