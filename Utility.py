


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
    file.write("		<integer name=\"maxDepth\" value=\"20\"/>\n")
    file.write("	</integrator>\n")