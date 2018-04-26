import pygame, sys
from pygame import *

def main():
    
    pygame.init()
    DISPLAY = pygame.display.set_mode((400,300))
    pygame.display.set_caption("Explorer")
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
        
main()
