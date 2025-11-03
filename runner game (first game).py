import pygame
from sys import exit

pygame.init() #pygame initialize 

screen = pygame.display.set_mode((800, 400)) # width and height of the screen
pygame.display.set_caption("Runner Game")
clock = pygame.time.Clock()
test_font = pygame.font.Font('font/Pixeltype.ttf', 50) # font type for our text

sky_surface = pygame.image.load("graphics/Sky.png").convert()
ground_surface = pygame.image.load("graphics/ground.png").convert()
 #text surface #antialiasing (where working with pixel art to we choose False)
snail_surf = pygame.image.load("graphics/snail/snail1.png").convert_alpha()

score_surf = test_font.render("Score", False, "Black")
score_rect = score_surf.get_rect(center = (400, 50))


snail_y_pos = 250
player_surf = pygame.image.load("graphics/Player/player_walk_1.png").convert_alpha()
player_rect = player_surf.get_rect(midbottom =(80,300))
snail_rect = snail_surf.get_rect(midbottom = (600,300))



#loop for the game to run
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() #this is the opposite action on pygame.init()
            exit()
        #if event.type == pygame.MOUSEMOTION:
            #if player_rect.collidepoint(event.pos): print('collision')
            

    screen.blit(sky_surface, (0,0))
    screen.blit(ground_surface, (0,300)) # the bottom of the must be 
    #the same with the bottom of the surface
    #screen.blit(text_surface,(300,100)) #(x,y) position of the text
    pygame.draw.rect(screen, 'Pink', score_rect)
    #pygame.draw.rect(screen, 'Pink', score_rect, 10)
    pygame.draw.rect(screen, 'Pink', score_rect.inflate(10, 10), 10)
    #pygame.draw.line(screen, 'Gold', (0,0), (800,400), 10)
    pygame.draw.ellipse(screen, 'Brown', pygame.Rect(50,200,100,100) )

    snail_rect.x -= 4
    if snail_rect.right <=0:  snail_rect.left = 800 #800 is the right side of the screen(line 6)
    screen.blit(snail_surf,snail_rect)
    screen.blit(player_surf,player_rect)
    screen.blit(score_surf, score_rect)
    

    #if player_rect.colliderect(snail_rect):
        #print('collision')
    # if there is a collision we get 1 (true)
    # if there is no collision we get 0 (false)

    #get the position of the mouse
    #mouse_pos = pygame.mouse.get_pos() 
    #if player_rect.collidepoint(mouse_pos):
        # the bollean value for each of my mouse buttons
        #print(pygame.mouse.get_pressed()) #shows which mouse buttons pressed

    

    pygame.display.update()
    clock.tick(60) 