import os
import Utility as u

u.test()

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