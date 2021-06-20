# !/usr/bin/env python

"""
    Used to get the mouse position not well implemented by PySimpleGUI
"""


class Mouse_position:
    def __init__(self):
        self.x = 0
        self.y = 0

    def motion(self, event):
        self.x, self.y = event.x, event.y