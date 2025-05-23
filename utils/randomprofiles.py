#!/bin/env python3

import random

with open("usernames.txt", "r") as file:
	data = file.read()
names = data.split("\n")[:-1]

with open("skins.txt", "r") as file:
	data = file.read()
skins = data.split("\n")[:-1]


def name():
	return random.choice(names).replace("\\", "\\\\").replace("\"", "\\\"")


def clan():
	if random.random() < 0.5:
		return " "
	return name()


def skin():
	return random.choice(skins)


def color():
	r = random.randint(0, 255)
	g = random.randint(0, 255)
	b = random.randint(0, 255)
	return (r << 16) | (g << 8) | b


def flag():
	return random.randint(0, 999)


def emote():
	if random.random() < 0.5:
		return 0
	return random.randint(1, 15)


def profile():
	# add_profile i[body] i[feet] i[flag] i[emote] s[skin] s[name] s[clan]
	return f"add_profile {color()} {color()} {flag()} {emote()} \"{skin()}\" \"{name()}\" \"{clan()}\""


count = 100
for i in range(count):
	print(profile())
