import os
import Utility as u

u.test()

file = open("mitsuba.xml", "w+")

u.print_head_Info(file)
u.print_scene_head(file)
u.integrator(file)
u.print_scene_tail(file)