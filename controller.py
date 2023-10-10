from time import sleep
import pygame
import busio
import board
from adafruit_servokit import ServoKit

pygame.init()
pygame.joystick.init()

i2c = busio.I2C(3, 2)
kit = ServoKit(channels=16, i2c=i2c)


try:
	if pygame.joystick.get_count() > 0:
		joystick = pygame.joystick.Joystick(0)
		joystick.init()
		while True:
			pygame.event.pump()
			
			x_axis = joystick.get_axis(0)
			y_axis = joystick.get_axis(1)
			y_axis = -y_axis
			
			print("X-axis: {:.2f}, Y-axis: {:.2f}".format(x_axis, y_axis))
			
			kit.servo[0].angle = ((x_axis + 1)/2) * 180
			kit.servo[1].angle = ((x_axis + 1)/2) * 180
			
			kit.servo[15].angle = ((x_axis + 1)/2) * 180
			
			sleep(0.1)
	else:
		print("No joystick found.")
except KeyboardInterrupt:
	pass
finally:
	pygame.quit()
	
