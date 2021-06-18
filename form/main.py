import PySimpleGUI as sg
from image_converter import convert_to_bytes

IMG_TYPES = [("PNG (*.png)", "*.png"), ("JPEG (*.jpg)", "*.jpg")]
DD_RACES = ["Elfe", "Halfelin", "Humain", "Nain", "Demi-Elfe", "Demi-Orque", "Drakéide", "Gnome", "Tieffelin", "Aarakocra", "Génasi", "Gnome des profondeurs", "Goliath"]
DD_ALIGNMENT = ["Loyal Bon (LB)", "Neutre Bon (NB)", "Chaotique Bon (CB)", "Loyal Neutre (LN)", "Neutre (N)", "Chaotique Neutre (CN)", "Loyal Mauvais (LM)", "Neutre mauvais (NM)", "Chaotique mauvais (CM)"]
DD_CLASSES = ["Barbare", "Barde", "Clerc", "Druide", "Ensorceleur", "Guerrier", "Magicien", "Moine", "Paladin", "Rôdeur", "Roublard", "Sorcier"]

class CharacterCreator():
    """The program that helps us create a character"""

    def __init__(self):
        # Theme
        sg.theme('DarkGrey5')

        # --- Columns ---
        self.image_col = [
            [sg.Frame(layout=[[sg.Image('./assets/2.png', size=(200, 200), key='-IMAGE-')],
                              [sg.FileBrowse(key='-IMGBROWSE-', file_types=IMG_TYPES, enable_events=True)]], title='Image du personnage', element_justification="right", size=(210, 210))]
        ]
        self.base_col = [
            [sg.Text("Nom & Prénom : "), sg.InputText(size=(30, 1))],
            [sg.Text("Genre : "), sg.Radio('Homme', "R1"),
             sg.Radio('Femme', "R1"), sg.Radio('Autre', "R1")],
            [sg.Text("Race : "), sg.InputCombo(DD_RACES)],
            [sg.Text("Alignement : "), sg.InputCombo(DD_ALIGNMENT)],
            [sg.Text("Classe :"), sg.InputCombo(DD_CLASSES)],
            [sg.Text("Niveau :"), sg.InputText(key='-LVL-', enable_events=True, size=(15, 1)), sg.Text("Points d'expérience"), sg.InputText(key='-XP-', size=(15, 1), enable_events=True)],
        ]
        self.appearance_col = [
            [sg.Frame(layout = [
                [sg.Text("Age :"), sg.InputText(key='-AGE-', size=(10, 1)), sg.Text('Taille (cm) :'), sg.InputText(key='-HEIGHT-', size=(10, 1)), sg.Text("Poids (kg)"), sg.InputText(key='-WEIGHT-', size=(10, 1))],
                [sg.Text('Cheveux'), sg.InputCombo(('Bruns', 'Blonds', 'Châtaings', 'Noirs', 'Blanc', 'Rose')), sg.Text("Yeux"), sg.InputCombo(('Bleus', 'Verts', 'Bruns', 'Gris', 'Rouges', 'Sans'))]
            ], element_justification='center', title='Physique')]
        ]

        # --- Window Layout ---
        self.layout = [
            [sg.Text('CRÉATEUR DE PERSONNAGE', size=(25, 1),
                     justification='center', font=('', 30), key='-TITLE-')],
            [sg.Column(self.base_col, justification='left', key='-BASE-COL-'), sg.Column(
                self.image_col, justification='right', key='-IMAGE-COL-')],
            [sg.Column(self.appearance_col, justification='center', key='-APPEARANCE-COL-')]
        ]

        # Window
        self.window = sg.Window('Créateur de personnage',
                                self.layout, margins=(5, 5), finalize=True)
        
        # --- Expanding things ---
        self.window['-IMAGE-COL-'].expand(expand_x=True)
        #self.window['-APPEARANCE-COL-'].expand(expand_x=True)
        self.window['-TITLE-'].expand(expand_x=True)
        self.window['-BASE-COL-'].expand(expand_x=True)


    def loop(self):
        """The loop of our program that handles the different possible events 
        in the GUI"""
        while True:
            event, values = self.window.read()
            print(event, values)
            # If quiting
            if event in (sg.WIN_CLOSED, 'Exit'):
                break
            # If searching for an image
            if event == '-IMGBROWSE-':
                filename = values['-IMGBROWSE-']
                if filename:
                    self.window['-IMAGE-'].update(
                        data=convert_to_bytes(filename, resize=(200, 200)))
                    self.window['-TITLE-'].justification = 'center'
            # Entering exp points and level
            if event in ('-XP-', '-LVL-') and (values['-XP-'] and values['-XP-'][-1] not in ('0123456789-')) or (values['-LVL-'] and values['-LVL-'][-1] not in ('0123456789-')):
                if event == '-XP-':
                    self.window['-XP-'].update(values['-XP-'][:-1])
                if event == '-LVL-':
                    self.window['-LVL-'].update(values['-LVL-'][:-1])
        # Closing window if the loop broke
        self.window.close()


if __name__ == '__main__':
    character_creator = CharacterCreator()
    character_creator.loop()
