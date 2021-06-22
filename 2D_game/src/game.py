# !/usr/bin/env python

"""
    Small POC of rts game made in PySimpleGUI
"""

from tkinter.constants import DISABLED
from typing import Text
import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import (
    ProgressBar,
    TOOLTIP_FONT,
    ToolTip,
    one_line_progress_meter,
)
from rts_map import Map, TILESIZE
from player import Player
from mouse_position import Mouse_position
import datetime


GAMEPLAY_SIZE = (1024, 768)
BACKGROUND_COLOR = "white"


def game():

    sg.theme("DarkAmber")
    sg.set_options(tooltip_font=("Courier 14"))
    health_col = [
        [
            sg.Text(
                "Health",
                font="Courrier 24",
                justification="right",
                text_color="red",
            ),
        ],
        [
            sg.ProgressBar(
                100,
                orientation="h",
                size=(20, 20),
                key="-HEALTH-",
                bar_color=("red", "black"),
            ),
        ],
    ]
    mana_col = [
        [
            sg.Text(
                "Mana", font="Courrier 24", justification="right", text_color="blue"
            ),
        ],
        [
            sg.ProgressBar(
                100,
                orientation="h",
                size=(20, 20),
                key="-MANA-",
                bar_color=("blue", "black"),
            ),
        ],
    ]
    inner_layout = [
        [
            sg.Graph(
                GAMEPLAY_SIZE,
                (0, GAMEPLAY_SIZE[1]),
                (GAMEPLAY_SIZE[0], 0),
                background_color=BACKGROUND_COLOR,
                key="-GRAPH-",
                drag_submits=True,
                enable_events=True,
            )
        ],
        [
            sg.Column(health_col),
            sg.Button(
                "Attack",
                key="-ATTACK-",
                font="Courier 24",
                disabled_button_color="grey",
                tooltip="Inflict damage to ennemy",
            ),
            sg.Button(
                "Ability 1",
                key="-ABILITY 1-",
                font="Courier 24",
                disabled_button_color="grey",
                tooltip="Use your amazing ability 1",
            ),
            sg.Button(
                "Ability 2",
                key="-ABILITY 2-",
                font="Courier 24",
                disabled_button_color="grey",
                tooltip="Use your amazing ability 2",
            ),
            sg.Column(mana_col),
        ],
    ]

    sleep_time = 10
    mouse_pos = Mouse_position()
    window = sg.Window("RTS", inner_layout, finalize=True)
    window.TKroot.bind("<Motion>", mouse_pos.motion)
    window["-ABILITY 1-"].update(disabled=True, button_color="grey")
    window["-ABILITY 2-"].update(disabled=True, button_color="grey")
    window["-ATTACK-"].update(disabled=True, button_color="grey")
    window["-GRAPH-"].bind("<Button-1>", "+LEFT CLICK+")
    window["-GRAPH-"].bind("<Button-3>", "+RIGHT CLICK+")
    window["-GRAPH-"].bind("<B1-Motion>", "+LEFT MOTION+")
    window["-GRAPH-"].bind("<ButtonRelease-1>", "+RELEASED+")
    window["-MANA-"].set_tooltip("0")
    window["-HEALTH-"].set_tooltip("0")
    window.bind("<Left>", "+LEFT+")
    window.bind("<Right>", "+RIGHT+")
    window.bind("<Up>", "+UP+")
    window.bind("<Down>", "+DOWN+")

    graph_element = window["-GRAPH-"]

    selected_units = []
    shift_from_init_pos = {}
    rts_map = Map(graph_element, [8, 8])
    motion = False
    units = [
        Player(
            graph_element,
            rts_map,
            [
                rts_map.id_array[0][0][1][0] + TILESIZE // 2,
                rts_map.id_array[0][0][1][1],
            ],
        )
        for i in range(10)
    ]
    selection_rectangle = None
    start = datetime.datetime.now()
    last_post_read_time = start
    init_left_click_pos = None

    while True:
        pre_read_time = datetime.datetime.now()
        processing_time = (pre_read_time - last_post_read_time).total_seconds()
        time_to_sleep = sleep_time - int(processing_time * 1000)
        time_to_sleep = max(time_to_sleep, 0)
        event, value = window.read(time_to_sleep)
        now = datetime.datetime.now()
        delta = (now - last_post_read_time).total_seconds()
        last_post_read_time = now
        for unit in units:
            unit.update(delta)
        if event in (sg.WIN_CLOSED, "-QUIT-"):
            break

        elif event == "-GRAPH-+LEFT CLICK+":
            shift_from_init_pos.clear()
            window["-ABILITY 1-"].update(disabled=True, button_color="grey")
            window["-ABILITY 2-"].update(disabled=True, button_color="grey")
            window["-ATTACK-"].update(disabled=True, button_color="grey")
            window["-HEALTH-"].update(0)
            window["-MANA-"].update(0)
            window["-MANA-"].set_tooltip(str(0))
            window["-HEALTH-"].set_tooltip(str(0))
            init_left_click_pos = [mouse_pos.x, mouse_pos.y]
            for unit in selected_units:
                unit.unselected()
            selected_units.clear()
            for unit in units:
                if mouse_pos.x:
                    if unit.is_selected((mouse_pos.x, mouse_pos.y)):
                        unit.draw_selected()
                        selected_units.append(unit)
                        window["-HEALTH-"].update(unit.health)
                        window["-MANA-"].update(unit.mana)
                        window["-MANA-"].set_tooltip(str(unit.mana))
                        window["-HEALTH-"].set_tooltip(str(unit.health))
                        window["-ABILITY 1-"].update(
                            disabled=False, button_color="beige"
                        )
                        window["-ABILITY 2-"].update(
                            disabled=False, button_color="beige"
                        )
                        window["-ATTACK-"].update(disabled=False, button_color="beige")
                        break

        elif event == "-GRAPH-+LEFT MOTION+":
            if not init_left_click_pos:
                init_left_click_pos = [mouse_pos.x, mouse_pos.y]

            motion = True
            mouse_pos.x, mouse_pos.y = value["-GRAPH-"]
            if selection_rectangle:
                graph_element.delete_figure(selection_rectangle)
            selection_rectangle = graph_element.DrawRectangle(
                init_left_click_pos,
                (mouse_pos.x, mouse_pos.y),
                line_color="red",
                line_width=1,
            )
        elif event == "-GRAPH-+RIGHT CLICK+":
            if not rts_map.is_valid_tile((mouse_pos.x, mouse_pos.y)):
                click_pos = rts_map.get_closest_valid_tile((mouse_pos.x, mouse_pos.y))
            else:
                click_pos = (mouse_pos.x, mouse_pos.y)
            for unit in selected_units:
                if unit and shift_from_init_pos:

                    if rts_map.is_valid_tile(
                        (
                            click_pos[0] - shift_from_init_pos[unit][0],
                            click_pos[1] - shift_from_init_pos[unit][1],
                        )
                    ):
                        unit.move(
                            (
                                click_pos[0] - shift_from_init_pos[unit][0],
                                click_pos[1] - shift_from_init_pos[unit][1],
                            )
                        )
                    else:
                        new_pos = rts_map.get_closest_valid_tile(
                            (
                                click_pos[0] - shift_from_init_pos[unit][0],
                                click_pos[1] - shift_from_init_pos[unit][1],
                            )
                        )
                        unit.move((new_pos))
                elif unit:
                    unit.move(click_pos)

        elif event == "-GRAPH-+RELEASED+" and motion:
            motion = False
            if selection_rectangle:
                graph_element.delete_figure(selection_rectangle)
            for unit in selected_units:
                if unit:
                    unit.unselected()
            selected_units.clear()
            for unit in units:
                if mouse_pos.x and unit and init_left_click_pos:
                    if (
                        init_left_click_pos[0] <= unit.pos[0] <= mouse_pos.x
                        or init_left_click_pos[0] >= unit.pos[0] >= mouse_pos.x
                        and init_left_click_pos[1] <= unit.pos[1] <= mouse_pos.y
                        or init_left_click_pos[1] >= unit.pos[1] >= mouse_pos.y
                    ):
                        unit.draw_selected()
                        selected_units.append(unit)
                        shift_from_init_pos[unit] = (
                            init_left_click_pos[0] - unit.pos[0],
                            init_left_click_pos[1] - unit.pos[1],
                        )

        elif event in ("+LEFT+", "+RIGHT+", "+UP+", "+DOWN+"):
            rts_map.move_map(event)
            for unit in units:
                unit.move_with_map(event)

    window.close()


if __name__ == "__main__":
    game()