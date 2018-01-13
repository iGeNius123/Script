import os, sys

import subprocess

import Utility as u


def no_split_long_drops(n,f):
    f.write("	<shape type=\"obj\">\n")
    str ="		<string name=\"filename\" value=\"No_Split_Long_Drops/dynamic_drop_"+'{num:03d}'.format(num=n)+".obj\"/>\n"
    f.write(str)
    f.write("			<transform name=\"toWorld\">\n")
    f.write("		    <scale x=\"0.2\" y=\"0.2\" z=\"0.5\"/>\n")
    f.write("		</transform>\n")
    f.write("		<ref id=\"Water_Drop\"/>\n")
    f.write("	</shape>\n")


#C:\\Users\\chu.386\\Desktop\\FinalScene\\


for i in range(1, 271):
    file = open("C:\\Users\\chu.386\\Desktop\\FinalScene\\mitsuba.xml", "w+")
    u.print_head_Info(file)
    u.print_scene_head(file)
    u.integrator(file)
    u.perspective(file)
    u.bsdf_water_drop(file)
    u.envmap(file)
    u.glass(file)
    no_split_long_drops(i,file)
    u.print_scene_tail(file)



    file.close()


    name = '{num:03d}'.format(num=i)
    cmd="cd C:\\Users\\chu.386\\Desktop\\FinalScene && mitsuba -o "+name+" mitsuba.xml"
    os.system(cmd)
    move = "move  C:\\Users\\chu.386\\Desktop\\FinalScene\\"+name+".png  C:\\Users\\chu.386\\Desktop\\FinalScene\\Result"
    os.system(move)

#os.system("start \"\" cmd /k \"cd /D C:\\ ")
#subprocess.check_output("C:\\Users\\chu.386\\Desktop\\Mitsuba0.5.0\\mitsuba.exe C:/Users/chu.386/Desktop/FinalScene/mitsuba.xml", shell=True)
#cmd = ["cd", "C:\\Users\\chu.386\\Desktop\\FinalScene\\"]
#subprocess.call(cmd)
#cmd_out = subprocess.check_output(cmd)

#print(cmd_out)

#cmd = ["mitsuba", "mitsuba.xml"]
#subprocess.call(cmd)

#cmd_out = subprocess.check_output(cmd)

#print(cmd_out)

