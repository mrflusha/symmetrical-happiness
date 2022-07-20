from time import sleep
import os, subprocess


def pohui():
	#out = cv_shell.stdout.read()
	return  os.system("sensors")
while True:
	os.system("clear")
	print(pohui())
	sleep(3)