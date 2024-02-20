from ursina import *


app = Ursina(show_ursina_splash=False)


player = Entity(
    model ='models/entidades/entidade.obj',
    texture='models/entidades/textura/text_jogador.png',
    position=(0,0,0),
    colision = 'box'
    



)
inimigo = Entity(
    model ='models/entidades/entidade.obj',
    texture='models/entidades/textura/text_inimigo.png',
    position=(0,0,0),
    colision = 'box'
    



)
world = Entity(
    model='models/estruturas/world.obj',
    position = (0,0,0),
    colision = 'box'

)



def update():
   player.x += held_keys['d'] * time.dt  * 5
   player.x -= held_keys['a'] * time.dt  * 5
   player.z += held_keys['w'] * time.dt  * 5
   player.z -= held_keys['s']* time.dt  * 5




EditorCamera()
app.run()