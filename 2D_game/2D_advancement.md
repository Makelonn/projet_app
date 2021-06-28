# Avancement partie 2D

## Résumé

Je me suis occupé de réaliser un petit jeu minimaliste en 2D isométrique au style RTS (sélection de plusieurs unités et affichage d'une carte). Pour réaliser ce petit jeu j'ai utilisé la librairie PySimpleGUI.

## Niveau de fonctionnalité

Le jeu affiche une carte ainsi que 10 unités qui se déplacent de manière aléatoire dans la carte. Nous pouvons nous déplacer dans la carte à l'aide des flèches directionnelles. Nous pouvons sélectionner une unité à l'aide d'un unique clic gauche ou sélectionner un groupe d'unité en laissant le clic gauche enfoncé et en faisant glisser la souris jusqu'à ce que toutes les unités voulues rentrent dans le cadre. En appuyant sur le clic droit les unités, sélectionnés au préalable, se déplacent en ligne droite jusqu'à la position du clic. Si plusieurs unités sont selectionnés elles garderont leur formation initiale pour éviter qu'elles ne se superposent.

## Documentation

PySimpleGUI possède une documentation très fournie pour réaliser des interfaces utilisateurs, elle guide l'utilisateur pas à pas sur les outils utilisables et le fonctionnement de ces derniers. Cependant, au fur et à mesure que nous progressons dans la documentation elle devient de moins en moins fournie et beaucoup d'utilisations ne sont pas indiquées. En effet, arrivés à un certain point seule l'utilisation principale est mentionnée et il faut alors souvent comprendre comment l'élément fonctionne grâce à la documentation de TKinter. Malgrè ce petit point négatif, beaucoup de projets variés sont mis en avant dans la documentation que ça soit un simple mélangeur de volume ou un petit jeu comme pong. Cela permet d'avoir de premières pistes sur quels outils utilisés. Pour comparer avec la documentation de Pygame que j'avais utilisé lors du projet python, il est clair que celle de PySimpleGUI est supérieure car bcp plus guidée et non pas simplement une liste de fonction.

## Facilité de débugage / réalisation

- Le framework peut être assez compliqué à débuguer. En effet, les erreurs ne sont pas bien indiquées. Ces dernières apparaissent souvent dans le terminal au niveau même du programme PySimpleGUI. De ce fait, cela peut être assez compliqué de déterminer d'où provient l'erreur. De plus, si le développeur écrit mal un paramètre aucun crash ne surviendra mais le paramètre ne sera simplement pas appliqué. Ce qui fait que l'on peut chercher longtemps pourquoi telle ou telle fonctionnalité ne fonctionne pas de la manière voulue à cause d'une faute de frappe qui ne saute pas immédiatement aux yeux.
- Le framework permet d'avancer très rapidement et d'obtenir très vite des résultats. En effet, la création d'une fenêtre et la mise en place des premiers éléments est très facile et détaillé dans la documentation. En particulier pour la partie jeu, il est très facile de créer des éléments graphique, de les déplacer et de les supprimer. La gestion par évènements du framework est particulièrement bien adapté à un jeu et permet de récupérer très facilement les interactions de l'utilisateur. Pour comparer avec mon expérience de Pygame, ce framework m'a l'air plus simple à prendre en main que Pygame et permet de réaliser plus efficacement la plupart des fonctionnalités attendues. Il est cependant possible que la réalisation de features très avancées soit plus simple à réaliser avec Pygame mais je n'ai pas rencontré ce cas lors de mes différents tests.

## Stabilité de l'ensemble

Je n'ai rencontré aucun problème de stabilité ou de crash inexpliqué lors de mes différents tests. De plus lors de mes tests de performances le framework m'a paru stable et performant.

## Degré de liberté pour la personnalisation

Le degré de liberté pour la personnalisaiton me parait important. Cependant, il est possible qu'il faille récupérer les modules TKinter pour réaliser précisément ce que nous voulons. Par exemple, je n'ai pas encore trouvé comment mettre un élément de type Graph en plein écran. Nous ne pouvons pas non plus modifier la transparence d'une forme de manière simple. En effet, TKinter ne propose pas nativement de pouvoir modifier le canal alpha d'une image. Il faut donc soit préparer l'image au préalable en fixant la transparence soit utiliser d'autres framework.

## Impression générale

Il me semble que ce framework est particulièrement adapté pour réaliser un petit jeu vidéo. En effet, le framework est plutôt simple à utiliser et de ce fait, la difficulté du projet repose sur la conception des fonctionnalités et pas sur l'utilisation du framework ce qui est un plus. Même si certains aspects ne sont, à mon avis, pas bien documentés les différents projets disponible sur github et les issues du projet permettent de bien progresser dans l'apprentissage et l'utilisation du framework. La grosse force du framework est la facilité de réaliser une interface utilisateur et de lier l'ensemble, de récupérer les intéractions utilisateur. Cependant, pour des gros projets, le framework me parait limité notamment dans l'affichage d'éléments, et il me semble plus intéressant de se diriger vers des frameworks destiné à faire des jeux comme pygame qui sont néanmoins plus long à prendre en main.
