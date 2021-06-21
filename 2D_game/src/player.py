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
        self.velocity = 10
        self.dest = [None, None]

    def move(self, pos):
        self.dest = list(pos)

    def move_with_map(self, dir):
        if dir == "+RIGHT+":
            self.pos[0] -= rts_map.TILESIZE
            self.shift[0] -= 1
            if self.dest != [None, None]:
                self.dest[0] -= rts_map.TILESIZE

        elif dir == "+LEFT+":
            self.pos[0] += rts_map.TILESIZE
            self.shift[0] += 1
            if self.dest != [None, None]:
                self.dest[0] += rts_map.TILESIZE

        elif dir == "+DOWN+":
            self.pos[1] -= rts_map.TILESIZE
            self.shift[1] -= 1
            if self.dest != [None, None]:
                self.dest[1] -= rts_map.TILESIZE

        elif dir == "+UP+":
            self.pos[1] += rts_map.TILESIZE
            self.shift[1] += 1
            if self.dest != [None, None]:
                self.dest[1] += rts_map.TILESIZE

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
        if self.dest != [None, None]:
            target = [self.dest[0] - self.pos[0], self.dest[1] - self.pos[1]]
            if abs(target[0]) < 20 and abs(target[1]) < 20:
                self.dest = [None, None]
                return
            self.pos[0] += target[0] * delta * self.velocity
            self.pos[1] += target[1] * delta * self.velocity
            self.graph.relocate_figure(self.player_id, *self.pos)
            if self.selected_figure:
                self.graph.relocate_figure(self.selected_figure, *self.pos)
