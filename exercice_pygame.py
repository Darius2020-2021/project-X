
import time
pygame.init()
i = 0
taille_ecran = (1200,675)
pygame.display.set_caption("Tenis Med")
window =pygame.display.set_mode(taille_ecran)
fond_ecran = pygame.image.load("fond.jpg")
fond_ecran.convert_alpha()
color_red = (148, 49, 38)
color_blue= (41, 128, 185)
color_ball = (241, 196, 15)
rectangle_enemy= pygame.Rect(18,28, 100, 25)
rectangle_player = pygame.Rect(32 , 624, 100, 25)
ball = pygame.Rect(588, 335, 20, 20)
quitter = True
while quitter:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quitter = False
        elif event.type == pygame.MOUSEMOTION:
            print("{}".format(event.pos))
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                window.blit(fond_ecran, (0, 0))
                rectangle_player.x -= 10
                pygame.draw.rect(window, color_blue, rectangle_player)
                print("touche gauche")
            elif event.key == pygame.K_RIGHT:
                window.blit(fond_ecran, (0, 0))
                rectangle_player.x += 10
                pygame.draw.rect(window, color_blue, rectangle_player)
                print("touche droite")
            else:
                print("pas la bonne touche")
    window.blit(fond_ecran, (0,0))
    pygame.draw.rect(window, color_ball, ball)
    pygame.draw.rect(window, color_red, rectangle_enemy)
    pygame.draw.rect(window, color_blue, rectangle_player)
    pygame.display.flip()
    while i < 105 :
        time.sleep(.040)
        window.blit(fond_ecran, (0,0))
        rectangle_enemy.x += 10
        pygame.draw.rect(window, color_red, rectangle_enemy)
        ball.y += 10
        pygame.draw.rect(window, color_ball, ball)
        
        if  not ball.colliderect(rectangle_player):
            pygame.draw.rect(window, color_ball, ball)
            pygame.draw.rect(window, color_blue, rectangle_player)
        elif not ball.colliderect(rectangle_enemy) :
            pygame.draw.rect(window, color_ball, ball)
            pygame.draw.rect(window, color_red, rectangle_enemy)

        pygame.display.flip()
        i += 1
    
