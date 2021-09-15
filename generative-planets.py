
import cairo, PIL, argparse, math, random
from PIL import Image, ImageDraw

list_of_colors = [(145, 185, 141), (229, 192, 121), (210, 191, 88), (140, 190, 178), (255, 183, 10), (189, 190, 220),
 (221, 79, 91), (16, 182, 98), (227, 146, 80), (241, 133, 123), (110, 197, 233), (235, 205, 188), (197, 239, 247), (190, 144, 212),
 (41, 241, 195), (101, 198, 187), (255, 246, 143), (243, 156, 18), (189, 195, 199), (243, 241, 239)]

float_gen = lambda a, b: random.uniform(a, b)

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
        cr.arc(random.randint(0, width), random.randint(0, height), random.uniform(.1, 5), 0, 2*math.pi)
        cr.set_source_rgb(255, 255, 255)
        cr.fill()
    for x in range(0, yellow):
        cr.arc(random.randint(0, width), random.randint(0, height), random.uniform(.1, 5), 0, 2*math.pi)
        cr.set_source_rgb(1, 198/255, 127/255)
        cr.fill()
    for x in range(0, blue):
        cr.arc(random.randint(0, width), random.randint(0, height), random.uniform(.1, 5), 0, 2*math.pi)
        cr.set_source_rgb(167/255, 188/255, 1)
        cr.fill()


     
# def points_on_circum(r,n=100):
#                 points_positive = []
#                 for x in range(0,n+1):
#                     xcoord = (math.cos(2*math.pi/n*x)*r)
#                     ycoord = (math.sin(2*math.pi/n*x)*r)
#                     if(xcoord > 0 and ycoord > 0):
#                         points_positive.append((xcoord, ycoord))
#                 print(points_positive)
#                 return points_positive

def points_on_circum(r, width, height, border):
                print(r, "this is insive function")
                points_positive = []
                for x in range(0, 100):
                    xcoord = (math.cos(1.8*x) *r) + width/2 
                    ycoord = -1 * (math.sin(1.8*x) *r) + height - border
                    if((xcoord > 0 and xcoord < width-border) and (ycoord > 0 and ycoord < height - border)):
                        points_positive.append((xcoord, ycoord))
                # print(points_positive)
                return points_positive
    
# def points_on_circum(r, width ,n=100):
#     return [((-1*(math.cos(2*math.pi/n*x)*r) - width/2),math.sin(2*math.pi/n*x)*r) for x in range(0,n+1)]

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--width", help="Specify Width", default=3000, type=int)
    parser.add_argument("--height", help="Specify Height", default=2000, type=int)
    parser.add_argument("-o", "--orbit", help="Actual Orbits", action="store_true")
    parser.add_argument("-l", "--line", help=".", action="store_true")
    parser.add_argument("-s", "--sunsize", help=".", default=random.randint(200, 400), type=int)
    parser.add_argument("-bs", "--bordersize", help=".", default=50, type=int)
    parser.add_argument("-n", "--noise", help="Texture", default=.4, type=float)
    
    # white_star= int(input('white star number: '))
    # yellow_star= int(input('yellow star number: '))
    # blue_star= int(input('blue star number: '))
    
    white_star = 350
    blue_star = 30
    yellow_star = 60
    border_size = 25
    args = parser.parse_args()
    
    width, height = args.width, args.height
    # border_size = int(input('border size: '))
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

    for x in range(1, 20):
        next_size = random.randint(min_size, max_size)
        next_center = last_center - last_size - (next_size * 2) - distance_between_planets
        movement = [width/2 + (random.randint(0, width-border_size-next_center)/2), 
                    width/2 - (random.randint(0,width-border_size-next_center)/2)]
        move_line = random.choice(movement)
        
        if not(next_center - next_size < border_size):
            
            if(args.orbit):
                # cr, line, x, y, radius, r, g, b
                print(height - next_center - border_size, "this is at the orbit draw spot", x)
                draw_orbit(cr, 4, width/2, sun_center, height - next_center - border_size, .6, .6, .6)
                draw_circle_fill(cr, width/2, next_center, next_size*1.3, 0, 0, 0)
            elif(args.line):
                cr.move_to(border_size * 2, next_center)
                cr.line_to(width-(border_size*2), next_center)
                cr.stroke()
                draw_circle_fill(cr, move_line, next_center, next_size*1.5, 0, 0, 0)
                # draw_rings(cr, 2,move_line, next_center, next_size*1.5, 0, 0, 0)

            rand_color = random.choice(list_of_colors)
            while (rand_color is last_color):
                rand_color = random.choice(list_of_colors)

            last_color = rand_color

            r, g, b = rand_color[0]/255.0, rand_color[1]/255.0, rand_color[2]/255.0

            if(args.orbit):
                # what arg, x, y, radius, r, g, b
                    # x^ + y^ = r^
                # (cr, x, y, radius, ...)
                arc = height - next_center - border_size
                print(arc, "this is at the draw planet part", x)
                placement = random.choice(points_on_circum(arc, width, height, border_size))
                print (placement)
                # draw_circle_fill(cr, width/2, next_center, next_size, r, g, b)
                draw_circle_fill(cr, placement[0],placement[1], next_size, r, g, b)
                
            elif(args.line):
                   
                draw_circle_fill(cr, move_line, next_center, next_size, r, g, b)

            last_center = next_center
            last_size = next_size

            min_size += 5
            max_size += 5 * x

    draw_border(cr, border_size, sun_r, sun_g, sun_b, width, height)

    ims.write_to_png('Examples/Generative-Space-Flat-' + str(width) + 'w-' + str(height) + 'h.png')

    pil_image = Image.open('Examples/Generative-Space-Flat-' + str(width) + 'w-' + str(height) + 'h.png')
    pixels = pil_image.load()

    for i in range(pil_image.size[0]):
        for j in range(pil_image.size[1]):
            r, g, b = pixels[i, j]

            noise = float_gen(1.0 - args.noise, 1.0 + args.noise)
            pixels[i, j] = (int(r*noise), int(g*noise), int(b*noise))
    pil_image.save('Examples/Generative-Space-Texture-' + str(width) + 'w-' + str(height) + 'h.png')

if __name__ == "__main__":
    main()
    
   
    
   
    
    
