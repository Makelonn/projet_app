# Panda 3D
## Utilisation du Framework 

De façon générale, Panda3D est un framework très complet et qui permet de faire à peu près ce qu'on veut, si on trouve les bons outils pour le faire. La documentation est très vaste et par conséquent impossible à appréhender seul, et l'utilisation d'un tutoriel semble être la meilleure façon de comprendre les fonctionnements basiques. 

### 1. Ouvrir une fenêtre

En utilisant une instance de `Showbase` (ou en faisant hériter le main de la classe), il suffit de faire `my_main.run()`pour lancer une fenetre.

### 2. Gestion de la souris

La souris se gère grâce à la fonction `accept`de showbase. Le fonctionnement que nous avons utiliser est d'avoir un dictionnaire qui contient `clé : status` (`True` si activé, `False` sinon). Grâce à la fonction `accept`, on va modifier le statut selon si la touche est abaissée ou relevée.

Même si le fonctionnement n'est pas très technique en soit, sans utiliser le dictionnaire il est beaucoup plus compliqué de gérer la souris. 

### 3. Gestion du clavier

Le clavier fonctionnement exactement comme la souris, puisque panda3d ne fait pas de différence entre les boutons du clavier et de la souris. 

### 4. Gestion des frames
### 5. Gestion de la lumière 
### 6. Evaluation des performances
### 7. Faire un cube / sphère / heptatriacontaèdre
### 8. Bouger la caméra

La caméra est un objet de `Showbase`, et comme sur Ursina, on peut utiliser les fonctions `setPos` ou `setHPR`(la rotation). Par conséquent, il est assez facile de l'utiliser une fois qu'on a compris qu'elle était déjà existante dans `Showbase`.

### 9. Faire bouger une forme géométrique
- ### 9.1 En Translation

Pour faire bouger un `Actor`, qui sont les entités générées à partir d'un modèle `.egg`, on peut utiliser les fonctions `setPos` ou `setX`, ... La difficulté est de trouver comment utiliser l'horloge (là ou Ursina le proposait directement), pour maintenir une vitesse constante, qui ne dépend pas de l'execution sur la machine. 

- ### 9.2 En Rotation

La rotation se gère de la même façon que la translation avec `setHPR`, ou `setH`, ...

### 10. Déformer une forme géo
### 11. Faire une forme complexe
### 12. Gestion des formes complexes
### 13. Gestion des groupements de formes
### 14. Importer un modèle 3D (au format opensource ?)

Il est assez facile d'importer les `.egg`, et les animations qui vont avec, à la création d'un `Actor`. 

### 15. Compatibilité des modèles 3D / facilité à les utiliser
### 16. Gestion des collisions

La gestion des collisions est fastidieuse: il faut non seulement créer un collider pour chaque Actor/ Objet, mais il faut les ajouter dans des gestionnaires dans des variables globales. Il faut aussi choisir un gestionnaire d'évènement, et on peut en avoir plusieurs à la fois. Sans un tutoriel, il est quasimment impossible de réussir à faire fonctionner les collisions, du moins, sans y passer une éternité. 

### 17. Faire bouger une forme par rapport à une autre 
- ### 17.1. Un bras qui bouge
- ### 17.2. Une planète qui orbite
```py
```
### 19. Créer un sol 
```py
```
### 20. Importer des textures
```py
```
## Impressions globales sur le Framework

### Avantages

Panda3D est un framework très complet, qui offre de nombreuses classes et méthodes, et qui est bien documenté. De plus le Framework est stable et nous n'avons observé aucun comportement aléatoire pendant nos tests. 

Le Framework étant reconnu et très utilisé, on trouve aussi de nombreuses ressources en ligne, que ce soit des tutoriels, du code, ou même des questions/réponses sur les forums.

C'est un framework qui est destiné à de gros projets en 3D, notamment grâces à ses très nombreuses possibilité qui lui permette d'être très pointu dans son domaine.
### Désavantages

La documentation est si large qu'elle en est indigeste par elle même : c'est une documentation ou l'on va chercher quelque chose en particulier, mais par une documentation qui permet de se familiariser avec le framework. L'utilisation de panda3D est fortement limité par les connaissance préalable en modélisation 3D de jeu : si n'avions pas utilisé Ursina avant, il est fort possible que nous n'aurions pas réussi a faire fonctionner quelque chose sans copier coller un tutoriel.

Par exemple, beaucoup d'objet nécessite d'utiliser des fonctions très spécifiques de la classes ainsi que des variables globales, et il est très compliqué d'en avoir l'intuition, et même avec des explications, certains fonctionnements restent obscurs.

A la différence de Ursina, panda3D ne fournit pas d'objet prédéfini comme des sphères, et cela implique donc de devoir utiliser des modèles 3D directement. Le format de modèle 3D étant les `.egg`, ils ne sont pas particulièrement faciles à trouver sur internet.

### Conclusion
