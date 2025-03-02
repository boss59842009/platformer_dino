from objects import *
from levels import *

pygame.init()

level1_objects = draw_level(level1)

player = Player(50, H - 90, 40, 50, 10, player_images)

level1_objects.add(player)

game = True
while game:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
    
    window.blit(bg, (0, 0))
    for obj in level1_objects:
        window.blit(obj.image, camera.apply(obj))
    camera.update(player)

    player.update(platforms)


    pygame.display.update()
    clock.tick(FPS)
