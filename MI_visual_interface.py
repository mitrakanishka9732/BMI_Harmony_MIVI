import pygame
from sys import exit

pygame.init()

screen = pygame.display.set_mode((800,400))
pygame.display.set_caption("BMI/Harmony: MI Visual Interface")

clock = pygame.time.Clock()

test_surface = pygame.Surface((100,100))
test_surface.fill('Red')

pygame.draw.rect(screen,'BLUE',(500,50,200,200),2)

while True: 
	for event in pygame.event.get():
		if event.type == pygame.QUIT: 
			pygame.quit()
			exit()

	
	screen.blit(test_surface,(200,100))
	pygame.display.update()
	clock.tick(60)