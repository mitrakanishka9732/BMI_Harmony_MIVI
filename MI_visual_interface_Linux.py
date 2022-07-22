import pygame
from sys import exit
import random
import cnbiloop
from cnbiloop import BCI, BCI_tid


bci = BCI_tid.BciInterface()

def sendTiD(Event_):
        bci.id_msg_bus.SetEvent(Event_)
        bci.iDsock_bus.sendall(str.encode(bci.id_serializer_bus.Serialize()))

def receiveTiD():
    data = None
    try:
        data = bci.iDsock_bus.recv(512).decode("utf-8")
        bci.idStreamer_bus.Append(data)
    except:
        nS = False
        dec = 0
        pass
    # deserialize ID message
    if (data):
        if (bci.idStreamer_bus.Has("<tobiid", "/>")):
            msg = bci.idStreamer_bus.Extract("<tobiid", "/>")
            bci.id_serializer_bus.Deserialize(msg)
            bci.idStreamer_bus.Clear()
            tmpmsg = int(round(float(bci.id_msg_bus.GetEvent())))
            # print("Received Message: ", tmpmsg)
            return tmpmsg
               
        elif bci.idStreamer_bus.Has("<tcstatus","/>"):
            MsgNum = bci.idStreamer_bus.Count("<tcstatus")
            for i in range(1,MsgNum-1):
                # Extract most of these messages and trash them     
                msg_useless = bci.idStreamer_bus.Extract("<tcstatus","/>")

pygame.init()

screen = pygame.display.set_mode((1400,800))
pygame.display.set_caption("BMI/Harmony: MI Visual Interface")
clock = pygame.time.Clock()

#color definitions 
BLACK = (0, 0, 0)
GRAY = (127, 127, 127)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

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
stop_pos = random.randint(600,800)   #350-450

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

#main loop 
while True: 
	for event in pygame.event.get():
		if event.type == pygame.QUIT: 
			#######################STOP TRIAL TRIGGER################
			if run_once_3 == 0:
				print(2000)
				sendTiD(2000)
				run_once_3 = 1
			pygame.quit()
			exit()

	if run_once_00 == 0:
		print(1000)
		sendTiD(1000)
		run_once_00 = 1
	#fill the screen with black after movement
	screen.fill(BLACK)

	#task box
	text_surface_5= base_font.render(task_des, False, task_col)
	screen.blit(text_surface_5, (650,250))

	#User prompt
	text_surface_6= base_font.render(user_text_3, False, WHITE)
	screen.blit(text_surface_6, (550,500))

	#text box_1
	text_surface_1 = base_font.render(user_text_1, False, (255,255,255))
	screen.blit(text_surface_1, (200,200))

	#text box_2
	text_surface_2 = base_font.render(user_text_2, False, (255,255,255))
	screen.blit(text_surface_2, (200,250))

	#text box_3
	text_surface_3 = base_font.render('Trial: ' + str(trial_cnt), False, (255,255,255))
	screen.blit(text_surface_3, (200,300))

	#text box_4
	text_surface_4 = base_font.render('Timer: ' + str(tot_sec), False, (255,255,255))
	screen.blit(text_surface_4, (1060,200))

	#task bar
	pygame.draw.rect(screen,BLUE,(200,400,1000,50),2)

	#subject cursor 
	pygame.draw.circle(screen, cursor_col, (cursor_x_pos,425), 25)

	#start MI bar
	pygame.draw.rect(screen,GREEN,(200,400,20,50),0)

	#stop MI bar
	pygame.draw.rect(screen,RED,(stop_pos,400,20,50),0)

	#stop rest bar
	pygame.draw.rect(screen,YELLOW,(1190,400,20,50),0)

	
	#count down timer 
	
	if(tot_sec_2 < 3):
		task_des = str(3-tot_sec_2)
		task_col = WHITE
	#at 0 sec, task des is GO
	if(tot_sec_2 == 3):
		task_des = 'GO!'
		task_col = GREEN
		#######################START Trigger 2################
		if run_once == 0:
			print(100)
			sendTiD(100)
			run_once = 1
	#after countdown, begin MI, increase x_pos
	if(tot_sec_2 > 3):
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
				sendTiD(500)
				run_once_2 = 1
		if(cursor_x_pos < stop_pos):
			task_des = "Begin MI"
			task_col = GREEN
		if(cursor_x_pos <= 1200):     #updating cursor position
			cursor_x_pos +=1.6         #Speed of the cursor 
		if(cursor_x_pos == 1200):		#stoping cursor at end line 
			cursor_x_pos = 1200
			#######################START Trigger 4################
		if(tot_sec == 10):
			if run_once_1 == 0:
				print(900)
				sendTiD(900)
				run_once_1 = 1
		if(tot_sec == 11): 			#after 10 sec, reset all variables	 
			cursor_x_pos = 200
			trial_cnt +=1
			frame_count = 0
			frame_count_2 = 0
			start = False
			user_text_3 = 'Press SPACE to start trial. '
			stop_pos = random.randint(600,800) 
			cursor_col = WHITE
			run_once_0 = 0
			run_once = 0
			run_once_1 = 0
			run_once_2 = 0
			run_once_3 = 0


	#once space is pressed, start the trial, countdown 
	keys=pygame.key.get_pressed()
	if keys[pygame.K_SPACE]:
		#######################START Trigger 1################
		if run_once_0 == 0:
			print(300)
			sendTiD(300)
			run_once_0 = 1
		start = True 
		user_text_3 = 'Press (r) to restart trial.'

	if keys[pygame.K_r]:
		cursor_x_pos = 200
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
