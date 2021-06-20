# !/usr/bin/env python

"""simple module for player implementation
"""

import PySimpleGUI as sg
import rts_map
import math


class Player:
    def __init__(self, graph: sg.Graph, map: rts_map.Map, pos: list):
        self.graph = graph
        self.pos = pos
        self.player_id = self.graph.DrawImage(
            filename="image/unit.png",
            location=(self.pos),
        )
        self.shift = [0, 0]
        self.selected_figure = None

    def move(self, pos):
        self.pos = list(pos)
        self.graph.relocate_figure(self.player_id, *pos)
        if self.selected_figure:
            self.graph.relocate_figure(self.selected_figure, *self.pos)

    def move_with_map(self, dir):
        if dir == "+RIGHT+":
            self.pos[0] -= rts_map.TILESIZE
            self.shift[0] -= 1

        elif dir == "+LEFT+":
            self.pos[0] += rts_map.TILESIZE
            self.shift[0] += 1

        elif dir == "+DOWN+":
            self.pos[1] -= rts_map.TILESIZE
            self.shift[1] -= 1
        elif dir == "+UP+":
            self.pos[1] += rts_map.TILESIZE
            self.shift[1] += 1
        self.graph.relocate_figure(self.player_id, *self.pos)
        if self.selected_figure:
            self.graph.relocate_figure(self.selected_figure, *self.pos)

    def draw_selected(self):
        self.selected_figure = self.graph.DrawRectangle(
            self.pos, (self.pos[0] + 5, self.pos[1] + 10), fill_color="red"
        )

    def unselected(self):
        self.graph.delete_figure(self.selected_figure)
        self.selected_figure = None

    def is_selected(self, pos):
        return abs(self.pos[0] - pos[0]) < 30 and abs(self.pos[1] - pos[1]) < 30

    def update(self, delta: float):

        self.pos[0] = int(self.pos[0] + self.velocity / math.sqrt(2) * delta)
