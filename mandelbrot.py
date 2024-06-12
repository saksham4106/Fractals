from PIL import Image, ImageDraw
WIDTH = 500
HEIGHT = 500
global draw

class Complex:
    def __init__(self, x, y):
        self.x = x
        self.y = y 
    
    def sqr(self):
        return Complex(self.x * self.x - self.y * self.y, 2 * self.x * self.y)
    
    def mod(self):
        return self.x * self.x + self.y * self.y
    
    def add(self, c2):
        return Complex(self.x + c2.x, self.y + c2.y)
            
    


im = Image.new('RGB', (WIDTH, HEIGHT), (0,0,0,0))
draw = ImageDraw.Draw(im)
for x in range(0, WIDTH):
    for y in range(0, HEIGHT):
        f = 125
        X = (x -250 ) / f
        Y = (-y + 250) / f

        c= Complex(X, Y)
        z = Complex(0.0, 0.0)

        for i in range(10):
            z = (z.sqr()).add(c)

        mod = z.mod()
        if mod == 0:
            g = 255
        else:
            g = (int) ((1 / mod) * 255)
        draw.point((X*f + 250, 250 - Y * f), (g // 2, g, g   ))    
        


im.save('mandelbrot.png', 'PNG', quality = 95)