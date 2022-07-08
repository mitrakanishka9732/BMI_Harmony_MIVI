import pygame
from sys import exit

pygame.init()

screen = pygame.display.set_mode((800,400))
pygame.display.set_caption("BMI/Harmony: MI Visual Interface")

clock = pygame.time.Clock()


#Text: subject id 
base_font = pygame.font.Font('Gilroy-Light.otf', 16)
user_text_1 = 'Subject ID'
user_text_2 = 'Session: #'
#trial count
trial_cnt = 0
task_des = "Begin MI"
task_col = 'GREEN'

#cursor x position
cursor_x_pos = 115

#timer variables 
tot_sec = 0 
tot_sec_2 = 0
frame_count = 0
frame_count_2 = 0

while True: 
	for event in pygame.event.get():
		if event.type == pygame.QUIT: 
			pygame.quit()
			exit()

	screen.fill((0,0,0))


	#task box
	text_surface_5= base_font.render(task_des, False, task_col)
	screen.blit(text_surface_5, (370,100))

	#text box_1
	text_surface_1 = base_font.render(user_text_1, False, (255,255,255))
	screen.blit(text_surface_1, (100,100))

	#text box_2
	text_surface_2 = base_font.render(user_text_2, False, (255,255,255))
	screen.blit(text_surface_2, (100,120))

	#text box_3
	text_surface_3 = base_font.render('Trial: ' + str(trial_cnt), False, (255,255,255))
	screen.blit(text_surface_3, (100,140))

	#text box_4
	text_surface_4 = base_font.render('Timer: ' + str(tot_sec), False, (255,255,255))
	screen.blit(text_surface_4, (650,100))

	#task bar
	pygame.draw.rect(screen,'BLUE',(100,200,600,30),2, 5)

	#start MI bar
	pygame.draw.rect(screen,'GREEN',(100,200,10,30),0,2)

	#subject cursor 

	pygame.draw.circle(screen, 'WHITE', (cursor_x_pos,215), 15)

	#stop MI bar
	pygame.draw.rect(screen,'RED',(400,200,10,30),0,2)

	#stop rest bar
	pygame.draw.rect(screen,'YELLOW',(690,200,10,30),0,2)

	#main engine
	
	#count down timer 
	if(tot_sec_2 < 3):
		task_des = str(3-tot_sec_2)
		task_col = 'WHITE'
	#at 0 sec, task des is GO
	if(tot_sec_2 == 3):
		task_des = 'GO!'
		task_col = 'GREEN'
	#after countdown, begin MI, increase x_pos
	if(tot_sec_2 > 3):
		frame_count += 1
		#move cursor 
		#current task instruction 
		if(cursor_x_pos >= 400):
			task_des = "End MI...Rest"
			task_col = 'RED'
		if(cursor_x_pos < 400):
			task_des = "Begin MI"
			task_col = 'GREEN'
		if(cursor_x_pos <= 700):
			cursor_x_pos +=1
		if(cursor_x_pos == 700):
			cursor_x_pos = 700
		if(tot_sec == 11): 
		 	cursor_x_pos = 115
		 	trial_cnt +=1
		 	frame_count = 0
		 	frame_count_2 = 0


	#timer for the game
	tot_sec = round((frame_count/60)%60)
	tot_sec_2 = round((frame_count_2/60)%60)
	frame_count_2 += 1
	

	pygame.display.update()
	clock.tick(60)

