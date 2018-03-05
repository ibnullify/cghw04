from display import *
from matrix import *
from draw import *


def parse_file( fname, points, transform, screen, color ):
    f = open(fname)
    lines = f.readlines() 
    for i in range(len(lines)):
        if lines[i]=="line\n":
            params=lines[i+1].split(" ")
            add_edge(points,int(params[0]),int(params[1]),int(params[2]),int(params[3]),int(params[4]),int(params[5]))
        elif lines[i]=="ident\n":
            ident(transform)
        elif lines[i]=="scale\n":
            params=lines[i+1].split(" ")
            scale=make_scale(int(params[0]),int(params[1]),int(params[2]))
            matrix_mult(scale,transform)
        elif lines[i]=="move\n":
            params=lines[i+1].split(" ")
            translation=make_translate(int(params[0]),int(params[1]),int(params[2]))
            matrix_mult(translation,transform)
        elif lines[i]=="rotate\n":
            params=lines[i+1].split(" ")
            if params[0]=="x":
                rotation=make_rotX(int(params[1]))
            if params[0]=="y":
                rotation=make_rotY(int(params[1]))
            if params[0]=="z":
                rotation=make_rotZ(int(params[1]))
            matrix_mult(rotation,transform)
        elif lines[i]=="apply\n":
            matrix_mult(transform,points)
        elif lines[i]=="display\n":
            for p in range(len(points)):
                for x in range(len(points[0])):
                    points[p][x]=int(points[p][x])
            clear_screen(screen)
            draw_lines(points,screen,color)
            display(screen)
        elif lines[i]=="save\n":
            save_extension(screen,lines[i+1].strip())
        elif lines[i]=="quit\n":
            break


"""
Goes through the file named filename and performs all of the actions listed in that file.
The file follows the following format:
     Every command is a single character that takes up a line
     Any command that requires arguments must have those arguments in the second line.
     The commands are as follows:
         line: add a line to the edge matrix - 
	    takes 6 arguemnts (x0, y0, z0, x1, y1, z1)
	 ident: set the transform matrix to the identity matrix - 
	 scale: create a scale matrix, 
	    then multiply the transform matrix by the scale matrix - 
	    takes 3 arguments (sx, sy, sz)
	 move: create a translation matrix, 
	    then multiply the transform matrix by the translation matrix - 
	    takes 3 arguments (tx, ty, tz)
	 rotate: create a rotation matrix,
	    then multiply the transform matrix by the rotation matrix -
	    takes 2 arguments (axis, theta) axis should be x, y or z
	 apply: apply the current transformation matrix to the 
	    edge matrix
	 display: draw the lines of the edge matrix to the screen
	    display the screen
	 save: draw the lines of the edge matrix to the screen
	    save the screen to a file -
	    takes 1 argument (file name)
	 quit: end parsing

See the file script for an example of the file format
"""

