layout = [
    [sg.Text('Ma fenêtre')],
    [sg.Input()],
    [sg.Submit(), sg.Exit()]
]

window = sg.Window('Le titre de ma fenêtre', layout=layout)