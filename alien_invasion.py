import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from alien import Alien
from pygame.sprite import Group
from game_stats import GameStats
from button import Button
from scoreboard import ScoreBoard
def run_game():
    #Initialize game and create  a screen object
    pygame.init()
    ai_settings=Settings()


    #Make a group that stores bullet
    #Make an alien





    screen=pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))

    #Create an instance to store game statistics and create a scoreboard
    stats=GameStats(ai_settings)
    sb=ScoreBoard(ai_settings,screen,stats)
    #set the background color.
    bg_color=(230,230,230)
    #Start the main cloop for the game
    #Make a Ship
    ship=Ship(ai_settings,screen)
    alien=Alien(ai_settings,screen)
    bullets=Group()
    aliens=Group()
    #Make the play button
    play_button=Button(ai_settings,screen,"Play")
    #Create a fleet of aliens
    gf.create_fleet(ai_settings,screen,ship,aliens)
    while True:

        gf.check_events(ai_settings,screen,stats,sb,play_button,ship,aliens,bullets)
        if stats.game_active:


            ship.update()
            bullets.update()
            gf.update_bullets(ai_settings,screen,stats,sb,ship,aliens,bullets)
            gf.update_aliens(ai_settings,screen,stats,sb,ship,aliens,bullets)



        #get rid of bullets that have disappeared
        for bullet in bullets.copy():
            if bullet.rect.bottom<=0:
                bullets.remove(bullet)
        print(len(bullets))



        #Watch for keyboard and mouse events.
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit()



        #mAKE THE MOST RECENTLY DRAWN SCREEN VISIBLE
        #redraw the screen during each pass through the VISIBLE
        screen.fill(ai_settings.bg_color)
        ship.blitme()

        pygame.display.flip()
        gf.update_screen(ai_settings,screen,stats,sb,ship,aliens,bullets,play_button)

run_game()
