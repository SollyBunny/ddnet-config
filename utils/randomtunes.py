#!/bin/env python3

from random import random
from time import sleep

MSGCOUNTDOWN = "%ss untill randomize"
MSGRANDOMIZE = "tunes randomized"
DELTA = 5  # seconds between each random
FIFOPATH = "./fifo.fifo"
TUNES = {
	("ground_control_speed", 4.00, 14.00),  # Maximum running speed on the ground. (Higher values make the character move faster)
	("ground_control_accel", 0.50, 4.00),  # Acceleration on the ground. (Higher values make the character speed up faster)
	("ground_friction", 0.30, 1.00),  # Ground friction. (Higher values make the character stop faster)
	("ground_jump_impulse", 8.00, 18.00),  # Jump force from the ground. (Higher values make the character jump higher)
	("air_jump_impulse", 6.00, 16.00),  # Jump force in the air. (Applies to double jumps; higher values allow higher jumps)
	("air_control_speed", 2.00, 9.00),  # Maximum speed when moving in the air. (Higher values allow faster air movement)
	("air_control_accel", 0.50, 3.00),  # Acceleration in the air. (Higher values allow quicker changes in air movement)
	("air_friction", 0.70, 1.10),  # Air friction. (Higher values reduce the character's air speed more quickly)
	("gravity", 0.30, 0.80),  # Gravity strength. (Lower values make the character float longer; higher values make them fall faster)
}


def write(s):
	with open(FIFOPATH, "w") as fifo:
		fifo.write(s)
	print(s)


sleep(1)
while True:
	out = "broadcast %s\n" % MSGRANDOMIZE
	for name, min, max in TUNES:
		value = min + random() * (max - min)
		value = round(value, 2)
		out += "tune %s %s\n" % (name, value)
	write(out)
	if DELTA > 3:
		sleep(DELTA - 3)
		for i in range(3):
			write("broadcast " + MSGCOUNTDOWN % (3 - i))
			sleep(1)
	else:
		sleep(DELTA)
