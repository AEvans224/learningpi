from gpiozero import AngularServo
from time import sleep

#SG90 settings
servo = AngularServo(
    18,
    min_angle = 0,
    max_angle=180,
    min_pulse_width=0.0006,
    max_pulse_width=0.0023
)

idx = 1

while True:
    if idx == 0: #basic movement
        print("Move to 0 Degrees")
        servo.angle = 0
        sleep(1)

        print("Move to 90 Degrees")
        servo.angle = 90
        sleep(1)

        print("Move to 180 Degrees")
        servo.angle = 180
        sleep(1)
    elif idx ==1: #sweep movement
        print("Sweep from 0 to 180 Degrees")
        for angle in range(0, 181, 10):
            servo.angle = angle
            sleep(0.5)
        print("Sweep from 180 to 0 Degrees")
        for angle in range(180, -1, -10):
            servo.angle = angle
            sleep(0.5)

