# Avancement partie 2D

## Résumé

Je me suis occupé de réaliser un petit jeu minimaliste en 2D isométrique au style RTS (sélection de plusieurs unités et affichage d'une carte). Pour réaliser ce petit jeu j'ai utilisé la librairie PySimpleGUI.

## Niveau de fonctionnalité

Le jeu affiche une carte ainsi que 3 unités. Nous pouvons nous déplacer dans la carte à l'aide des flèches directionnelles. Nous pouvons sélectionner une unité à l'aide d'un unique clic gauche ou sélectionner un groupe d'unité en laissant le clic gauche enfoncé et en faisant glisser la souris jusqu'à ce que toutes les unités voulues rentrent dans le cadre. En appuyant sur le clic droit les unités, sélectionnés au préalable, se déplacent en ligne droite jusqu'à la position du clic. Si plusieurs unités sont selectionnés elles garderont leur formation initiale pour éviter qu'elles ne se superposent.

## Documentation

PySimpleGUI est très documenté pour tout ce qui est interface utilisateur, mise en place de formulaires, boutons etc... Cependant la partie jeu n'est que très peu documentée et seules les fonctionnalités de base sont évoquées. Pour réaliser la partie graphique du jeu je me suis basé sur un projet pong qui m'a guidé dans les outils que je pouvais utiliser. Pour quelqu'un qui ne sait pas trop où aller et comment faire la documentation peut poser problème.
