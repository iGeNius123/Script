import os, sys
import platform
import subprocess
import window as w
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

def single_water_drops_window(total_f):
    # Clear Folder
    #clearFolderContents("window/Result02/")
    for i in range(0, 751):
    #for i in [0,50,100,150,200,250,300,350,400,450,500,550,600,650,700,749]:
        file = open("window/mitsuba.xml", "w+")
        w.print_head_Info(file)
        w.print_scene_head(file)
        w.integrator(file)
        w.perspective(file)
        w.bsdf_water_drop(file)
        w.envmap(file)
        w.glass(file)
        #w.no_split_long_drops(i, file)
        #w.test_drops_53(i,file)

        # Water drops loading function: (start_f,current_f,x_trans,y_trans,file,max_frame)
        w.waterDrop_11_15thJan_SmallDS_Split(430,i,-6.0,1.0,file,319)
        w.waterDrop_52_16thJan_LargeDS_Split(0,i,-3.0,-2.0,file,499)
        w.waterDrop_12_16thJan_BigDS_Split(430,i,3.0,1.55,file,319)
        w.waterDrop_52_16thJan_SmallDS(0,i,3.0,0.6,file,499)
        w.waterDrop_25_15thJan_BigDS_Split(0,i,6,-8,file,319)
        # Merging water drop seq
        w.waterDrop_merging(0,i,0,-2.07,file,319)


        #Static drops static_water_drop(path_to_file,scale,rot_x,rot_y,rot_z,x_trans,y_trans,z_trans,file):
        #w.static_water_drop("NewWaterDrops/Static Drops/Immobile_1.obj",0.3,0,0,180,0,0,0,file)

        #   Right area
        w.static_water_drop("NewWaterDrops/Static Drops/Immobile_1.obj",0.3,0,0,180,7.5,-2.5,0,file)
        w.static_water_drop("NewWaterDrops/Static Drops/Immobile_2.obj",0.2,0,0,180,7.2,1.2138,0,file)
        w.static_water_drop("NewWaterDrops/Static Drops/Immobile_3.obj",0.2,0,0,180,7.956,-0.618,0,file)
        w.static_water_drop("NewWaterDrops/Static Drops/Immobile_7.obj",0.2,0,0,180,8.1,-2.6,0,file)
        w.static_water_drop("NewWaterDrops/Static Drops/Immobile_4.obj",0.2,0,0,180,9.256,0.5,0,file)
        w.static_water_drop("NewWaterDrops/Static Drops/Immobile_5.obj",0.2,0,0,180,9.396,-1,0,file)
        w.static_water_drop("NewWaterDrops/Static Drops/Immobile_6.obj",0.2,0,0,180,7,-3.618,0,file)
        w.static_water_drop("NewWaterDrops/Static Drops/Immobile_4.obj",0.2,0,0,180,6.256,0.5,0,file)
        w.static_water_drop("NewWaterDrops/Static Drops/Immobile_2.obj",0.2,0,0,180,5.5,1.2138,0,file)
        w.static_water_drop("NewWaterDrops/Static Drops/Immobile_3.obj",0.2,0,0,180,5.45,-3,0,file)
        w.static_water_drop("NewWaterDrops/Static Drops/Immobile_4.obj",0.2,0,0,180,6.35,-4.5,0,file)

        w.static_water_drop("NewWaterDrops/Static Drops/Immobile_3.obj",0.2,0,0,180,7.956,-5.618,0,file)
        w.static_water_drop("NewWaterDrops/Static Drops/Immobile_7.obj",0.2,0,0,180,8.1,-7.6,0,file)
        w.static_water_drop("NewWaterDrops/Static Drops/Immobile_4.obj",0.2,0,0,180,9.256,-4.5,0,file)
        w.static_water_drop("NewWaterDrops/Static Drops/Immobile_5.obj",0.2,0,0,180,9.396,-6,0,file)

        w.static_water_drop("NewWaterDrops/Static Drops/Immobile_6.obj",0.2,0,0,180,7,-5.618,0,file)
        w.static_water_drop("NewWaterDrops/Static Drops/Immobile_2.obj",0.2,0,0,180,7.2,-6.56,0,file)

   



        #   Left Area
        w.static_water_drop("NewWaterDrops/Static Drops/Immobile_6.obj",0.2,0,0,180,-7,-3.618,0,file)
        w.static_water_drop("NewWaterDrops/Static Drops/Immobile_4.obj",0.2,0,0,180,-6.256,0.5,0,file)
        w.static_water_drop("NewWaterDrops/Static Drops/Immobile_2.obj",0.2,0,0,180,-5.5,-4.2138,0,file)
        w.static_water_drop("NewWaterDrops/Static Drops/Immobile_3.obj",0.2,0,0,180,-5.45,-6,0,file)
        w.static_water_drop("NewWaterDrops/Static Drops/Immobile_4.obj",0.2,0,0,180,-6.35,-4.5,0,file)
        w.static_water_drop("NewWaterDrops/Static Drops/Immobile_6.obj",0.2,0,0,180,-7,-5.618,0,file)



        # Middle Area
        #   Middle Left
        w.static_water_drop("NewWaterDrops/Static Drops/Immobile_2.obj",0.2,0,0,180,-1.03,1.2138,0,file)
        w.static_water_drop("NewWaterDrops/Static Drops/Immobile_3.obj",0.2,0,0,180,-0.856,-0.618,0,file)
        w.static_water_drop("NewWaterDrops/Static Drops/Immobile_1.obj",0.3,0,0,180,-1.36,-2.5,0,file)
        w.static_water_drop("NewWaterDrops/Static Drops/Immobile_4.obj",0.2,0,0,180,-1.102,-4.5,0,file)
        w.static_water_drop("NewWaterDrops/Static Drops/Immobile_4.obj",0.2,0,0,180,-1.202,-7.5,0,file)
        w.static_water_drop("NewWaterDrops/Static Drops/Immobile_3.obj",0.2,0,0,180,-0.756,-6.8,0,file)
        #   Middle Right
        w.static_water_drop("NewWaterDrops/Static Drops/Immobile_2.obj",0.2,0,0,180,1.2,1.2138,0,file)
        w.static_water_drop("NewWaterDrops/Static Drops/Immobile_5.obj",0.2,0,0,180,1,-1.87,0,file)
        w.static_water_drop("NewWaterDrops/Static Drops/Immobile_7.obj",0.2,0,0,180,2,-3.6,0,file)
        w.static_water_drop("NewWaterDrops/Static Drops/Immobile_5.obj",0.2,0,0,180,1.5,-4,0,file)
        w.static_water_drop("NewWaterDrops/Static Drops/Immobile_6.obj",0.2,0,0,180,1.89,-5.618,0,file)


        w.print_scene_tail(file)

        file.close()
        if platform.system() == "Windows" :
            name = '{num:03d}'.format(num=i)
            cmd = "cd window && mitsuba -o " + name + " mitsuba.xml"
            os.system(cmd)



            # load the image and crop it
            name = name+".png"
            #image = cv2.imread("C:\\Users\\chu.386\\Desktop\\window\\"+name)
            #image = image[0:720, 0:1280]
            #cv2.imwrite("C:\\Users\\chu.386\\Desktop\\window\\Result02\\"+name,image)
            mov = "cd window && move "+name+" Result02/"# window && move " + name + " /Result02/"
            os.system(mov)
        elif platform.system() == "Darwin" :
            name = '{num:03d}'.format(num=i)
            cmd = "cd window && mitsuba -o " + name + " mitsuba.xml"

            os.system(cmd)
            name = name+".png"
            mov = "cd window && mv "+name+" Result02/"# window && move " + name + " /Result02/"
            os.system(mov)


single_water_drops_window(1000)





