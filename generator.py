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

def static_water_drops(file):
    #Static drops static_water_drop(path_to_file,scale,rot_x,rot_y,rot_z,x_trans,y_trans,z_trans,file):
    #w.static_water_drop("NewWaterDrops/Static Drops/Immobile_1.obj",0.3,0,0,180,0,0,0,file)

    #   Right area


    w.static_water_drop("NewWaterDrops/Static Drops/Immobile_2.obj",0.2,0,0,180,8.756,0.5,0,file)
    w.static_water_drop("NewWaterDrops/Static Drops/Immobile_9.obj",0.2,0,0,180,8.896,-1,0,file)

    w.static_water_drop("NewWaterDrops/Static Drops/Immobile_1.obj",0.2,0,0,180,5.356,0.5,0,file)
    #w.static_water_drop("NewWaterDrops/Static Drops/Immobile_2.obj",0.2,0,0,180,5.76,1.2138,0,file)
    w.static_water_drop("NewWaterDrops/Static Drops/Immobile_9.obj",0.2,0,0,180,4.95,-3,0,file)
    w.static_water_drop("NewWaterDrops/Static Drops/Immobile_9.obj",0.2,0,0,180,7.35,-3.12,0,file)
    w.static_water_drop("NewWaterDrops/Static Drops/Immobile_1.obj",0.2,0,0,180,7.35,-4.5,0,file)
    w.static_water_drop("NewWaterDrops/Static Drops/Immobile_2.obj",0.2,0,0,180,5.95,-3,0,file)
    w.static_water_drop("NewWaterDrops/Static Drops/Immobile_1.obj",0.2,0,0,180,5.85,-4.78,0,file)
    #w.static_water_drop("NewWaterDrops/Static Drops/Immobile_6.obj",0.2,0,0,180,7,-5.618,0,file)
    #w.static_water_drop("NewWaterDrops/Static Drops/Immobile_2.obj",0.2,0,0,180,7.2,-6.56,0,file)

   



        #   Left Area
    w.static_water_drop("NewWaterDrops/Static Drops/Immobile_9.obj",0.2,0,0,180,-6.986,-3.618,0,file)
    w.static_water_drop("NewWaterDrops/Static Drops/Immobile_9.obj",0.2,0,0,180,-6.256,0.5,0,file)
    w.static_water_drop("NewWaterDrops/Static Drops/Immobile_2.obj",0.2,0,0,180,-5.0,-4.2138,0,file)
    w.static_water_drop("NewWaterDrops/Static Drops/Immobile_4.obj",0.2,0,0,180,-6.35,-4.5,0,file)
    w.static_water_drop("NewWaterDrops/Static Drops/Immobile_9.obj",0.2,0,0,180,-8.1,-0.123,0,file)
    w.static_water_drop("NewWaterDrops/Static Drops/Immobile_1.obj",0.2,0,0,180,-6.138,-1.123,0,file)
    w.static_water_drop("NewWaterDrops/Static Drops/Immobile_1.obj",0.2,0,0,180,-8.1,-1.235,0,file)
    #w.static_water_drop("NewWaterDrops/Static Drops/Immobile_3.obj",0.2,0,0,180,-6.986,0,0,file)
    w.static_water_drop("NewWaterDrops/Static Drops/Immobile_3.obj",0.2,0,0,180,-7.135,-1,0,file)
    w.static_water_drop("NewWaterDrops/Static Drops/Immobile_3.obj",0.2,0,0,180,-5.986,-7.138,0,file)
    w.static_water_drop("NewWaterDrops/Static Drops/Immobile_3.obj",0.2,0,0,180,-5.135,-6.058,0,file)
    w.static_water_drop("NewWaterDrops/Static Drops/Immobile_9.obj",0.2,0,0,180,-5.035,-2.2138,0,file)

        # Middle Area
        #   Middle Left
    w.static_water_drop("NewWaterDrops/Static Drops/Immobile_9.obj",0.2,0,0,180,-0.03,1.2138,0,file)
    w.static_water_drop("NewWaterDrops/Static Drops/Immobile_9.obj",0.2,0,0,180,-1.33,1.0138,0,file)
    w.static_water_drop("NewWaterDrops/Static Drops/Immobile_9.obj",0.2,0,0,180,-0.65,0.0138,0,file)
    w.static_water_drop("NewWaterDrops/Static Drops/Immobile_3.obj",0.2,0,0,180,0.256,-0.618,0,file)
    w.static_water_drop("NewWaterDrops/Static Drops/Immobile_3.obj",0.2,0,0,180,-1.856,-0.818,0,file)
    w.static_water_drop("NewWaterDrops/Static Drops/Immobile_1.obj",0.2,0,0,180,-1.456,-1.618,0,file)
    w.static_water_drop("NewWaterDrops/Static Drops/Immobile_9.obj",0.2,0,0,180,-1.656,-3.618,0,file)
    w.static_water_drop("NewWaterDrops/Static Drops/Immobile_4.obj",0.2,0,0,180,0.156,-2.618,0,file)
    #w.static_water_drop("NewWaterDrops/Static Drops/Immobile_1.obj",0.3,0,0,180,-1.36,-2.5,0,file)
    #w.static_water_drop("NewWaterDrops/Static Drops/Immobile_4.obj",0.2,0,0,180,-1.102,-4.5,0,file)
    #w.static_water_drop("NewWaterDrops/Static Drops/Immobile_4.obj",0.2,0,0,180,-1.202,-7.5,0,file)
    #w.static_water_drop("NewWaterDrops/Static Drops/Immobile_3.obj",0.2,0,0,180,-0.756,-6.8,0,file)
        #   Middle Right
    #w.static_water_drop("NewWaterDrops/Static Drops/Immobile_2.obj",0.2,0,0,180,1.2,1.2138,0,file)
    #w.static_water_drop("NewWaterDrops/Static Drops/Immobile_5.obj",0.2,0,0,180,1,-1.87,0,file)
    #w.static_water_drop("NewWaterDrops/Static Drops/Immobile_7.obj",0.2,0,0,180,2,-3.6,0,file)
    #w.static_water_drop("NewWaterDrops/Static Drops/Immobile_5.obj",0.2,0,0,180,1.5,-4,0,file)
    #w.static_water_drop("NewWaterDrops/Static Drops/Immobile_6.obj",0.2,0,0,180,1.89,-5.618,0,file)


def single_water_drops_window(total_f):
    # Clear Folder
    #clearFolderContents("window/Result02/")
    for i in range(0,500,50):
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

        # waterDrop_11_15thJan_SmallDS_Split_Smooth
        # 000~319  y: -7.46(bot) 1(top)
            # Appear from Top
        w.waterDrop_11_15thJan_SmallDS_Split_Smooth(180,i,-7.896,1,file,319)
        w.waterDrop_11_15thJan_SmallDS_Split_Smooth(180,i,6.614,1.389,file,319)
            # Disappear at bot
        w.waterDrop_11_15thJan_SmallDS_Split_Smooth(0,i,-2.6,-7.46,file,319)
        w.waterDrop_11_15thJan_SmallDS_Split_Smooth(0,i,5.614,-8.46,file,319)

        # waterDrop_12_14thJan_SmallDS_Smooth
        # 000 ~244 y: -7 (bot) 1.55(top) 
            # Appear from Top
        w.waterDrop_12_14thJan_SmallDS_Smooth(255,i,-4.38,1.55,file,244)
            # Disappear at bot
        w.waterDrop_12_14thJan_SmallDS_Smooth(0,i,-4.5,-7,file,244)
        
        # 000~319  y: -6.6(bot) 1.55(top)
        # waterDrop_12_16thJan_BigDS_Split_Smooth
            # Appear from Top
        w.waterDrop_12_16thJan_BigDS_Split_Smooth(180,i,8.5,1.55,file,319)
            # Disappear at bot
        #w.waterDrop_12_16thJan_BigDS_Split_Smooth(0,i,-0.56,-8.6,file,319)
        w.waterDrop_12_16thJan_BigDS_Split_Smooth(0,i,-8.5,-6.6,file,319)

        # 000 ~499 -2.31(bot) 3.27(top)
        # waterDrop_13_20thJan_BigDS_Split(start_f,current_f,x_trans,y_trans,file,max_frame)
            # Appear from Top
        #w.waterDrop_13_20thJan_BigDS_Split(100,i,-5.023,3.27,file,499)
            # Disappear at bot
        w.waterDrop_13_20thJan_BigDS_Split(0,i,3.25,-2.0,file,499)

        # 000~499  y: -4.3 (bot) 2.8 (top)
        # waterDrop_15_20thJan_BigDS_Split(start_f,current_f,x_trans,y_trans,file,max_frame):
            # Appear from top
        w.waterDrop_15_20thJan_BigDS_Split(250,i,6,2.8,file,499)
        w.waterDrop_15_20thJan_BigDS_Split(0,i,0,2.8,file,499)
        w.waterDrop_15_20thJan_BigDS_Split(200,i,9.0,2.8,file,499)
            # Disappear at bot
        w.waterDrop_15_20thJan_BigDS_Split(0,i,2,-4.3,file,499)

        # 000~499  y: -5.05 (bot) 2.07 (top)
        # waterDrop_16_20thJan_BigDS_Split_Smooth(start_f,current_f,x_trans,y_trans,file,max_frame):
           # Appear from top
 
            # Disappear at bot
        w.waterDrop_16_20thJan_BigDS_Split_Smooth(0,i,0,-5.05,file,499)
        w.waterDrop_16_20thJan_BigDS_Split_Smooth(0,i,6.38,-2.85,file,499)

        # 000~319  y: -8.09 (bot) 0.04 (top)
        # waterDrop_25_15thJan_BigDS_Split_Smooth(start_f,current_f,x_trans,y_trans,file,max_frame):
            # Appear from top
        w.waterDrop_25_15thJan_BigDS_Split_Smooth(180,i,1.5,0.04,file,319)
            # Disappear at bot
        w.waterDrop_25_15thJan_BigDS_Split_Smooth(0,i,9.5,-8.99,file,319)

        # 000~319  y: -8.06 (bot) 0.05 (top)
        # waterDrop_25_15thJan_SmallDS_Smooth(start_f,current_f,x_trans,y_trans,file,max_frame):
            # Appear from top
        w.waterDrop_25_15thJan_SmallDS_Smooth(180,i,3,0.05,file,319)
            # Disappear at bot

        # 000~499  y: -2(bot) 2.2(top)
        # waterDrop_52_16thJan_LargeDS_Split_Smooth(start_f,current_f,x_trans,y_trans,file,max_frame):
            
        w.waterDrop_52_16thJan_LargeDS_Split_Smooth(200,i,3.6,1.50,file,499)
        w.waterDrop_52_16thJan_LargeDS_Split_Smooth(0,i,-9,0.69,file,499)
        w.waterDrop_52_16thJan_LargeDS_Split_Smooth(0,i,7.86,-5.23,file,499)
        w.waterDrop_52_16thJan_LargeDS_Split_Smooth(0,i,-3.8,-1.23,file,499)
        w.waterDrop_52_16thJan_LargeDS_Split_Smooth(50,i,9,3.318,file,499)
            # Disappear at bot

        # 000~352  y: -4.02 (bot) 2.19 (top)
        # waterDrop_52_20thJan_BigDS_Merge_Frame33_Smooth(start_f,current_f,x_trans,y_trans,file,max_frame):
             # Appear from top
        #w.waterDrop_52_20thJan_BigDS_Merge_Frame33_Smooth(60,i,5.1,2.19,file,352)
            # Disappear at bot
        w.waterDrop_52_20thJan_BigDS_Merge_Frame33_Smooth(0,i,0.8,-4.02,file,352)


                #w.waterDrop_25_15thJan_SmallDS_Smooth(0,i,8.5,-8.06,file,319)

                #w.waterDrop_52_16thJan_LargeDS_Split_Smooth(0,i,1.389,1.2,file,499)
                #w.waterDrop_52_16thJan_LargeDS_Split_Smooth(0,i,7.5,-1.396,file,499)

                #w.waterDrop_52_20thJan_BigDS_Merge_Frame33_Smooth(0,i,2.89,-4.52,file,352)


                #w.waterDrop_25_15thJan_SmallDS_Smooth(0,i,3,-8.06,file,319)
                #w.waterDrop_13_20thJan_BigDS_Split(0,i,9.8,-2.05,file,499)
                #w.waterDrop_12_14thJan_SmallDS_Smooth(0,i,-7.5,-7.89,file,244)
        #w.waterDrop_13_20thJan_BigDS_Split(0,i,1.575,1.759,file,499)
                #w.waterDrop_52_16thJan_LargeDS_Split_Smooth(0,i,0.135,-1.23,file,499)
                #w.waterDrop_52_20thJan_BigDS_Merge_Frame33_Smooth(0,i,-9.24,-4.02,file,352)

        # Static drops
        static_water_drops(file)
        
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
            mov = "cd window && move "+name+" Result05/"# window && move " + name + " /Result02/"
            os.system(mov)
        elif platform.system() == "Darwin" :
            name = '{num:03d}'.format(num=i)
            cmd = "cd window && mitsuba -o " + name + " mitsuba.xml"

            os.system(cmd)
            name = name+".png"
            mov = "cd window && mv "+name+" Result05/"# window && move " + name + " /Result02/"
            os.system(mov)


single_water_drops_window(1000)





