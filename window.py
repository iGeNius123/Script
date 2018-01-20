


def test():
    print("Test Function")

def print_head_Info(file):
    file.write("<?xml version=\"1.0\" encoding=\"utf-8\"?>\n")

def print_scene_head(file):
    file.write("<scene version=\"0.5.0\">\n")

def print_scene_tail(file):
    file.write("</scene>\n")

def integrator(file):
    file.write("	<integrator type=\"bdpt\">\n")
    file.write("		<integer name=\"maxDepth\" value=\"6\"/>\n")
    file.write("		<boolean name=\"strictNormals\" value=\"true\"/>\n")
    file.write("	</integrator>\n")

def perspective(file):
    file.write("	<sensor type=\"perspective\">\n")
    file.write("		<float name=\"farClip\" value=\"1000\"/>\n")
    file.write("		<float name=\"focusDistance\" value=\"10\"/>\n")
    file.write("		<float name=\"fov\" value=\"20\"/>\n")
    file.write("		<string name=\"fovAxis\" value=\"x\"/>\n")
    file.write("		<float name=\"nearClip\" value=\"0.1\"/>\n")
    file.write("		<transform name=\"toWorld\">\n")
    file.write("			<lookat target=\"0, 0, 0\" origin=\"0, 0, 50\" up=\"0, 1, 0\"/>\n")
    file.write("		</transform>\n")
    file.write("		<sampler type=\"ldsampler\">\n")
    file.write("			<integer name=\"sampleCount\" value=\"512\"/>\n")
    file.write("		</sampler>\n")
    file.write("		<film type=\"ldrfilm\">\n")
    file.write("			<integer name=\"height\" value=\"720\"/>\n")
    file.write("			<integer name=\"width\" value=\"1280\"/>\n")
    file.write("			<rfilter type=\"gaussian\"/>\n")
    file.write("			<boolean name=\"banner\" value=\"false\"/>\n")
    file.write("		</film>\n")
    file.write("	</sensor>\n")

def bsdf_water_drop(file):
    file.write("	<bsdf type=\"dielectric\" id=\"Water_Drop\">\n")
    file.write("		<float name=\"extIOR\" value=\"1.0\"/>\n")
    file.write("		<float name=\"intIOR\" value=\"1.333\"/>\n")
    file.write("	</bsdf>\n")

def envmap(file):
    file.write("	<emitter type=\"envmap\">\n")
    file.write("	    <float name = \"scale\" value = \"5\"/>\n")
    file.write("		<string name=\"filename\" value=\"env_blur.hdr\"/>\n")
    file.write("		<transform name=\"toWorld\">\n")
    file.write("			<rotate y = \"1\" angle = \"-150\"/>\n")
    file.write("			<rotate x = \"1\" angle = \"-2\"/>\n")
    file.write("		</transform>\n")
    file.write("	</emitter>\n")

def glass(file):
    file.write("	<shape type=\"cube\" id = \"glass\">\n")
    file.write("		<transform name=\"toWorld\">\n")
    file.write("			<scale x=\"10\" y=\"10\" z=\"0.1\"/>\n")
    file.write("		</transform>\n")

    file.write("		<bsdf type=\"mixturebsdf\">\n")
    file.write("			<string name = \"weights\" value = \"1,0\"/>\n")
    file.write("			<bsdf type = \"dielectric\"/>\n")
    file.write("			<bsdf type = \"roughdielectric\">\n")
    file.write("			    <float name = \"alpha\" value = \"0.1\"/>\n")
    file.write("		    </bsdf>\n")
    file.write("		</bsdf>\n")
#    file.write("		<medium type=\"homogeneous\" name=\"interior\">\n")
 #   file.write("			<rgb name=\"sigmaS\" value=\"0, 0, 0\"/>\n")
  #  file.write("			<rgb name=\"sigmaA\" value=\"4, 4, 2\"/>\n")
   # file.write("		</medium>\n")
    file.write("	</shape>\n")

def no_split_long_drops(n,f):
    f.write("	<shape type=\"obj\">\n")
    str ="		<string name=\"filename\" value=\"No_Split_Long_Drops/dynamic_drop_"+'{num:03d}'.format(num=n)+".obj\"/>\n"
    f.write(str)
    f.write("		<transform name=\"toWorld\">\n")
    f.write("		    <scale value=\"0.3\"/>\n")
    f.write("		    <rotate z=\"1\" angle=\"180\"/>\n")
    f.write("		</transform>\n")
    f.write("		<ref id=\"Water_Drop\"/>\n")
    f.write("	</shape>\n")

def test_drops_53(n,f):
    f.write("	<shape type=\"obj\">\n")
    str ="		<string name=\"filename\" value=\"52_13thJan_SmallDS/static_drop_"+'{num:03d}'.format(num=n)+".obj\"/>\n"
    f.write(str)
    f.write("		<transform name=\"toWorld\">\n")
    f.write("		    <scale value=\"0.3\"/>\n")
    f.write("		    <rotate z=\"1\" angle=\"180\"/>\n")
    f.write("		</transform>\n")
    f.write("		<ref id=\"Water_Drop\"/>\n")
    f.write("	</shape>\n")

# 000~309  y: -7.3(bot) 1(top)
def waterDrop_11_15thJan_SmallDS_Split(start_f,current_f,x_trans,y_trans,file,max_frame):
    if ((current_f - start_f) <= max_frame) and ((current_f - start_f) >= 0):
        file.write("	<shape type=\"obj\">\n")
        str ="		<string name=\"filename\" value=\"NewWaterDrops/11_15thJan_SmallDS_Split/dynamic_drop_"+'{num:03d}'.format(num=current_f - start_f)+".obj\"/>\n"
        file.write(str)
        file.write("		<transform name=\"toWorld\">\n")
        file.write("		    <scale value=\"0.3\"/>\n")
        file.write("		    <rotate z=\"1\" angle=\"180\"/>\n")

        file.write("		    <translate y = \""+'{num:f}'.format(num=y_trans)+"\"/>\n")
        file.write("		    <translate x = \""+'{num:f}'.format(num=x_trans)+"\"/>\n")
        file.write("		</transform>\n")
        file.write("		<ref id=\"Water_Drop\"/>\n")
        file.write("	</shape>\n")

    # 000~319  y: -6.6(bot) 1.55(top)
def waterDrop_12_16thJan_BigDS_Split(start_f,current_f,x_trans,y_trans,file,max_frame):
    if ((current_f - start_f) <= max_frame) and ((current_f - start_f) >= 0):
        file.write("	<shape type=\"obj\">\n")
        str = "		<string name=\"filename\" value=\"NewWaterDrops/12_16thJan_BigDS_Split/dynamic_drop_" + '{num:03d}'.format(num=current_f - start_f) + ".obj\"/>\n"
        file.write(str)
        file.write("		<transform name=\"toWorld\">\n")
        file.write("		    <scale value=\"0.3\"/>\n")
        file.write("		    <rotate z=\"1\" angle=\"180\"/>\n")

        file.write("		    <translate y = \"" + '{num:f}'.format(num=y_trans) + "\"/>\n")
        file.write("		    <translate x = \"" + '{num:f}'.format(num=x_trans) + "\"/>\n")
        file.write("		</transform>\n")
        file.write("		<ref id=\"Water_Drop\"/>\n")
        file.write("	</shape>\n")


    # 000~319  y: -8(bot) 0.08(top)
def waterDrop_25_15thJan_BigDS_Split(start_f,current_f,x_trans,y_trans,file,max_frame):
    if ((current_f - start_f) <= max_frame) and ((current_f - start_f) >= 0):
        file.write("	<shape type=\"obj\">\n")
        str = "		<string name=\"filename\" value=\"NewWaterDrops/25_15thJan_BigDS_Split/dynamic_drop_" + '{num:03d}'.format(num=current_f - start_f) + ".obj\"/>\n"
        file.write(str)
        file.write("		<transform name=\"toWorld\">\n")
        file.write("		    <scale value=\"0.3\"/>\n")
        file.write("		    <rotate z=\"1\" angle=\"180\"/>\n")

        file.write("		    <translate y = \""+'{num:f}'.format(num=y_trans)+"\"/>\n")
        file.write("		    <translate x = \""+'{num:f}'.format(num=x_trans)+"\"/>\n")
        file.write("		</transform>\n")
        file.write("		<ref id=\"Water_Drop\"/>\n")
        file.write("	</shape>\n")


    # 000~499  y: -2(bot) 2.2(top)
def waterDrop_52_16thJan_LargeDS_Split(start_f,current_f,x_trans,y_trans,file,max_frame):
    if ((current_f - start_f) <= max_frame) and ((current_f - start_f) >= 0):
        file.write("	<shape type=\"obj\">\n")
        str = "		<string name=\"filename\" value=\"NewWaterDrops/52_16thJan_LargeDS_Split/dynamic_drop_" + '{num:03d}'.format(num=current_f - start_f) + ".obj\"/>\n"
        file.write(str)
        file.write("		<transform name=\"toWorld\">\n")
        file.write("		    <scale value=\"0.3\"/>\n")
        file.write("		    <rotate z=\"1\" angle=\"180\"/>\n")

        file.write("		    <translate y = \""+'{num:f}'.format(num=y_trans)+"\"/>\n")
        file.write("		    <translate x = \""+'{num:f}'.format(num=x_trans)+"\"/>\n")
        file.write("		</transform>\n")
        file.write("		<ref id=\"Water_Drop\"/>\n")
        file.write("	</shape>\n")


    # 000~499  y: 0.6(bot) 2.2(top)
def waterDrop_52_16thJan_SmallDS(start_f,current_f,x_trans,y_trans,file,max_frame):
    if ((current_f - start_f) <= max_frame) and ((current_f - start_f) >= 0):
        file.write("	<shape type=\"obj\">\n")
        str = "		<string name=\"filename\" value=\"NewWaterDrops/52_16thJan_SmallDS/dynamic_drop_" + '{num:03d}'.format(num=current_f - start_f) + ".obj\"/>\n"
        file.write(str)
        file.write("		<transform name=\"toWorld\">\n")
        file.write("		    <scale value=\"0.3\"/>\n")
        file.write("		    <rotate z=\"1\" angle=\"180\"/>\n")

        file.write("		    <translate y = \""+'{num:f}'.format(num=y_trans)+"\"/>\n")
        file.write("		    <translate x = \""+'{num:f}'.format(num=x_trans)+"\"/>\n")
        file.write("		</transform>\n")
        file.write("		<ref id=\"Water_Drop\"/>\n")
        file.write("	</shape>\n")

# 000~319  y: -2.07 (bot)
def waterDrop_merging(start_f,current_f,x_trans,y_trans,file,max_frame):
    if ((current_f - start_f) <= max_frame) and ((current_f - start_f) >= 0):
        file.write("	<shape type=\"obj\">\n")
        str = "		<string name=\"filename\" value=\"NewWaterDrops/52_19thJan_SmallDS_Merge_Frame33_Smooth/dynamic_drop_" + '{num:03d}'.format(num=current_f - start_f) + ".obj\"/>\n"
        file.write(str)
        file.write("		<transform name=\"toWorld\">\n")
        file.write("		    <scale value=\"0.3\"/>\n")
        file.write("		    <rotate z=\"1\" angle=\"180\"/>\n")

        file.write("		    <translate y = \""+'{num:f}'.format(num=y_trans)+"\"/>\n")
        file.write("		    <translate x = \""+'{num:f}'.format(num=x_trans)+"\"/>\n")
        file.write("		</transform>\n")
        file.write("		<ref id=\"Water_Drop\"/>\n")
        file.write("	</shape>\n")

def static_water_drop(path_to_file,scale,rot_x,rot_y,rot_z,x_trans,y_trans,z_trans,file):
    file.write("	<shape type=\"obj\">\n")
    str = "		<string name=\"filename\" value=\""+path_to_file+"\"/>\n"
    file.write(str)
    file.write("		<transform name=\"toWorld\">\n")
    file.write("		    <scale value=\""+'{num:f}'.format(num=scale)+"\"/>\n")
    file.write("		    <rotate x=\"1\" angle=\""+'{num:f}'.format(num=rot_x)+"\"/>\n")
    file.write("		    <rotate y=\"1\" angle=\""+'{num:f}'.format(num=rot_y)+"\"/>\n")
    file.write("		    <rotate z=\"1\" angle=\""+'{num:f}'.format(num=rot_z)+"\"/>\n")
    file.write("		    <translate y = \""+'{num:f}'.format(num=y_trans)+"\"/>\n")
    file.write("		    <translate x = \""+'{num:f}'.format(num=x_trans)+"\"/>\n")
    file.write("		    <translate z = \""+'{num:f}'.format(num=z_trans)+"\"/>\n")
    file.write("		</transform>\n")
    file.write("		<ref id=\"Water_Drop\"/>\n")
    file.write("	</shape>\n")


def test_obj(file):
    file.write("	<shape type=\"sphere\">\n")
    file.write("		<ref id=\"Water_Drop\"/>\n")
    file.write("		<transform name=\"toWorld\">\n")
    file.write("			<scale x=\"1\" y=\"1\" z=\"1\"/>\n")
    file.write("		</transform>\n")
    file.write("	</shape>\n")
    file.write("	<shape type=\"obj\">\n")
    file.write("		<string name=\"filename\" value=\"static_drop_004.obj\"/>\n")
    file.write("		<transform name=\"toWorld\">\n")
    file.write("			<translate x=\"10\" y=\"30\" z=\"0\"/>\n")
    file.write("			<scale x=\"0.2\" y=\"0.2\" z=\"0.5\"/>\n")
    file.write("		</transform>\n")
    file.write("		<ref id=\"Water_Drop\"/>\n")
    file.write("	</shape>\n")

    file.write("	<shape type=\"obj\">\n")
    file.write("		<string name=\"filename\" value=\"static_drop_004.obj\"/>\n")
    file.write("		<transform name=\"toWorld\">\n")
    file.write("			<translate x=\"10\" y=\"0\" z=\"0\"/>\n")
    file.write("			<scale x=\"0.2\" y=\"0.2\" z=\"0.5\"/>\n")
    file.write("		</transform>\n")
    file.write("		<ref id=\"Water_Drop\"/>\n")
    file.write("	</shape>\n")


    file.write("\n")
    file.write("\n")
    file.write("\n")



