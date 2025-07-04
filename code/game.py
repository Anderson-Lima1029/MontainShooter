#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
from code.Menu import Menu

class Game:
    def __init__(self):
        pygame.init()
        LARGURA_DA_TELA = 600
        ALTURA_DA_TELA = 480
        self.window = pygame.display.set_mode(size=(LARGURA_DA_TELA, ALTURA_DA_TELA))

    def run(self):
        while True:
            menu = Menu(self.window)
            menu.run()
            # Check for all events
            # for event in pygame.event.get():
            #     if event.type == pygame.QUIT:
            #         pygame.quit() # Close Window
            #         quit() #end py game
