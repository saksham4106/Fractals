from PIL import Image, ImageDraw
import random
import time

t0= time.time()
global draw

class point:
    def __init__(self, x, y) -> None:
        self.x = x 
        self.y = y
        draw.point([self.x, self.y], (255,255,255))


def generatePoints(vertices):
    init_v = point(250, 250)
    for i in range(1000000):
        dest = vertices[int(3 * random.random())]
        new_v = point((init_v.x + dest.x) / 2,(init_v.y + dest.y)  /2)
        init_v = new_v


WIDTH = 500
HEIGHT = 500
im = Image.new('RGB', (WIDTH, HEIGHT), (0,0,0,0))
draw = ImageDraw.Draw(im)
for x in range(0,WIDTH):
    for y in range(0, HEIGHT):
        draw.point([x,y], (0,0,0))

v2 = point(0, HEIGHT)
v1 = point(WIDTH,HEIGHT)
v3 = point(WIDTH // 2,0)

generatePoints([v1,v2,v3])
im.save('sierpinski_triangle.png', 'PNG')

t1 = time.time()
print("Time elapsed: ", t1 - t0)