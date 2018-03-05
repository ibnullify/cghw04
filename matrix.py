import math

def make_translate( x, y, z ):
    arr = new_matrix();
    ident(arr);
    arr[3][0] = x
    arr[3][1] = y
    arr[3][2] = z
    return arr

def make_scale( x, y, z ):
    arr = new_matrix()
    ident(arr)
    arr[0][0] = x
    arr[1][1] = y
    arr[2][2] = z
    return arr

def make_rotX( theta ):    
    radians = math.radians(theta);
    arr = new_matrix()
    ident(arr)
    arr[1][1]=math.cos(radians)
    arr[2][1]=-math.sin(radians)
    arr[1][2]=math.sin(radians)
    arr[2][2]=math.cos(radians)
    return arr


def make_rotY( theta ):
    radians = math.radians(theta);
    arr = new_matrix()
    ident(arr)
    arr[0][0]=math.cos(radians)
    arr[0][3]=-math.sin(radians)
    arr[2][0]=math.sin(radians)
    arr[2][3]=math.cos(radians)
    return arr

def make_rotZ( theta ):
    radians = math.radians(theta);
    arr = new_matrix()
    ident(arr)
    arr[0][0]=math.cos(radians)
    arr[1][0]=-math.sin(radians)
    arr[0][1]=math.sin(radians)
    arr[1][1]=math.cos(radians)
    return arr

def print_matrix( matrix ):
    s = ''
    for r in range( len( matrix[0] ) ):
        for c in range( len(matrix) ):
            s+= str(matrix[c][r]) + ' '
        s+= '\n'
    print s

def ident( matrix ):
    for r in range( len( matrix[0] ) ):
        for c in range( len(matrix) ):
            if r == c:
                matrix[c][r] = 1
            else:
                matrix[c][r] = 0

#m1 * m2 -> m2
def matrix_mult( m1, m2 ):

    point = 0
    for row in m2:
        #get a copy of the next point
        tmp = row[:]
        
        for r in range(4):
            m2[point][r] = (m1[0][r] * tmp[0] +
                            m1[1][r] * tmp[1] +
                            m1[2][r] * tmp[2] +
                            m1[3][r] * tmp[3])
        point+= 1


def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m
