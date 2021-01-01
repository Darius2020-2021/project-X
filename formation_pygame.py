import pygame
import time
pygame.init()
pygame.display.set_caption("formation")
window= pygame.display.set_mode((1000,650))
color= (255, 255, 255)
color_black= (0, 0 , 0)
arial= pygame.font.SysFont("arial", 40, True)
texte= arial.render("salut tout le monde", True, color_black)
musique= pygame.mixer.Sound("music.mp3")
musique.play(0, 0, 5000)
quitter= True
while quitter :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quitter = False
        elif event.type == pygame.MOUSEMOTION:
            print("{}".format(event.pos))     
    
    pygame.display.flip()
