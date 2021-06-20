# !/usr/bin/env python

"""
    Map representation
"""

import PySimpleGUI as sg

TILESIZE = 250


class Map:
    def __init__(self, graph: sg.Graph, size: tuple):
        self.graph = graph
        self.width = size[0]
        self.height = size[1]
        self.id_array = []
        self.shift = [0, 0]
        for width in range(self.width):
            self.id_array.append([])
            for height in range(self.height):

                self.id_array[width].append(
                    (
                        self.graph.DrawImage(
                            filename="image/tile_iso.png",
                            location=(
                                1 / 2 * width * TILESIZE + 1 / 2 * height * TILESIZE,
                                1
                                / 2
                                * (
                                    1 / 2 * height * TILESIZE
                                    + (1 / 2 * (self.width - 1) * TILESIZE)
                                    - (1 / 2 * width * TILESIZE)
                                ),
                            ),
                        ),
                        [
                            1 / 2 * width * TILESIZE + 1 / 2 * height * TILESIZE,
                            1
                            / 2
                            * (
                                1 / 2 * height * TILESIZE
                                + (1 / 2 * (self.width - 1) * TILESIZE)
                                - (1 / 2 * width * TILESIZE)
                            ),
                        ],
                    )
                )

    def is_valid_tile(self, pos: tuple):
        cam_pos = [0, 0]
        cam_pos[0] = pos[0] - self.shift[0] * TILESIZE
        cam_pos[1] = pos[1] - self.shift[1] * TILESIZE
        if (
            self.width / 2 * TILESIZE >= cam_pos[0] >= 0
            and self.width / 4 * TILESIZE >= cam_pos[1] >= 0
        ):
            if cam_pos[0] > self.width / 2 * TILESIZE - 2 * cam_pos[1]:
                return True

        elif (
            self.width * TILESIZE >= cam_pos[0] >= self.width / 2 * TILESIZE
            and self.width / 4 * TILESIZE >= cam_pos[1] >= 0
        ):
            if cam_pos[0] < self.width / 2 * TILESIZE + 2 * cam_pos[1]:
                return True

        elif (
            self.width / 2 * TILESIZE >= cam_pos[0] >= 0
            and self.width / 2 * TILESIZE >= cam_pos[1] >= self.width / 4 * TILESIZE
        ):
            if cam_pos[0] > 2 * cam_pos[1] - self.width / 2 * TILESIZE:
                return True

        elif (
            self.width * TILESIZE >= cam_pos[0] >= self.width / 2 * TILESIZE
            and self.width / 2 * TILESIZE >= cam_pos[1] >= self.width / 4 * TILESIZE
        ):
            if cam_pos[0] < -2 * cam_pos[1] + 3 / 2 * self.width * TILESIZE:
                return True
        return False

    def move_map(self, dir: str):
        if dir == "+RIGHT+":
            for line in self.id_array:
                for tile in line:
                    self.graph.relocate_figure(
                        tile[0], tile[1][0] - TILESIZE, tile[1][1]
                    )
                    tile[1][0] = tile[1][0] - TILESIZE
            self.shift[0] -= 1

        elif dir == "+LEFT+":
            for line in self.id_array:
                for tile in line:
                    self.graph.relocate_figure(
                        tile[0], tile[1][0] + TILESIZE, tile[1][1]
                    )
                    tile[1][0] = tile[1][0] + TILESIZE
            self.shift[0] += 1

        elif dir == "+DOWN+":
            for line in self.id_array:
                for tile in line:
                    self.graph.relocate_figure(
                        tile[0], tile[1][0], tile[1][1] - TILESIZE
                    )
                    tile[1][1] = tile[1][1] - TILESIZE
            self.shift[1] -= 1
        elif dir == "+UP+":
            for line in self.id_array:
                for tile in line:
                    self.graph.relocate_figure(
                        tile[0], tile[1][0], tile[1][1] + TILESIZE
                    )
                    tile[1][1] = tile[1][1] + TILESIZE
            self.shift[1] += 1

    def get_closest_valid_tile(self, pos):
        shifted_pos = [0, 0]

        shifted_pos[0] = pos[0] - self.shift[0] * TILESIZE
        shifted_pos[1] = pos[1] - self.shift[1] * TILESIZE
        if (
            self.width / 2 * TILESIZE >= shifted_pos[0]
            and self.width / 4 * TILESIZE >= shifted_pos[1]
        ):
            b = shifted_pos[1] - 2 * shifted_pos[0]
            x = (-b + (self.width / 2 * TILESIZE) / 2) / (1 / 2 + 2)
            return (
                int(x + self.shift[0] * TILESIZE),
                int(2 * x + b + self.shift[1] * TILESIZE),
            )

        elif (
            self.width * TILESIZE >= shifted_pos[0]
            and self.width / 4 * TILESIZE >= shifted_pos[1]
        ):
            b = shifted_pos[1] + 2 * shifted_pos[0]
            x = (-b - (self.width / 2 * TILESIZE) / 2) / (-1 / 2 - 2)
            return (
                int(x + self.shift[0] * TILESIZE),
                int(-2 * x + b + self.shift[1] * TILESIZE),
            )

        elif (
            self.width / 2 * TILESIZE >= shifted_pos[0]
            and self.width / 2 * TILESIZE >= shifted_pos[1]
        ):
            b = 2 * shifted_pos[0] + shifted_pos[1]
            x = ((self.width / 2 * TILESIZE) / 2 - b) / (-2 - 1 / 2)
            return (
                int(x + self.shift[0] * TILESIZE),
                int(-2 * x + b + self.shift[1] * TILESIZE) - 35,
            )

        elif (
            shifted_pos[0] >= self.width / 2 * TILESIZE
            and shifted_pos[1] >= self.width / 4 * TILESIZE
        ):
            b = shifted_pos[1] - 2 * shifted_pos[0]
            x = ((3 / 2 * self.width * TILESIZE) / 2 - b) / (2 + 1 / 2)
            return (
                int(x + self.shift[0] * TILESIZE),
                int(2 * x + b + self.shift[1] * TILESIZE) - 45,
            )
