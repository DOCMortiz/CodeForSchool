from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, SpeedPercent
from time import sleep

# Connect large motors to ports A and B
tiller = LargeMotor(OUTPUT_A)
planter = LargeMotor(OUTPUT_B)

# Define tilling speed and duration
tilling_speed = SpeedPercent(50)
tilling_duration = 5 # seconds

# TILL THE GROUND
tiller.on_for_seconds(tilling_speed, tilling_duration)

# Define planting speed and duration
planting_speed = SpeedPercent(30)
planting_duration = 2 # seconds

# PLANT THE SEEDS
planter.on_for_seconds(planting_speed, planting_duration)

# Pause for 1 second
sleep(1)

# Return motors to their starting positions
tiller.on_for_seconds(-tilling_speed, tilling_duration)
planter.on_for_seconds(-planting_speed, planting_duration)
