import pygame
from sys import exit
import random
import math



#color definitions 
BLACK = (0, 0, 0)
GRAY = (127, 127, 127)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

pygame.init()

screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption("BMI/Harmony: MI Visual Interface")
clock = pygame.time.Clock()


#Text and font 
base_font = pygame.font.Font('Gilroy-Light.otf', 32)
user_text_1 = 'Subject ID'
user_text_2 = 'Session: #'
#trial count
trial_cnt = 1
task_des = "Begin MI"
task_col = GREEN

user_text_3 = 'Press SPACE to start trial.'

#start and stop cursor position
cursor_col = WHITE
cursor_x_pos = 200
stop_pos = random.randint(650,750)   #350-450

#timer variables 
tot_sec = 0 
tot_sec_2 = 0
frame_count = 0
frame_count_2 = 0
start = False

#run once
run_once_00 = 0
run_once_0 = 0
run_once = 0
run_once_1 = 0
run_once_2 = 0
run_once_3 = 0

sx_pos = screen.get_width(); 
sy_pos = screen.get_height();

cur_x = int(sx_pos/2); 
cur_y = int(sy_pos/2); 
angle1 = 4.75; 

#main loop 
while True: 
	keys=pygame.key.get_pressed()

	for event in pygame.event.get():
		if event.type == pygame.QUIT: 
			#######################STOP TRIAL TRIGGER################
			if run_once_3 == 0:
				print(2000)
				run_once_3 = 1
			pygame.quit()
			exit()
	if keys[pygame.K_ESCAPE] or trial_cnt == 21:
		if run_once_3 == 0:
				print(2000)
				run_once_3 = 1
		pygame.quit()
		exit()


	if run_once_00 == 0:
		print(1000)
		run_once_00 = 1
	#fill the screen with black after movement
	screen.fill(BLACK)

	#task box
	text_surface_5= base_font.render(task_des, False, task_col)
	screen.blit(text_surface_5, (cur_x,cur_y))

	#User prompt
	text_surface_6= base_font.render(user_text_3, False, WHITE)
	screen.blit(text_surface_6, (cur_x-175,cur_y-400))

	#text box_3
	text_surface_3 = base_font.render('Trial: ' + str(trial_cnt), False, (255,255,255))
	screen.blit(text_surface_3, (sx_pos*(1/4),200))

	#text box_4
	text_surface_4 = base_font.render('Timer: ' + str(tot_sec), False, (255,255,255))
	screen.blit(text_surface_4, (sx_pos*(3/4),200))

	#task tube
	pygame.draw.circle(screen, BLUE, (int(sx_pos/2),int(sy_pos/2)+100), 350, 3)
	pygame.draw.circle(screen, BLUE, (int(sx_pos/2),int(sy_pos/2)+100), 300, 3)

	#start MI bar
	pygame.draw.rect(screen,GREEN,(cur_x,cur_y-250,20,50),0)

	#subject cursor 
	pygame.draw.circle(screen, cursor_col, (int(cursor_x_pos),425), 25)

	#subject cursor _2
	pygame.draw.circle(screen, cursor_col, (325*math.cos(angle1)+(cur_x), 325*math.sin(angle1)+(cur_y+100)), 25)

	#stop MI bar
	#pygame.draw.rect(screen,RED,(cur_x,cur_y+400,20,50),0)
	pygame.draw.rect(screen,RED,(325*math.cos(10)+(cur_x), 325*math.sin(10)+(cur_y+75),20,50),0)


	#stop rest bar
	pygame.draw.rect(screen,YELLOW,(cur_x-20,cur_y-250,20,50),0)

	
	#count down timer 
	
	if(tot_sec_2 < 5):
		task_des = str(5-tot_sec_2)
		task_col = WHITE
	#at 0 sec, task des is GO
	if(tot_sec_2 == 5):
		task_des = 'GO!'
		task_col = GREEN
		#######################START Trigger 2################
		if run_once == 0:
			print(100)
			run_once = 1
	#after countdown, begin MI, increase x_pos
	if(tot_sec_2 > 5):
		frame_count += 1
		#move cursor 
		cursor_col = GREEN
		#current task instruction 
		if(cursor_x_pos >= stop_pos):
			task_des = "End MI...Rest"
			task_col = RED
			cursor_col = RED
			#######################START Trigger 3################
			if run_once_2 == 0:
				print(500)
				run_once_2 = 1
		if(cursor_x_pos < stop_pos):
			task_des = "Begin MI"
			task_col = GREEN
		if(cursor_x_pos <= 1200):     #updating cursor position
			cursor_x_pos +=1.6 
			angle1 +=0.01;         #Speed of the cursor 
		if(cursor_x_pos == 1200):		#stoping cursor at end line 
			cursor_x_pos = 1200
			#######################START Trigger 4################
		if(tot_sec == 10):
			if run_once_1 == 0:
				print(900)
				run_once_1 = 1
		if(tot_sec > 10):
			task_des = "Relax"
			task_col = YELLOW
			cursor_col = YELLOW	
		if(tot_sec == 15): 			#after 10 sec, reset all variables	 
			cursor_x_pos = 200
			angle1 = 4.75; 
			trial_cnt +=1
			frame_count = 0
			frame_count_2 = 0
			start = True
			user_text_3 = 'Press SPACE to start trial. '
			stop_pos = random.randint(650,750) 
			cursor_col = WHITE
			run_once_0 = 0
			run_once = 0
			run_once_1 = 0
			run_once_2 = 0
			run_once_3 = 0


	#once space is pressed, start the trial, countdown 
	
	if keys[pygame.K_SPACE]:
		#######################START Trigger 1################
		if run_once_0 == 0:
			print(300)
			run_once_0 = 1
		start = True 
		user_text_3 = 'Press (r) to restart trial.'

	if keys[pygame.K_r]:
		cursor_x_pos = 200
		angle1 = 4.75; 
		frame_count = 0
		frame_count_2 = 0
		start = False
		cursor_col = WHITE
		user_text_3 = 'Press SPACE to start trial. '
	


	#once space is pressed, start countdown 
	if(start):
		frame_count_2 +=1


	#timer for the game
	tot_sec = round(((frame_count/60)%60),2)
	tot_sec_2 = round((frame_count_2/60)%60)
	
	
	pygame.display.update()  #screen is updated 
	clock.tick(60)  #60fps 

