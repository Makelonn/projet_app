# !/usr/bin/env python

"""
    Small POC of rts game made in PySimpleGUI
"""

import PySimpleGUI as sg
from rts_map import Map, TILESIZE
from player import Player
from mouse_position import Mouse_position


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
                drag_submits=True,
                enable_events=True,
            )
        ]
    ]

    mouse_pos = Mouse_position()
    window = sg.Window("RTS", inner_layout, finalize=True)

    window.TKroot.bind("<Motion>", mouse_pos.motion)

    window.bind("<Button-1>", "+LEFT CLICK+")
    window.bind("<Button-3>", "+RIGHT CLICK+")
    window.bind("<B1-Motion>", "+LEFT MOTION+")
    window.bind("<Left>", "+LEFT+")
    window.bind("<Right>", "+RIGHT+")
    window.bind("<Up>", "+UP+")
    window.bind("<Down>", "+DOWN+")
    window.bind("<ButtonRelease-1>", "+RELEASED+")
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
        ),
        Player(
            graph_element,
            rts_map,
            [
                rts_map.id_array[0][0][1][0] + TILESIZE // 2 + 30,
                rts_map.id_array[0][0][1][1] + 5,
            ],
        ),
        Player(
            graph_element,
            rts_map,
            [
                rts_map.id_array[0][0][1][0] + TILESIZE // 2 + 30,
                rts_map.id_array[0][0][1][1] + 30,
            ],
        ),
    ]
    selection_rectangle = None
    while True:
        event, value = window.read()
        print(event)
        if event in (sg.WIN_CLOSED, "-QUIT-"):
            break

        elif event == "+LEFT CLICK+":
            shift_from_init_pos.clear()
            init_left_click_pos = [mouse_pos.x, mouse_pos.y]
            for unit in selected_units:
                unit.unselected()
            selected_units.clear()
            for unit in units:
                if unit.is_selected((mouse_pos.x, mouse_pos.y)):
                    unit.draw_selected()
                    selected_units.append(unit)
                    print("break")
                    break

        elif event == "+LEFT MOTION+":
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
        elif event == "+RIGHT CLICK+":
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
                        print("test")
                        new_pos = rts_map.get_closest_valid_tile(
                            (
                                click_pos[0] - shift_from_init_pos[unit][0],
                                click_pos[1] - shift_from_init_pos[unit][1],
                            )
                        )
                        unit.move((new_pos))
                elif unit:
                    unit.move(click_pos)

        elif event == "+RELEASED+" and motion:
            motion = False
            print("released")
            if selection_rectangle:
                graph_element.delete_figure(selection_rectangle)
            for unit in units:
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