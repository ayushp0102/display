import pygame
from time import sleep

running = True

pygame.init()
pygame.mouse.set_visible(False)
screen = pygame.display.set_mode((0,0), 680*480)
screen.fill(pygame.Color(0,0,0))
imgsize = pygame.Surface.get_size(screen)

def image_fade(image_name): #can use this to enable the fading effect.
            background = pygame.image.load(image_name)
            background = pygame.transform.scale(background,(imgsize[0],imgsize[1])).convert() #adding .convert() greatly increases the speed

            for x in range(0,255):
                background.set_alpha(x)
                #screen.fill(pygame.Color(0,0,0))
                screen.blit(background, (0, 0))
                pygame.display.update()
                x += 5 #increase the step size for faster transitions
while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
        	if event.key==pygame.K_1:
			#image_fade("1.jpg") #uncomment to enable the fading effect
			background = pygame.image.load("1.jpg").convert() #comment it out for fading 
        	if event.key==pygame.K_2:
			#image_fade("2.jpg")
			background = pygame.image.load("2.jpg").convert()
        	if event.key==pygame.K_3:
			#image_fade("3.jpg")
			background = pygame.image.load("3.jpg").convert()
                screen.blit(background, (0, 0))  #comment it out for fading
                pygame.display.update() #comment it out for fading
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
