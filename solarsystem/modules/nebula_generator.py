    
import cairo, sys, copy, math, random

def generate_nebula(shapes, max_shapes):
    float_gen = lambda a, b: random.uniform(a, b)

    colors = []
    for x in range(10):
        colors.append((0,0,0))
    for i in range(15):
        colors.append((float_gen(.1, 1), float_gen(.1, .5), float_gen(.1, 1)))
        colors.append((0, 0, 0))

    def draw_background(cr, width, height):
        cr.rectangle(0, 0, width, height)
        cr.set_source_rgb(0, 0, 0)
        cr.fill()

    def octagon(x_orig, y_orig, side):
        x = x_orig
        y = y_orig
        d = side / math.sqrt(2)

        oct = []

        oct.append((x, y))

        x += side
        oct.append((x, y))

        x += d
        y += d
        oct.append((x, y))

        y += side
        oct.append((x, y))

        x -= d
        y += d
        oct.append((x, y))

        x -= side
        oct.append((x, y))

        x -= d
        y -= d
        oct.append((x, y))

        y -= side
        oct.append((x, y))

        x += d
        y -= d
        oct.append((x, y))

        return oct

    def deform(shape, iterations, variance):
        for i in range(iterations):
            for j in range(len(shape)-1, 0, -1):
                midpoint = ((shape[j-1][0] + shape[j][0])/2 + float_gen(-variance, variance), (shape[j-1][1] + shape[j][1])/2 + float_gen(-variance, variance))
                shape.insert(j, midpoint)
        return shape

    min_shape = shapes
    max_num = max_shapes
    def main():

        # size of canvas
        width = 3000
        height = 2000
        # initial 
        initial = 10
        deviation = 1000
        # deformations
        basedeforms = 1
        finaldeforms = 3
        # oct nums
        minshapes = int(min_shape)
        maxshapes = int(max_num)
        # color presense
        shapealpha = .007

        ims = cairo.ImageSurface(cairo.FORMAT_ARGB32, width, height)
        cr = cairo.Context(ims)

        cr.set_source_rgb(.9, .9, .9)
        cr.rectangle(0, 0, width, height)
        cr.fill()
        
        draw_background(cr, width, height)

        cr.set_line_width(1)

        for p in range(-int(height*.2), int(height*1.2), 60):
            cr.set_source_rgba(random.choice(colors)[0], random.choice(colors)[1], random.choice(colors)[2], shapealpha)

            shape = octagon(random.randint(-100, width+100), p, random.randint(100, 300))
            baseshape = deform(shape, basedeforms, initial)

            for j in range(random.randint(minshapes, maxshapes)):
                tempshape = copy.deepcopy(baseshape)
                layer = deform(tempshape, finaldeforms, deviation)

                for i in range(len(layer)):
                    cr.line_to(layer[i][0], layer[i][1])
                cr.fill()
        
        ims.write_to_png('../solarsystem/space/static/renderings/nebula.png')
        

    main()
