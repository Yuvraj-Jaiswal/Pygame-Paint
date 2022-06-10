import pygame
from pygame.locals import *
pygame.init()

def Get_mouse_position():

    colors = [(255,0,0),(0,255,0),(0,0,255),(255,255,255)]
    start = True
    i = 0
    while True:
        key = pygame.key.get_pressed()
        mouse = pygame.mouse.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT or key[K_ESCAPE]:
                pygame.quit()

            if key[K_SPACE]:
                if i==len(colors)-1:i = 0
                else:i += 1

            clr = colors[i]

            if mouse[0]:
                x, y = pygame.mouse.get_pos()
                pygame.draw.rect(Screen,clr,(x,y,10,10))

            if mouse[2]:
                Screen.fill((255,255,255))

        if start :
            Screen.fill((255, 255, 255))
            start = False

        pygame.draw.rect(Screen,(255,255,255),(0,0,0,0))
        pygame.display.update()



#--------------------------------------------------------------------------------------------------------

sw = 1000
sh = 500
Screen = pygame.display.set_mode((sw,sh))


if __name__=='__main__':

    Get_mouse_position()

