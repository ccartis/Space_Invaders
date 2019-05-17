import pygame
import sys

def run_game():
    pygame.init()
    screen=pygame.display.set_mode((1200,800))
    pygame.display.set_caption("Blue sky")
    #Set background background color to sky blue
    bg_color=(0,191,255)

    #Start the main loop for the game
    while True:

        #watch for the keyboard and mouse check_events
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit()
        #Make the most recently drawn screen VISIBLE
        screen.fill(bg_color)
        pygame.display.flip()

run_game()
