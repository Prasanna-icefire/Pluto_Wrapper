from Pluto import pluto
import time

my_pluto = pluto()# This commands creates an object of pluto() where you can connect your hardware to. my_pluto is literally your plutodrone

my_pluto.arm()# Arm your Pluto Drone
time.sleep(5)

my_pluto.disarm()# Disarm your pluto Drone


