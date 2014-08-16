import re

def process_grid( filename ):
    """ input: a file containing
            grid size on the first line: #x#
            bomb locations on subsequent lines: #,#
        returns: string of grid, space separated locations
            X is a bomb
            # is adjacent bombs
    """
    with open(filename, 'r') as f:
        p = re.compile("([0-9]+)x([0-9]+)")
        m = p.match(f.readline())

        # size args
        if m:
            # board size
            xsize=int(m.group(1))
            ysize=int(m.group(2))

            board = [[]] * (ysize+1)
            # initialize board
            for i in range(ysize):
                #print i, " ", xsize, " ", ysize
                board[i] = [0] * (xsize+1)

            # parse a bombs coordinaes'
            p = re.compile("([0-9]+),([0-9]+)")

            # read another consecutive bomb line
            m = p.match(f.readline())
            while m:
                bx=int(m.group(1))
                by=int(m.group(2))
                if (bx <= xsize) & (by <= ysize):
                    board[bx][by] = "X"
                m = p.match(f.readline())

            grid = ""
            for y in range(ysize):
                for x in range(xsize):
                    if not (board[x][y] == "X"):
                        board[x][y] = adjacent(board,bx,by,x,y)
                    if (x == xsize-1):
                        grid += str(board[x][y])
                    else:
                        grid += str(board[x][y]) + " "
                if not (y == ysize):
                    grid += "\n"
            return grid
        else:
            return null
    f.close()

def adjacent(board, bx, by, x, y):
    count = 0
    top = False
    bot = False
    left = False
    right = False
    if y > 0:
        top=True
    if y <= by:
        bot=True
    if x > 0:
        left=True
    if x <= bx:
        right=True
    if (top & left):
        if (board[x-1][y-1] == "X"):
            count += 1
    if (top):
        if (board[x][y-1] == "X"):
            count = count + 1
    if (top & right):
        if (board[x+1][y-1] == "X"):
            count += 1
    if (left):
        if (board[x-1][y] == "X"):
            count += 1
    if (right):
        if (board[x+1][y] == "X"):
            count += 1
    if (bot & left):
        if (board[x-1][y+1] == "X"):
            count += 1
    if (bot):
        if (board[x][y+1] == "X"):
            count += 1
    if (bot & right):
        if (board[x+1][y+1] == "X"):
            count += 1
    return count

