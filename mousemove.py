import pyautogui
import random
from time import sleep

while True:
	x = 1000*random.random()
	y = 1000*random.random()
	print(x,y)
	pyautogui.moveTo(x, y)
	sleep(1)
