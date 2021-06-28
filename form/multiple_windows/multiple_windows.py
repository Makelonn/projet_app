import PySimpleGUI as sg
"""
    Demo - 2 simultaneous windows using read_all_window

    Both windows are immediately visible.  Each window updates the other.

    Copyright 2020 PySimpleGUI.org
"""

sg.theme("BrightColors")

def create_w1():
    layout = [[sg.Text('Fenêtre 1', font=('Comic Sans MS', 20, 'bold'))],
              [sg.Text("Ecrivez quelque-chose à afficher sur l'autre fenêtre", font=('Comic Sans MS', 15))],
              [sg.Input(key='-IN-', enable_events=True, font=('Comic Sans MS', 15))],
              [sg.Text(size=(45,1), key='-OUTPUT-')],
              [sg.Button('Ouvrir deuxième fenêtre', font=('Comic Sans MS', 15))],
              [sg.Button('Quitter', font=('Comic Sans MS', 15))]]
    return sg.Window('Fenêtre 1', layout, finalize=True, font=('Comic Sans MS', 15))


def create_w2():
    layout = [[sg.Text('Fenêtre 2', font=('Comic Sans MS', 20, 'bold'))],
              [sg.Text("Ecrivez quelque-chose à afficher sur l'autre fenêtre", font=('Comic Sans MS', 15))],
              [sg.Input(key='-IN-', enable_events=True, font=('Comic Sans MS', 15))],
              [sg.Text(size=(45,1), key='-OUTPUT-')],
              [sg.Button('Quitter', font=('Comic Sans MS', 15))]]
    return sg.Window('Fenêtre 2', layout, finalize=True, font=('Comic Sans MS', 15))


def main():
    window1, window2 = create_w1(), create_w2()

    window1.move(window1.current_location()[0], window1.current_location()[1]-200)
    window2.move(window1.current_location()[0], window1.current_location()[1]+250)

    while True:             # Event Loop
        window, event, values = sg.read_all_windows()

        if window == sg.WIN_CLOSED:     # if all windows were closed
            break
        if event == sg.WIN_CLOSED or event == 'Quitter':
            window.close()
            if window == window2:       # if closing win 2, mark as closed
                window2 = None
            elif window == window1:     # if closing win 1, mark as closed
                window1 = None

        elif event == 'Ouvrir deuxième fenêtre':
            if not window2:
                window2 = create_w2()
                window2.move(window1.current_location()[0], window1.current_location()[1] + 300)

        elif event == '-IN-':
            output_window = window2 if window == window1 else window1
            if output_window:           # if a valid window, then output to it
                output_window['-OUTPUT-'].update(values['-IN-'])
            else:
                window['-OUTPUT-'].update('Other window is closed')


if __name__ == '__main__':
    main()
