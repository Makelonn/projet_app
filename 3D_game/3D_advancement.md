# Ursina 3D

### 1. Ouvrir une fenêtre<br>
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
### 2. Gestion de la souris<br>
### 3. Gestion du clavier<br>
```py
held_keys['d']
```
<p>
&ensp;&ensp;&ensp;&ensp;
Retourne 1 ou 0 si la touche est enfoncée.
</p>

### 4. Gestion des frames<br>
<p>
&ensp;&ensp;&ensp;&ensp;
Le framework ne gère pas l'affichage par frame, l'affichage se fait automatiquement. <br>
</p>

### 5. Gestion de la lumière ?<br>
### 6. Evaluation des performances<br>
### 7. Faire un cube / sphère / heptatriacontaèdre<br>
### 8. Bouger la caméra<br>
### 9. Faire bouger une forme géométrique<br>
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
```py
player.rotation_y = player.rotation_y + time.dt*100
```
<p>
&ensp;&ensp;&ensp;&ensp;
La rotation du <i>player</i> est gérée par une varible que l'on incrémente au cours du temps. On peut imaginer tourner dans l'autre sens en le décrémentant. 
</p>

### 10. Déformer une forme géo<br>
### 11. Faire une forme complexe<br>
### 12. Gestion des formes complexes<br>
### 13. Gestion des groupements de formes<br>
<p>&ensp;&ensp;&ensp;&ensp;
Il faut utiliser la relation parent des objets <strong> Entity </strong>.
</p>

### 14. Importer un modèle 3D (au format opensource ?)<br>
```py
girl = load_model("girl.obj", path=asset_folder, file_types=(
    '.bam', '.ursinamesh', '.obj', '.glb', '.gltf', '.blend'))
player = Entity(model=girl, position=0,
                scale=10, double_sided=True) 
```
<p>&ensp;&ensp;&ensp;&ensp;
Ici <i> girl </i> est une <strong> Model </strong> pour générer une <strong> Entity </strong>.
</p>

- ### 14.1 Gestion des fichiers d'assets
```py
root_folder = Path(__file__).parent.parent
asset_folder = root_folder / 'asset/'
```
<p>&ensp;&ensp;&ensp;&ensp;
Les chemins d'accès aux fichiers pour les fonctions de load doivent obligatoirement être un objet <strong> Application </strong> et donc être décrit à l'aide des fonctions Ursina.
</p>

### 15. Compatibilité des modèles 3D / facilité à les utiliser<br>
### 16. Gestion des collisions<br>
### 17. Faire une pièce et s’y déplacer<br>
### 18. Faire bouger une forme par rapport à une autre <br>
- ### 18.1. Un bras qui bouge <br>
- ### 18.2. Une planète qui orbite<br>
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
### 19. Créer un sol <br>
### 20. Gestion des caméras (FPS, 3ème personne)<br>
### 21. Importer des textures<br>
```py
my_texture = load_texture("bot color.jgp", path=texture_folder)
player = Entity(model=girl, position=0,
                scale=10, double_sided=True, texture=my_texture)
```
<p>
&ensp;&ensp;&ensp;&ensp;
Les textures sont des objets de type <strong>Texture</strong> passé en paramètre à des <strong> Entity </strong>. Les fichiers décrivant la répartition des textures sur un <strong> Entity </strong> sont appelé ".mtl" et sont en cours de développement d'après le créateur du framework.
</p>

- ### 21.1 Gestion des fichiers de textures
```py
root_folder = Path(__file__).parent.parent
texture_folder = root_folder / 'texture/'
```
<p>&ensp;&ensp;&ensp;&ensp;
Les chemins d'accès aux fichiers pour les fonctions de load doivent obligatoirement être un objet <strong> Application </strong> et donc être décrit à l'aide des fonctions Ursina.
</p>


## Obstacles

- Documentation gives a list of model but some of them seems to not work 
- Text display is easy, auto \n
- Rotation coordonate and parent is a bit hard to understand