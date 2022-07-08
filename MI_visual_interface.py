import pygame
from sys import exit

pygame.init()

screen = pygame.display.set_mode((800,400))
pygame.display.set_caption("BMI/Harmony: MI Visual Interface")

clock = pygame.time.Clock()

#test_surface = pygame.Surface((100,100))
#test_surface.fill('Red')

#Text: subject id 
base_font = pygame.font.Font('Gilroy-Light.otf', 16)
user_text_1 = 'Subject ID'
user_text_2 = 'Session: #'
user_text_3 = 'Trial: #'
user_text_4 = 'Timer: '


while True: 
	for event in pygame.event.get():
		if event.type == pygame.QUIT: 
			pygame.quit()
			exit()

	
	#red box 
	#screen.blit(test_surface,(0,0))

	#text box_1
	text_surface_1 = base_font.render(user_text_1, False, (255,255,255))
	screen.blit(text_surface_1, (100,100))

	#text box_2
	text_surface_2 = base_font.render(user_text_2, False, (255,255,255))
	screen.blit(text_surface_2, (100,120))

	#text box_3
	text_surface_3 = base_font.render(user_text_3, False, (255,255,255))
	screen.blit(text_surface_3, (100,140))

	#text box_4
	text_surface_4 = base_font.render(user_text_4, False, (255,255,255))
	screen.blit(text_surface_4, (650,100))

	#task bar
	pygame.draw.rect(screen,'BLUE',(100,200,600,30),2, 5)


	pygame.display.update()
	clock.tick(60)

