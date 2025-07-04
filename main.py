import pygame
print("Setup Start")
pygame.init()
LARGURA_DA_TELA = 600
ALTURA_DA_TELA = 480
screen = pygame.display.set_mode(size=(LARGURA_DA_TELA, ALTURA_DA_TELA))
print("Setup End")

print("Loop Start")
while True:
    # Check for all events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() # Close Window
            print("Quitting...")
            quit() #end py game
