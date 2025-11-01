import pygame
from sys import exit

pygame.init() #pygame initialize 

screen = pygame.display.set_mode((800, 400)) # width and height of the screen
pygame.display.set_caption("Runner Game")
clock = pygame.time.Clock()
test_font = pygame.font.Font('font/Pixeltype.ttf', 50) # font type for our text

sky_surface = pygame.image.load("graphics/Sky.png").convert()
ground_surface = pygame.image.load("graphics/ground.png").convert()
test_surface = test_font.render("Fidan's Game", False, "Black") #text surface #antialiasing (where working with pixel art to we choose False)
snail_surface = pygame.image.load("graphics/snail/snail1.png").convert_alpha()
snail_x_pos = 600
snail_y_pos = 250
player_surf = pygame.image.load("graphics/Player/player_walk_1.png").convert_alpha()
player_rect = player_surf.get_rect(midbottom =(80,300))
snail_rect = snail_surface.get_rect(midbottom = (600,300))

#loop for the game to run
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() #this is the opposite action on pygame.init()
            exit()
    screen.blit(sky_surface, (0,0))
    screen.blit(ground_surface, (0,300))
    screen.blit(test_surface,(300,100)) #(x,y) position of the text
    screen.blit(snail_surface,snail_rect)
    screen.blit(player_surf,player_rect)
    snail_x_pos -= 4 #increase the x position of the snail by 1 each frame
    if snail_x_pos < -100: #if the snail is off the screen
        snail_x_pos = 800
    

    pygame.display.update()
    clock.tick(60) 