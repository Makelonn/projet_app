# !/usr/bin/env python

"""simple module for player implementation
"""

import PySimpleGUI as sg
import rts_map
import random
import math


class Player:
    def __init__(self, graph: sg.Graph, map: rts_map.Map, pos: list):
        self.graph = graph
        self.pos = pos
        self.player_id = self.graph.DrawImage(
            filename="image/unit_1.png",
            location=(self.pos),
        )
        self.test = self.graph.DrawImage(
            filename="image/test_transparency.png",
            location=(self.pos),
        )
        self.delay = 0
        self.image_nbr = random.randint(1, 5)
        self.map = map
        self.shift = [0, 0]
        self.selected_figure = None
        self.velocity = 100
        self.dest = [None, None]
        self.normalised_target = [None, None]
        self.norm = 0
        self.health = random.randint(30, 100)
        self.mana = random.randint(30, 100)

    def automation(self):
        if self.dest == [None, None]:
            random_pos = (
                random.randint(0, self.map.width * rts_map.TILESIZE),
                random.randint(0, self.map.width * rts_map.TILESIZE // 2),
            )
            self.dest = list(self.map.get_closest_valid_tile(random_pos))

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
        if self.selected_figure:
            self.graph.delete_figure(self.selected_figure)
        self.selected_figure = None

    def is_selected(self, pos):
        return abs(self.pos[0] - pos[0]) < 30 and abs(self.pos[1] - pos[1]) < 30

    def update(self, delta: float):
        self.delay += delta
        self.automation()
        if self.delay > 1:
            if self.image_nbr < 5:
                self.image_nbr += 1
            else:
                self.image_nbr = 1
            self.delay = 0
        if self.player_id:
            self.graph.delete_figure(self.player_id)
            self.player_id = self.graph.DrawImage(
                filename="image/unit_" + str(self.image_nbr) + ".png",
                location=(self.pos),
            )
        if self.dest != [None, None]:
            self.normalised_target = [
                self.dest[0] - self.pos[0],
                self.dest[1] - self.pos[1],
            ]

            self.norm = math.sqrt(
                math.pow(self.normalised_target[0], 2)
                + math.pow(self.normalised_target[1], 2)
            )
            self.normalised_target[0] = self.normalised_target[0] / self.norm
            self.normalised_target[1] = self.normalised_target[1] / self.norm
            if abs(self.normalised_target[0]) < (20 / self.norm) and abs(
                self.normalised_target[1]
            ) < (20 / self.norm):
                self.dest = [None, None]
                return
            self.pos[0] += self.normalised_target[0] * delta * self.velocity
            self.pos[1] += self.normalised_target[1] * delta * self.velocity
            self.graph.relocate_figure(self.player_id, *self.pos)
            if self.selected_figure:
                self.graph.relocate_figure(self.selected_figure, *self.pos)
