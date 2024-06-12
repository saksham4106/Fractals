from webbrowser import get
from PIL import Image, ImageDraw
import random
import time
import pygame
import numpy as np

t0 = time.time()
global draw
def t(x,y,a,b,c,d,tx,ty):
    return [a *x + b * y + tx , c * x + d * y + ty]


a1,b1,c1,d1,tx1,ty1,w1 =    0,     0      ,0      ,0.16,     0,    0,    0.01
a2,b2,c2,d2,tx2,ty2,w2 =    0.85,  0.04,  -0.04   ,0.85,     0,    1.60, 0.85
a3,b3,c3,d3,tx3,ty3,w3 =    0.20,  -0.26  ,0.23   ,0.22,     0,    1.60, 0.07
a4,b4,c4,d4,tx4,ty4,w4 =    -0.15, 0.30,   0.26,   0.24,     0,    0.44, 0.07


HEIGHT = 600
WIDTH = 600
def generateImage():
    im = Image.new('RGB', (WIDTH, HEIGHT), (0,0,0,0))
    draw = ImageDraw.Draw(im)
    for x in range(0,WIDTH):
        for y in range(0, HEIGHT):
            draw.point([x,y], (0,0,0))

    x,y = 0,0
    x1,y1 = 0, 0


    for i in range(0 ,WIDTH*HEIGHT):
        r = random.random()
        if r <= w1:
            upd = t(x,y,a1,b1,c1,d1,tx1,ty1)
            x1,y1 = upd[0], upd[1]
        if w1 <= r <= w2 + w1:
            upd = t(x,y,a2,b2,c2,d2,tx2,ty2)
            x1,y1 = upd[0], upd[1]
        if w1 + w2 <= r <= w3 + w1 + w2:
            upd = t(x,y,a3,b3,c3,d3,tx3,ty3)
            x1,y1 = upd[0], upd[1]
        if w1 + w2 + w3 <= r <= w4 + w1 + w2 + w3:
            upd = t(x,y,a4,b4,c4,d4,tx4,ty4)
            x1,y1 = upd[0], upd[1]

        
        draw.point(((x1 + 5) * 50, HEIGHT - y1 * 50), (255,255,255))
        x = x1
        y = y1
    return im




im = generateImage()
# im.save('output1.png', 'PNG')

t1 = time.time()
print("Time Elapsed: ", t1 - t0)




pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hello")
clock = pygame.time.Clock()


done = False
while not done:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            done = True
        screen.fill((255,255,255))

        npImage = np.asarray(im)
        npImage = np.rot90(npImage, 1)
        surface = pygame.surfarray.make_surface(npImage)
        pygame.transform.flip(surface, True, True)
        screen.blit(surface, (0, 0))
        pygame.display.update()
        # pygame.display.flip()
        clock.tick(60)

        
