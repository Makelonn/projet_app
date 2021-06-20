# !/usr/bin/env python

"""simple module for player implementation
"""

import PySimpleGUI as sg
import rts_map


class Player:
    def __init__(self, graph: sg.Graph, map: rts_map.Map):
        self.graph = graph
        self.pos = [
            map.id_array[0][0][1][0] + rts_map.TILESIZE // 2,
            map.id_array[0][0][1][1],
        ]
        self.player_id = self.graph.DrawImage(
            filename="image/unit.png",
            location=(self.pos),
        )
        self.shift = [0, 0]

    def move(self, pos):
        self.pos = list(pos)
        self.graph.relocate_figure(self.player_id, *pos)

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
        print(*self.pos)