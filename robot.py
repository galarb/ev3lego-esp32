import time
from ev3lego import ev3lego  

encoder1_pin = 14 
encoder2_pin = 12  
in1_pin = 4       
in2_pin = 0       
enA_pin = 2       
wheel_size = 65    # wheel size (in mm)

# Create an instance of ev3lego
robot = ev3lego(encoder1_pin, encoder2_pin, in1_pin, in2_pin, enA_pin, wheel_size)

#example usage: go an exact distance in mm
print('distance covered =', robot.gomm(90, 1000)) #required distance, number of iterations

#example usage: go to an exact angle in degrees
robot.godegrees(150, 1000) #required angle, number of iterations

robot.motgo(0)
