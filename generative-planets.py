
import cairo
import PIL
import argparse
import math
import random
import copy
from PIL import Image, ImageDraw
# from test2 import make_nebula

list_of_colors = [(145, 185, 141), (229, 192, 121), (210, 191, 88), (140, 190, 178), (255, 183, 10), (189, 190, 220),
                  (221, 79, 91), (16, 182, 98), (227, 146, 80), (241, 133, 123), (110,
                                                                                  197, 233), (235, 205, 188), (197, 239, 247), (190, 144, 212),
                  (41, 241, 195), (101, 198, 187), (255, 246, 143), (243, 156, 18), (189, 195, 199), (243, 241, 239)]


def float_gen(a, b): return random.uniform(a, b)

def draw_orbit(cr, line, x, y, radius, r, g, b):
    cr.set_line_width(line)
    cr.arc(x, y, radius, 0, 2*math.pi)
    cr.stroke()
    
# # draw_rings(cr, move_line, next_center, next_size*1.5, 0, 0, 0)
# # currently broken - line change in func makes planet lines thicker with radius of rings
# def draw_rings(cr, line, x, y, radius, r, g, b):
#     cr.set_line_width(line)
#     cr.arc(x, y, radius*1.2, 0, 2*math.pi)
#     cr.stroke()


def draw_circle_fill(cr, x, y, radius, r, g, b):
    cr.set_source_rgb(r, g, b)
    cr.arc(x, y, radius, 0, 2*math.pi)
    cr.fill()


def draw_border(cr, size, r, g, b, width, height):
    cr.set_source_rgb(r, g, b)
    cr.rectangle(0, 0, size, height)
    cr.rectangle(0, 0, width, size)
    cr.rectangle(0, height-size, width, size)
    cr.rectangle(width-size, 0, size, height)
    cr.fill()


def draw_background(cr, width, height, white, yellow, blue):
    cr.rectangle(0, 0, width, height)
    cr.set_source_rgb(0, 0, 0)
    cr.fill()
    for x in range(0, white):
        # x, y, radius, angle1, angle2
        cr.arc(random.randint(0, width), random.randint(
            0, height), random.uniform(.1, 5), 0, 2*math.pi)
        cr.set_source_rgb(255, 255, 255)
        cr.fill()
    for x in range(0, yellow):
        cr.arc(random.randint(0, width), random.randint(
            0, height), random.uniform(.1, 5), 0, 2*math.pi)
        cr.set_source_rgb(1, 198/255, 127/255)
        cr.fill()
    for x in range(0, blue):
        cr.arc(random.randint(0, width), random.randint(
            0, height), random.uniform(.1, 5), 0, 2*math.pi)
        cr.set_source_rgb(167/255, 188/255, 1)
        cr.fill()

# for randomization along orbit arc
def points_on_circum(r, width, height, border):
    points_positive = []
    for x in range(0, 100):
        xcoord = (math.cos(1.8*x) * r) + width/2
        ycoord = -1 * (math.sin(1.8*x) * r) + height - border
        if((xcoord > 0 and xcoord < width-border+30) and (ycoord > 0 and ycoord < height - border + 100)):
            points_positive.append((xcoord, ycoord))
    return points_positive


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--width", help="Specify Width",
                        default=3000, type=int)
    parser.add_argument("--height", help="Specify Height",
                        default=2000, type=int)
    parser.add_argument(
        "-o", "--orbit", help="Actual Orbits", default=True, action="store_true")
    parser.add_argument("-l", "--line", help=".", action="store_true")
    parser.add_argument("-s", "--sunsize", help=".",
                        default=random.randint(100, 400), type=int)
    parser.add_argument("-bs", "--bordersize", help=".", default=50, type=int)
    parser.add_argument("-n", "--noise", help="Texture",
                        default=.4, type=float)
    parser.add_argument("-r", "--random", help="Random placements", default=.4, type=float)

    # white_star= int(input('white star number: '))
    # yellow_star= int(input('yellow star number: '))
    # blue_star= int(input('blue star number: '))
    # border_size = int(input('border size: '))

    white_star = 1000
    blue_star = 30
    yellow_star = 60
    border_size = 25
    args = parser.parse_args()

    width, height = args.width, args.height
    sun_size = args.sunsize

    sun_center = height - border_size

    ims = cairo.ImageSurface(cairo.FORMAT_ARGB32, width, height)
    cr = cairo.Context(ims)

    draw_background(cr, width, height, white_star, yellow_star, blue_star)

    sun_color = random.choice(list_of_colors)
    sun_r, sun_g, sun_b = sun_color[0]/255.0, sun_color[1]/255.0, sun_color[2]/255.0

    draw_circle_fill(cr, width/2, sun_center, sun_size, sun_r, sun_g, sun_b)

    distance_between_planets = 20
    last_center = sun_center
    last_size = sun_size
    last_color = sun_color

    min_size = 5
    max_size = 70
    
    # def make_nebula():

    #     float_gen = lambda a, b: random.uniform(a, b)

    #     colors = []
    #     for i in range(15):
    #         colors.append((float_gen(.1, 1.3), float_gen(.1, .5), float_gen(.1, 1.3)))
    #         colors.append((0, 0, 0))

    #     def octagon(x_orig, y_orig, side):
    #         side = side * random.randint(1, 3)
    #         x = x_orig
    #         y = y_orig
    #         d = side / math.sqrt(2)

    #         oct = []

    #         oct.append((x, y))

    #         x += side
    #         oct.append((x, y))

    #         x += d
    #         y += d
    #         oct.append((x, y))

    #         y += side
    #         oct.append((x, y))

    #         x -= d
    #         y += d
    #         oct.append((x, y))

    #         x -= side
    #         oct.append((x, y))

    #         x -= d
    #         y -= d
    #         oct.append((x, y))

    #         y -= side
    #         oct.append((x, y))

    #         x += d
    #         y -= d
    #         oct.append((x, y))

    #         return oct

    #     def deform(shape, iterations, variance):
    #         for i in range(iterations):
    #             for j in range(len(shape)-1, 0, -1):
    #                 midpoint = ((shape[j-1][0] + shape[j][0])/2 + float_gen(-variance, variance), (shape[j-1][1] + shape[j][1])/2 + float_gen(-variance, variance))
    #                 shape.insert(j, midpoint)
    #         return shape

    #     def build():
            
    #         initial = 1
    #         deviation = 250
    #         basedeforms = 1
    #         finaldeforms = 3
    #         minshapes = 20
    #         maxshapes = 200
    #         shapealpha = .008

    #         # cr.set_source_rgb(0, 0, 0)
        
    #         # cr.rectangle(0, 0, width, height)
            
    #         # cr.fill()
            

    #         cr.set_line_width(1)

    #         for p in range(-int((height*.2)/3), int((height*1.2)/3), 80):
    #             cr.set_source_rgba(random.choice(colors)[0], random.choice(colors)[1], random.choice(colors)[2], shapealpha)

    #             shape = octagon(random.randint(width*.3, width*.8), random.randint(1, height), random.randint(4, 30))
                
    #             baseshape = deform(shape, basedeforms, initial)

    #             for j in range(random.randint(minshapes, maxshapes)):
    #                 tempshape = copy.deepcopy(baseshape)
    #                 layer = deform(tempshape, finaldeforms, deviation)

    #                 for i in range(len(layer)):
    #                     cr.line_to(layer[i][0], layer[i][1])
    #                 cr.fill()

    #     build()
    
    # make_nebula()
    for x in range(1, 20):
        next_size = random.randint(min_size, max_size)
        next_center = last_center - last_size - \
            (next_size * 2) - distance_between_planets
        movement = [width/2 + (random.randint(0, width-border_size-next_center)/2),
                    width/2 - (random.randint(0, width-border_size-next_center)/2)]
        move_line = random.choice(movement)

        if not(next_center - next_size < border_size):
            arc = height - next_center - border_size
            placement = random.choice(points_on_circum(
                arc, width, height, border_size))

            if(args.orbit):
                draw_orbit(cr, 4, width/2, sun_center, height -
                           next_center - border_size, .6, .6, .6)
                if(args.random < 5):
                    draw_circle_fill(
                        cr, placement[0], placement[1], next_size*1.3, 0, 0, 0)
                elif(args.random > 5):
                    draw_circle_fill(cr, width/2, next_center,
                                     next_size*1.3, 0, 0, 0)
            elif(args.line):
                cr.move_to(border_size * 2, next_center)
                cr.line_to(width-(border_size*2), next_center)
                cr.stroke()
                if(args.random < 5):
                    draw_circle_fill(cr, move_line, next_center,
                                    next_size*1.5, 0, 0, 0)
                elif(args.random > 5):
                    draw_circle_fill(cr, width/2, next_center,
                                    next_size*1.5, 0, 0, 0)
                    

            rand_color = random.choice(list_of_colors)
            while (rand_color is last_color):
                rand_color = random.choice(list_of_colors)

            last_color = rand_color

            r, g, b = rand_color[0]/255.0, rand_color[1] / \
                255.0, rand_color[2]/255.0

            if(args.orbit):
                if(args.random < 5):
                    draw_circle_fill(
                        cr, placement[0], placement[1], next_size, r, g, b)
                elif(args.random > 5):
                    draw_circle_fill(cr, width/2, next_center,
                                     next_size, r, g, b)

            elif(args.line):
                if(args.random < 5):
                    draw_circle_fill(cr, move_line, next_center,
                                    next_size, r, g, b)
                elif(args.random > 5):
                    draw_circle_fill(cr, width/2, next_center,
                                 next_size, r, g, b)

            last_center = next_center
            last_size = next_size

            min_size += 5
            max_size += 5 * x

    draw_border(cr, border_size, sun_r, sun_g, sun_b, width, height)

    ims.write_to_png('public/media/Generative-Space-Flat-' +
                     str(width) + 'w-' + str(height) + 'h.png')

    pil_image = Image.open('public/media/Generative-Space-Flat-' +
                           str(width) + 'w-' + str(height) + 'h.png')
    pixels = pil_image.load()

    for i in range(pil_image.size[0]):
        for j in range(pil_image.size[1]):
            r, g, b = pixels[i, j]

            noise = float_gen(1.0 - args.noise, 1.0 + args.noise)
            pixels[i, j] = (int(r*noise), int(g*noise), int(b*noise))
    pil_image.save('public/media/Generative-Space-Texture-' +
                   str(width) + 'w-' + str(height) + 'h.png')


if __name__ == "__main__":
    main()
