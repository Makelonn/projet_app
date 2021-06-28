import PySimpleGUI as sg
from graphs import radar_graph
from image_converter import convert_to_bytes
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import time 
import itertools

IMG_TYPES = [("PNG (*.png)", "*.png"), ("JPEG (*.jpg)", "*.jpg")]
DD_RACES = ["Elfe", "Halfelin", "Humain", "Nain", "Demi-Elfe", "Demi-Orque", "Drakéide",
            "Gnome", "Tieffelin", "Aarakocra", "Génasi", "Gnome des profondeurs", "Goliath"]
DD_ALIGNMENT = ["Loyal Bon (LB)", "Neutre Bon (NB)", "Chaotique Bon (CB)", "Loyal Neutre (LN)", "Neutre (N)",
                "Chaotique Neutre (CN)", "Loyal Mauvais (LM)", "Neutre mauvais (NM)", "Chaotique mauvais (CM)"]
DD_CLASSES = ["Barbare", "Barde", "Clerc", "Druide", "Ensorceleur",
              "Guerrier", "Magicien", "Moine", "Paladin", "Rôdeur", "Roublard", "Sorcier"]
FONT = 'Constantia'


class CharacterCreator():
    """The program that helps us create a character"""

    def __init__(self):
        # Theme
        sg.theme('DarkGrey4')

        # --- Menu ---
        self.menu = [['Fichier', ['Nouveau', 'Ouvrir', 'Charger un personnage']],
                     ['Paramètres',
                      ['Danger',
                       ['Comic Sans MS', 'Papyrus']],
                     ['Aide', 'A propos...']]]

        # --- Columns ---
        self.image_col = [
            [sg.Text('Image du personnage', size=(
                17, 1), justification='center')],
            [sg.Image('../assets/2.png', size=(200, 200), key='-IMAGE-')],
            [sg.FileBrowse(key='-IMGBROWSE-',
                           file_types=IMG_TYPES, enable_events=True)],
        ]
        self.base_col = [
            [sg.Text("Nom : ", size=(12, 1)), sg.Input(size=(15, 1))],
            [sg.Text("Prénom : ", size=(12, 1)), sg.Input(size=(15, 1))],
            [sg.Text("Genre : ",  size=(12, 1)), sg.Radio('Homme', "R1", size=(5, 1), key='-R1-'),
             sg.Radio('Femme', "R1", size=(5, 1)), sg.Radio('Autre', "R1", size=(5, 1))],
            [sg.Text("Race : ", size=(13, 1)), sg.InputCombo(
                DD_RACES, default_value="Votre race ici", size=(15, 1))],
            [sg.Text("Alignement : ", size=(13, 1)), sg.InputCombo(
                DD_ALIGNMENT, default_value="Votre alignement ici", size=(15, 1))],
            [sg.Text("Classe :", size=(13, 1)), sg.InputCombo(
                DD_CLASSES, default_value="Votre classe ici", size=(15, 1))],
            [sg.Text("Niveau :", size=(12, 1)), sg.Input(
                key='-LVL-', enable_events=True, size=(15, 1))],
            [sg.Text("Points d'expérience : ",  size=(12, 1)), sg.Input(
                key='-XP-', size=(15, 1), enable_events=True)],
        ]
        self.appearance_col = [
            [sg.Text("Âge :", size=(10, 1)), sg.Input(key='-AGE-', size=(10, 1)),
             sg.Text('Taille (cm) :', size=(10, 1)), sg.Spin(values=[
                 150, 155, 160, 165, 170, 175, 180, 185, 190, 195], initial_value=175, size=(10, 1)),
             sg.Text("Poids (kg) : ", size=(10, 1)), sg.Spin(values=[50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100], initial_value=65, size=(10, 1))],
            [sg.Text('Cheveux : ', size=(10, 1)), sg.InputCombo(('Bruns', 'Blonds', 'Châtains', 'Noirs', 'Blanc', 'Rose'), default_value="Bruns", size=(10, 1)),
             sg.Text("Yeux : ", size=(9, 1)), sg.InputCombo(
                 ('Bleus', 'Verts', 'Bruns', 'Gris', 'Rouges', 'Sans'), size=(10, 1), default_value="Bleus"),
             sg.Text("Barbe :", size=(10, 1)), sg.InputCombo(('Sans', 'Courte', 'Longue'), default_value='Sans', size=(10, 1))]
        ]
        self.stats = [
            [sg.Text("Force :", size=(10, 1)), sg.Slider((0, 20), orientation='h', key='-SLIDER_F-',
                                                         enable_events=True, disable_number_display=True), sg.Text('0', size=(4, 1), key='-S_F-')],
            [sg.Text("Intelligence :", size=(10, 1)), sg.Slider((0, 20), orientation='h', key='-SLIDER_I-',
                                                                enable_events=True, disable_number_display=True), sg.Text('0', size=(4, 1), key='-S_I-')],
            [sg.Text("Dextérité :", size=(10, 1)), sg.Slider((0, 20), orientation='h', key='-SLIDER_D-',
                                                             enable_events=True, disable_number_display=True), sg.Text('0', size=(4, 1), key='-S_D-')],
            [sg.Text("Sagesse :", size=(10, 1)), sg.Slider((0, 20), orientation='h', key='-SLIDER_S-',
                                                           enable_events=True, disable_number_display=True), sg.Text('0', size=(4, 1), key='-S_S-')],
            [sg.Text("Constitution :", size=(10, 1)), sg.Slider((0, 20), orientation='h', key='-SLIDER_CO-',
                                                                enable_events=True, disable_number_display=True), sg.Text('0', size=(4, 1), key='-S_CO-')],
            [sg.Text("Charisme :", size=(10, 1)), sg.Slider((0, 20), orientation='h', key='-SLIDER_CH-',
                                                            enable_events=True, disable_number_display=True), sg.Text('0', size=(4, 1), key='-S_CH-')]
        ]

        # --- Window Layout ---
        self.layout1 = [
            [sg.Menu(self.menu, tearoff=False, key='-MENU-')],
            [sg.Text('CRÉATEUR DE PERSONNAGE', size=(25, 1),
                     justification='center', font=(FONT, 30, 'bold'), key='-TITLE-', relief='raised')],
            [sg.Column(self.base_col, justification='left', key='-BASE-COL-', expand_x=True), sg.VerticalSeparator(pad=((7, 7), (0, 0))), sg.Column(
                self.image_col, element_justification='center', justification='center', expand_x=True, key='-IMAGE-COL-')],
        ]
        self.layout2 = [
            [sg.Column(self.appearance_col, justification='center',
                       key='-APPEARANCE-COL-')],
            [sg.Column(self.stats, element_justification='left', justification='left', expand_x=True)]
        ]
        self.layout3= [
           [sg.Canvas(size=(300, 300), key='-CANVAS-')]
        ]

        # Window
        self.window1 = sg.Window('Créateur de personnage 1',
                                self.layout1, margins=(5, 5), font=(FONT, 14), resizable=True, finalize=True)
        self.window2 = sg.Window('Créateur de personnage 2', self.layout2, margins=(5, 5), font=(FONT, 14), resizable=True, finalize=True)
        self.window3 = sg.Window('Créateur de personnage 3', self.layout3, margins=(5, 5), font=(FONT, 14), resizable=True, finalize=True)
        self.windows = [self.window1, self.window2, self.window3]

        self.window1.move(self.window1.current_location()[0]-200, self.window1.current_location()[1]-150)
        self.window3.move(self.window1.current_location()[0]+400, self.window1.current_location()[1]-300)
        self.window2.move(self.window1.current_location()[0], self.window1.current_location()[1]+300)
        

        # --- Expanding things ---
        self.expand_objets()

        # -- Graph --
        self.stats_keys = ['-S_F-', '-S_I-',
                           '-S_D-', '-S_S-', '-S_CO-', '-S_CH-']
        self.slider_keys = ['-SLIDER_F-', '-SLIDER_I-',
                            '-SLIDER_D-', '-SLIDER_S-', '-SLIDER_CO-', '-SLIDER_CH-']
        self.ax, self.fcg = None, None
        self.initialize_graph()

    def initialize_graph(self):
        """Initializes our graph part on the window"""
        data = [0, 0, 0, 0, 0, 0]
        self.ax = radar_graph(data)
        fig = plt.gcf()
        fig.set_size_inches(4, 4)
        self.fcg = FigureCanvasTkAgg(
            fig, master=self.window3['-CANVAS-'].TKCanvas)
        self.window3.move(self.window1.current_location()[0]+400, self.window1.current_location()[1]-300)
        self.fcg.draw()
        self.fcg.get_tk_widget().pack(side='right', fill='both', expand=1)
        self.fcg.flush_events()

    def update_graph(self, values):
        """Updates the statistics graph"""
        # Updating statistics values
        for key in range(len(self.stats_keys)):
            self.window2[self.stats_keys[key]].update(
                int(values[self.slider_keys[key]]))

        self.ax.clear()
        data = [int(values[key]) for key in self.slider_keys]
        self.ax = radar_graph(data)
        fig = plt.gcf()
        self.fcg.draw()
        self.fcg.flush_events()

    def loop(self):
        """The loop of our program that handles the different possible events 
        in the GUI"""
        while True:
            window, event, values = sg.read_all_windows()

            # -- Quiting the window --
            if event in (sg.WIN_CLOSED, 'Exit'):
                break

            # -- Image browsing --
            if event == '-IMGBROWSE-':
                filename = values['-IMGBROWSE-']
                if filename:
                    self.window1['-IMAGE-'].update(
                        data=convert_to_bytes(filename, resize=(200, 200)))
                    self.window1['-TITLE-'].justification = 'center'

            # -- Values filtering in entries --
            if event in ('-XP-', '-LVL-', '-AGE-'):
                if event == '-XP-' and values['-XP-'] and (values['-XP-'][-1] not in ('0123456789-')):
                    self.window1['-XP-'].update(values['-XP-'][:-1])
                if event == '-LVL-' and values['-LVL-'] and (values['-LVL-'][-1] not in ('0123456789-')):
                    self.window1['-LVL-'].update(values['-LVL-'][:-1])
                if event == '-AGE-' and values['-AGE-'] and (values['-AGE-'][-1] not in ('0123456789-')):
                    self.window2['-AGE-'].update(values['-AGE-'][:-1])

            # -- Menu font change  --
            if event == 'Papyrus':
                self.update_window_font('Papyrus')
            if event == 'Comic Sans MS':
                self.update_window_font('Comic Sans MS')

            # -- Updating graph --
            if event in self.slider_keys:
                self.update_graph(values)

        # Closing window if the loop broke
        self.window1.close(), self.window2.close(), self.window3.close()

    def expand_objets(self):
        """Expand all objets in our window to 
        create a smooth GUI"""
        key_list = ['-IMAGE-COL-', '-TITLE-', '-BASE-COL-']
        for key in key_list:
            self.window1[key].expand(expand_x=True)

        for sublist in self.base_col:
            for obj in sublist:
                obj.expand(expand_x=True)

    def update_window_font(self, font):
        """Updates the window font with the one specified"""
        for element in list(itertools.chain.from_iterable(self.image_col + self.base_col + self.stats + self.appearance_col)):
            try:
                element.update(font=(font, 14))
            except:
                pass
        for element in list(itertools.chain.from_iterable(self.layout1 + self.layout2 + self.layout3)):
            try:
                element.update(font=(font, 14))
            except:
                pass
        
        self.window1['-TITLE-'].update(font=(font, 20, 'bold'))


if __name__ == '__main__':
    character_creator = CharacterCreator()
    character_creator.loop()
