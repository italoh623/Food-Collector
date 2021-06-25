from PIL import Image
from pprint import pprint

path = input('path to map: ')
im = Image.open(path) 
pix = im.load()
rgb_im = im.convert('RGB')

width, height = rgb_im.size

# colors
SIZE = 20
WALL = (0,0,0)
SAND = (253, 244, 121)
MUD = (141, 80, 16)
WATER = (10, 38, 234)
START = (128, 128, 128)
GOAL = (236, 48, 26)

s = int(SIZE/2) - 1

grid = []
for x in range(s, width, SIZE):
    l = []
    for y in range(s, height, SIZE):
        px = rgb_im.getpixel((x,y))
        if px == WALL:
            l.append(-1)
        elif px == SAND:
            l.append(0)
        elif px == MUD:
            l.append(1)
        elif px == WATER:
            l.append(2)
        elif px == START:
            l.append(3)
        elif px == GOAL:
            l.append(4)
        else:
            print(px)
    grid.append(l)

print('grid = ')
pprint(grid)

# with open('maps/2.txt', 'w') as f:
#     f.write('grid = [')
#     for line in grid:
#         f.write('[' + ','.join([str(ch) for ch in line]) + '],\n\t')
#     f.write(']')