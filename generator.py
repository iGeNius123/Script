import os, sys
import subprocess
import window as w
import cv2
import shutil


#C:\\Users\\chu.386\\Desktop\\FinalScene\\

def clearFolderContents(pathToFolder, recursive=False):
    for theFile in os.listdir(pathToFolder):
        filePath = os.path.join(pathToFolder, theFile)
        try:
            if os.path.isfile(filePath):
                os.unlink(filePath)
            elif recursive and os.path.isdir(filePath):
                shutil.rmtree(filePath)
        except Exception as e:
            print(e)

def single_water_drops_window():
    # Clear Folder
    clearFolderContents("C:\\Users\\chu.386\\Desktop\\window\\Result02\\")

    for i in range(1, 271):
        file = open("C:\\Users\\chu.386\\Desktop\\window\\mitsuba.xml", "w+")
        w.print_head_Info(file)
        w.print_scene_head(file)
        w.integrator(file)
        w.perspective(file)
        w.bsdf_water_drop(file)
        w.envmap(file)
        w.glass(file)
        w.no_split_long_drops(i, file)
        w.print_scene_tail(file)

        file.close()

        name = '{num:03d}'.format(num=i)
        cmd = "cd C:\\Users\\chu.386\\Desktop\\window && mitsuba -o " + name + " mitsuba.xml"
        os.system(cmd)



        # load the image and crop it
        name = name+".png"
        image = cv2.imread("C:\\Users\\chu.386\\Desktop\\window\\"+name)
        image = image[0:720, 0:1280]
        cv2.imwrite("C:\\Users\\chu.386\\Desktop\\window\\Result02\\"+name,image)
        delete = "del  C:\\Users\\chu.386\\Desktop\\window\\" + name
        os.system(delete)



single_water_drops_window()




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

