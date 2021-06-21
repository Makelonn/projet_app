# Ursina 3D

## Utilisation du Framework 

### 1. Ouvrir une fenêtre

```py
app = Ursina()
window.title = 'My fucking game'        # The window title
window.borderless = False               # Show a border
window.fullscreen = False               # Do not go Fullscreen
# Do not show the in-game red X that loses the window
window.exit_button.visible = False
# Show the FPS (Frames per second) counter
window.fps_counter.enabled = True
```
### 2. Gestion de la souris

### 3. Gestion du clavier
```py
held_keys['d']
```
<p>
&ensp;&ensp;&ensp;&ensp;
Retourne 1 ou 0 si la touche est enfoncée.
</p>

### 4. Gestion des frames

<p>
&ensp;&ensp;&ensp;&ensp;
Le framework ne gère pas l'affichage par frame, l'affichage se fait automatiquement. 
</p>

### 5. Gestion de la lumière 

Il existe différent type de lumière selon ce que l'on souhaite faire (directionnelle, projecteur, ambiante). On peut positionner la source lumineuse ou l'on veut.

### 6. Evaluation des performances

Les performances d'Ursina sont plutot bonne, mais il reste quelques soucis notamment à l'affichage des colliders (s'ils sont trop détaillé et affiché ils font chauffer même de très bonne carte graphique).

### 7. Faire un cube / sphère / heptatriacontaèdre

Créer une forme simple est très simple puisque des modèles sont déjà disponible.

### 8. Bouger la caméra

L'utilisation de la caméra éditeur peut suffir dans la plupart des cas.

### 9. Faire bouger une forme géométrique
- ### 9.1 En Translation

```py
player.x += held_keys['d'] * .1
player.x -= held_keys['q'] * .1
player.y += held_keys['z'] * .1
player.y -= held_keys['s'] * .1
```
<p>
&ensp;&ensp;&ensp;&ensp;
<i>Player</i> est une <strong> Entity </strong>.
Ici le joueur se déplace à l'aide des touches ZQSD.
</p>

- ### 9.2 En Rotation
- 
```py
player.rotation_y = player.rotation_y + time.dt*100
```
<p>
&ensp;&ensp;&ensp;&ensp;
La rotation du <i>player</i> est gérée par une varible que l'on incrémente au cours du temps. On peut imaginer tourner dans l'autre sens en le décrémentant. 
</p>

### 10. Déformer une forme géo

On peut déformer les formes selons x,y,z assez facilement grâce à l'attribut `scale`.

### 11. Faire une forme complexe

On peut créer des formes complexes en ajoutant plusieurs entités et les faisant se suivre.

### 12. Gestion des formes complexes

Les formes complexes ne se suivent pas forcément automatiquement : pour la création d'un personnage par exemple, il a fallut faire une fonction d'update des membres du personnage avant qu'ils suivent le corps. De plus, mettre certaines relations entre les objets changent les axes de rotations et cela peut vite devenir un casse tête pour les faire se déplacer dans l'espace.

### 13. Gestion des groupements de formes

&ensp;&ensp;&ensp;&ensp;
Il faut utiliser la relation parent des objets <strong> Entity </strong>, et parfois des petites manipulations en plus.


### 14. Importer un modèle 3D (au format opensource ?)

```py
girl = load_model("girl.obj", path=asset_folder, file_types=(
    '.bam', '.ursinamesh', '.obj', '.glb', '.gltf', '.blend'))
player = Entity(model=girl, position=0,
                scale=10, double_sided=True) 
```
<p>&ensp;&ensp;&ensp;&ensp;
Ici <i> girl </i> est un <strong> Model </strong> pour générer une <strong> Entity </strong>.
</p>

- ### 14.1 Gestion des fichiers d'assets

```py
root_folder = Path(__file__).parent.parent
asset_folder = root_folder / 'asset/'
```
<p>&ensp;&ensp;&ensp;&ensp;
Les chemins d'accès aux fichiers pour les fonctions de load doivent obligatoirement être un objet <strong> Application </strong> et donc être décrit à l'aide des fonctions Ursina.
</p>

### 15. Compatibilité des modèles 3D / facilité à les utiliser

Les fichiers au format OBJ sont faciles à importer, mais les fichiers de textures `mtl` ne sont pas encore implémentés (mais c'est en cours). Les fichiers blender nécessitent une conversion, et donc d'avoir Blender d'installé. Ceci dit, la conversion ne se fait qu'une fois et n'est plus nécessaire par la suite.

### 16. Gestion des collisions

La gestion des collisions se fait très facilement grâce aux `collider` et aux fonctions de `raycast` et `boxcast`. Cependant, c'est assez compliqué de faire quelque chose de précis, et il y a besoin de faire des petits réglages grâce à des test (il y a probablement des façons plus simple et plus propre de prévues, mais sans documentation, ce serait trop chronovore de les rechercher).

### 17. Faire bouger une forme par rapport à une autre 
- ### 17.1. Un bras qui bouge 
- ### 17.2. Une planète qui orbite
```py
from ursina import *

app = Ursina()
window.title = 'My fucking game'                # The window title
window.borderless = False               # Show a border
window.fullscreen = False               # Do not go Fullscreen
# Do not show the in-game red X that loses the window
window.exit_button.visible = False
# Show the FPS (Frames per second) counter
window.fps_counter.enabled = True

sun = Entity(model='sphere', position=0,
             scale=20, double_sided=True)
rota_planet1 = Entity(position=0)
planet1 = Entity(model='sphere', position=(0, 50, 0),
                 scale=5, double_sided=True, parent=rota_planet1)
rota_planet2 = Entity(position=0)
planet2 = Entity(model='sphere', position=(0, 30, 0),
                 scale=3, double_sided=True, parent=rota_planet2)
rota_moon1 = Entity(position=planet1.get_position())
moon1 = Entity(model='sphere', position=planet1.get_position()+(0, -40, 0),
               scale=2, double_sided=True, parent=rota_moon1)
EditorCamera()
camera.orthographic = True

def update():   # update gets automatically called.

    rota_planet1.rotation_z = rota_planet1.rotation_z + 0.5*time.dt*100
    rota_planet2.rotation_z = rota_planet2.rotation_z + 1*time.dt*100

    rota_moon1.set_position(planet1.get_position(), relative_to=scene)
    rota_moon1.rotation_z = rota_moon1.rotation_z + 1.5*time.dt*100

    sun.rotation_z = sun.rotation_z + time.dt*100
    planet1.rotation_z = planet1.rotation_z + time.dt*100
    planet2.rotation_z = planet2.rotation_z + time.dt*100

app.run()   # opens a window and starts the game.

```
### 19. Créer un sol 

On peut créer un sol de 2 façons :
- Avec un objet de sol, de préférence avec une épaisseur (pour éviter les lags/bugs ou on tombe dans le sol)
- En limitant la hauteur des joueurs

```py
    def jmp(self):
        if self.in_air:
            self.y += self.jmp_force * ur.time.dt
            self.jmp_force -= self.acc
            if self.y <= +1:
                self.in_air = False
                self.y = +1
                self.jmp_force = self.base_jmp_force
```

### 20. Importer des textures
```py
my_texture = load_texture("bot color.jgp", path=texture_folder)
player = Entity(model=girl, position=0,
                scale=10, double_sided=True, texture=my_texture)
```
<p>
&ensp;&ensp;&ensp;&ensp;
Les textures sont des objets de type <strong>Texture</strong> passé en paramètre à des <strong> Entity </strong>. Les fichiers décrivant la répartition des textures sur un <strong> Entity </strong> sont appelé ".mtl" et sont en cours de développement d'après le créateur du framework.
</p>

- ### 20.1 Gestion des fichiers de textures
```py
root_folder = Path(__file__).parent.parent
texture_folder = root_folder / 'texture/'
```
<p>&ensp;&ensp;&ensp;&ensp;
Les chemins d'accès aux fichiers pour les fonctions de load doivent obligatoirement être un objet <strong> Application </strong> et donc être décrit à l'aide des fonctions Ursina.
</p>


## Impressions globales sur le Framework

### Avantages

- Ursina permet de coder en très peu de ligne des jeux en 3D très joli (petit Minecraft par exemple)
- La création d'objet "entité" et leur manipulation simple est facile à prendre en main
- Les collisions sont déjà intégrées dans le jeu
- On peut charger des modèles déjà existants
- Il existe un serveur discord ou le développeur ainsi que d'autres personnes répondent aux questions et proposent des solution rapidemment
- Le site d'Ursina fournit des exemple de jeu qui peuvent remplacer une partie de la documentation

### Désavantages

- La documentation est trop peu fournie, et la plupart des option ne sont pas expliquées
- Il y a des options citées dans la documentations que nous n'avons jamais réussi a mettre en place
- Certains rendus ne sont pas les même selon les machines, même si elles sont sur le même OS
- Certaines choses sont compliquées a prendre en main, notamment à cause du manque de documentation

### Conclusion

Ursina est très efficace, et la plupart des outils sont facile à prendre en mains, du moins si on ne cherche pas à exploiter toutes les spécificités. En revanche, du fait du manque de documentation, il est très difficile d'exploiter Ursina à son plein potentiel. Les codes de jeux qui sont disponible sur le site, et l'aide offerte par le serveur discord permettent de s'en sortir, mais commencer et faire son premier projet Python en utilisant Ursina engine parait compliqué voir impossible.