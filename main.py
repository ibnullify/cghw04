from display import *
from draw import *
from parser import *
from matrix import *

screen = new_screen()
color = [ 0, 255, 0 ]
edges = []
transform = new_matrix()


def parse_file( fname, points, transform, screen, color ):
    points = new_matrix()
    f = open(fname,'r')
    lines = f.readlines()
    for i in range(len(lines)):
        #LINES
        if (lines[i] == "line\n"):
            coors = lines[i+1].split(" ")
            x0 = int(coors[0])
            y0 = int(coors[1])
            z0 = int(coors[2])
            x1 = int(coors[3])
            y1 = int(coors[4])
            z1 = int(coors[5])
            add_edge(points, x0, y0, z0, x1, y1, z1)
            print "---------------ADDED LINE-------------"
            

        #IDENT
        elif (lines[i] == "ident\n"):
            print "------------IDENTITY----------"
            ident(transform)
            print_matrix(transform)

        #SCALE
        elif (lines[i] == "scale\n"):
            print "-----------SCALING-----------"
            triple = lines[i+1].split(" ")
            x = int(triple[0])
            y = int(triple[1])
            z = int(triple[2])
            scale = make_scale(x, y, z)
            matrix_mult(scale, transform)
            print_matrix(transform)

        #MOVE
        elif (lines[i] == "move\n"):
            print "------------MOVING-----------"
            triple = lines[i+1].split(" ")
            x = int(triple[0])
            y = int(triple[1])
            z = int(triple[2])
            translate = make_translate(x, y, z)
            matrix_mult(translate, transform)
            print_matrix(transform)

        #ROTATE
        elif (lines[i] == "rotate\n"):
            param = lines[i+1].split(" ")
            direct = param[0]
            angle = int(param[1])
            if (direct == "x"):
                print "-----------ROTATING BY X------------"
                rotate = make_rotX(angle)
            elif (direct == "y"):
                print "-----------ROTATING BY Y------------"
                rotate = make_rotY(angle)
            else:
                print "-----------ROTATING BY Z------------"
                rotate = make_rotZ(angle)
            matrix_mult(rotate, transform)
            print_matrix(transform)

        #APPLY
        elif (lines[i] == "apply\n"):
            print "----------------APPLYING--------------"
            matrix_mult(transform, points)
            #Integerize
            for c in range(len(points)):
                for r in range(len(points[0])):
                    points[c][r] = int(points[c][r])
            

        #DISPLAY
        elif (lines[i] == "display\n"):
            clear_screen(screen)
            draw_lines(points, screen, color)
            display(screen)

        #SAVE
        elif (lines[i] == "save\n"):
            image = lines[i+1].split()
            save_extension(screen, image[0])

        #ANYTHING ELSE
        else:
            pass

        
filename = 'newscript'
#filename = 'script'
parse_file( filename, edges, transform, screen, color )
