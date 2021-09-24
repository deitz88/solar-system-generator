



import cairo
import PIL
import argparse
import math
import random
import copy
from PIL import Image, ImageDraw

list_of_colors = [(145, 185, 141), (229, 192, 121), (210, 191, 88), (140, 190, 178), (255, 183, 10), (189, 190, 220),
                    (221, 79, 91), (16, 182, 98), (227, 146, 80), (241, 133, 123), (110,
                                                                                    197, 233), (235, 205, 188), (197, 239, 247), (190, 144, 212),
                    (41, 241, 195), (101, 198, 187), (255, 246, 143), (243, 156, 18), (189, 195, 199), (243, 241, 239)]

def float_gen(a, b): return random.uniform(a, b)

def draw_orbit(cr, line, x, y, radius, r, g, b):
    cr.set_line_width(line)
    cr.arc(x, y, radius, 0, 2*math.pi)
    cr.stroke()

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

def planet_rings(cr, x, y, size):
    color = random.choice(list_of_colors)
    # orig black spaceholder
    draw_circle_fill(cr, x, y, size*1.5, 0, 0, 0)
    # ring color
    draw_circle_fill(cr, x, y, size*1.3,
                        color[0]/255, color[1]/255, color[2]/255)
    # inner layer of black
    draw_circle_fill(cr, x, y, size*1.25, 0, 0, 0)

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
        if((xcoord > 0 and xcoord < width - border+50) and (ycoord > 0 and ycoord < height - border + 100)):
            points_positive.append((xcoord, ycoord))
    return points_positive



def main():

####### VARIABLES FOR RENDERING ########
    # height/width by px
    width = 3000
    height = 2000
    # orbit or lione
    rendering = 'orbit'
    white_star = 400
    blue_star = 25
    yellow_star = 60
    border_size = 40
    # random placements of planets
    rand = True
    # 0 < noise < 1
    noise = .35
    sun_size = random.randint(100, 400)
    # rings on planets?
    make_rings = True
    
    
    sun_center = height - border_size

    ims = cairo.ImageSurface(cairo.FORMAT_ARGB32, width, height)
    cr = cairo.Context(ims)


    draw_background(cr, width, height, white_star, yellow_star, blue_star)
    

    sun_color = random.choice(list_of_colors)
    sun_r, sun_g, sun_b = sun_color[0] / \
        255.0, sun_color[1]/255.0, sun_color[2]/255.0

    draw_circle_fill(cr, width/2, sun_center,
                        sun_size, sun_r, sun_g, sun_b)

    distance_between_planets = 20
    last_center = sun_center
    last_size = sun_size
    last_color = sun_color

    min_size = 5
    max_size = 70

    for x in range(1, 20):
        next_size = random.randint(min_size, max_size)
        next_center = last_center - last_size - \
            (next_size * 2) - distance_between_planets
        movement = [width/2 + (random.randint(0, width-border_size-next_center)/2),
                    width/2 - (random.randint(0, width-border_size-next_center)/2)]
        move_line = random.choice(movement)
        rings = random.randint(1, 3)

        if not(next_center - next_size < border_size):
            arc = height - next_center - border_size
            placement = random.choice(points_on_circum(
                arc, width, height, border_size))

            if(rendering == 'orbit'):
                # here here here
                draw_orbit(cr, 4, width/2, sun_center, height -
                            next_center - border_size, .6, .6, .6)
                if(rand == True):
                    if rings > 2 and make_rings==True and x > 4:
                        planet_rings(
                            cr, placement[0], placement[1], next_size)
                    else:
                        draw_circle_fill(
                            cr, placement[0], placement[1], next_size*1.5, 0, 0, 0)
                elif(rand == False):
                    if rings > 2 and make_rings == True and x > 4:
                        planet_rings(cr, width/2, next_center, next_size)
                    else:
                        draw_circle_fill(cr, width/2, next_center,
                                        next_size*1.5, 0, 0, 0)
            elif(rendering == 'line'):
                cr.move_to(border_size * 2, next_center)
                cr.line_to(width-(border_size*2), next_center)
                cr.stroke()
                if(rand == True):
                    if rings > 2 and make_rings==True and x > 4:
                        planet_rings(cr, move_line, next_center, next_size)
                    else:
                        draw_circle_fill(cr, move_line, next_center,
                                        next_size*1.5, 0, 0, 0)
                elif(rand == False):
                    if rings > 2 and make_rings==True and x > 4:
                        planet_rings(cr, width/2,next_center, next_size)
                    else:
                        draw_circle_fill(cr, width/2, next_center,
                                        next_size*1.5, 0, 0, 0)

            rand_color = random.choice(list_of_colors)
            while (rand_color is last_color):
                rand_color = random.choice(list_of_colors)

            last_color = rand_color

            r, g, b = rand_color[0]/255.0, rand_color[1] / \
                255.0, rand_color[2]/255.0

            if(rendering == 'orbit'):
                if(rand == True):
                    draw_circle_fill(
                        cr, placement[0], placement[1], next_size, r, g, b)
                elif(rand == False):
                    draw_circle_fill(cr, width/2, next_center,
                                        next_size, r, g, b)

            elif(rendering == 'line'):
                if(rand == True):
                    draw_circle_fill(cr, move_line, next_center,
                                        next_size, r, g, b)
                elif(rand == False):
                    draw_circle_fill(cr, width/2, next_center,
                                        next_size, r, g, b)

            last_center = next_center
            last_size = next_size

            min_size += 5
            max_size += 5 * x

    draw_border(cr, border_size, sun_r, sun_g, sun_b, width, height)
    ims.write_to_png('Examples/Generative-Space-Flat-' +
                        str(width) + 'w-' + str(height) + 'h.png')

    pil_image = Image.open('Examples/Generative-Space-Flat-' +
                            str(width) + 'w-' + str(height) + 'h.png')
    pixels = pil_image.load()

    for i in range(pil_image.size[0]):
        for j in range(pil_image.size[1]):
            r, g, b = pixels[i, j]

            noise = float_gen(1.0 - noise, 1.0 + noise)
            pixels[i, j] = (int(r*noise), int(g*noise), int(b*noise))
    pil_image.save('Examples/Generative-Space-Texture-' +
                    str(width) + 'w-' + str(height) + 'h.png')

main()


