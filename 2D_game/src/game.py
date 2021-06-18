# !/usr/bin/env python

"""
    Small POC of rts game made in PySimpleGUI
"""

import PySimpleGUI as sg
from rts_map import Map
from player import Player

GAMEPLAY_SIZE = (1024, 768)
BACKGROUND_COLOR = "white"


def game():

    sg.theme("DarkAmber")

    inner_layout = [
        [
            sg.Graph(
                GAMEPLAY_SIZE,
                (0, GAMEPLAY_SIZE[1]),
                (GAMEPLAY_SIZE[0], 0),
                background_color=BACKGROUND_COLOR,
                key="-GRAPH-",
                enable_events=True,
            )
        ]
    ]
    window = sg.Window("RTS", inner_layout, finalize=True)
    window.bind("<Button-1>", "+LEFT CLICK+")
    window.bind("<Left>", "+LEFT+")
    window.bind("<Right>", "+RIGHT+")
    window.bind("<Up>", "+UP+")
    window.bind("<Down>", "+DOWN+")
    graph_element = window["-GRAPH-"]

    rts_map = Map(graph_element, [8, 8])
    unit = Player(graph_element, rts_map)
    while True:
        event, value = window.read()
        if event in (sg.WIN_CLOSED, "-QUIT-"):
            break
        elif event == "+LEFT CLICK+":
            if rts_map.is_valid_tile(value["-GRAPH-"]):
                unit.move(value["-GRAPH-"])
        elif event in ("+LEFT+", "+RIGHT+", "+UP+", "+DOWN+"):
            rts_map.move_map(event)
            unit.move_with_map(event)

    window.close()


if __name__ == "__main__":
    game()