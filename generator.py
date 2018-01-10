import os, sys

import subprocess

import Utility as u

#C:\\Users\\chu.386\\Desktop\\FinalScene\\
file = open("C:\\Users\\chu.386\\Desktop\\FinalScene\\mitsuba.xml", "w+")

u.print_head_Info(file)
u.print_scene_head(file)
u.integrator(file)
u.perspective(file)
u.bsdf_water_drop(file)
u.envmap(file)
u.glass(file)

u.test_obj(file)


u.print_scene_tail(file)


subprocess.check_output("C:\\Users\\chu.386\\Desktop\\Mitsuba0.5.0\\mitsuba.exe C:/Users/chu.386/Desktop/FinalScene/mitsuba.xml", shell=True)
#cmd = ["cd", "C:\\Users\\chu.386\\Desktop\\FinalScene\\"]
#subprocess.call(cmd)
#cmd_out = subprocess.check_output(cmd)

#print(cmd_out)

#cmd = ["mitsuba", "mitsuba.xml"]
#subprocess.call(cmd)

#cmd_out = subprocess.check_output(cmd)

#print(cmd_out)

