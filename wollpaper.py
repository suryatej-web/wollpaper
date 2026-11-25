import math
import random
import sys
from PIL import Image, ImageDraw

WIDTH , HEIGHT = 2500 , 1400
SCALE = 1

seed = int(sys.argv[1]) if len(sys.argv) > 1 else random.randrange(1000)
rng = random.Random(seed)
hue = rng.randrange(360)
print("seed:", seed)
leafs =[
    ("pink" , 345),
    ("lavender", 285),
    ("peach", 12),
    ("ice blue", 195),
    ("golden" , 45),
    ("coral", 358),
    ("mint", 150),
]
sky_hue = rng.choice([335, 270, 25, 200 ,45 , 215])

# (tiny details for my stupid brain to remmber so that the code makes sense later 335 is pink, 270 is purple ,25 is orange ,200 is light blue ,45 is yellow ,215 is blue :3)

def hsl(h , s , l):
    l= max(0 ,min (100 , l))
    s= max(0 ,min (100 ,s))
    return f"hsl({round(h) %360}, {round(s)}%, {round(l)}%)"
# ( one more tiny note for me to remmebr here the two max(0, min(100)) lines keep the saturation and lightness between those two nums so that the code doesnt take a bad colour  and spoil da wollpaper :3 (very sugoi mechanics imo))
image = Image.new("RGB" , (WIDTH , HEIGHT))
draw = ImageDraw.Draw(image)
# (so dis part of da code is used to create a blank picture and a supposed pen to draw on it :O)
for y in range(HEIGHT):
    t = y / HEIGHT
    draw.line([(0,y), (WIDTH, y)], fill=hsl(sky_hue + 30 * t, 50 ,93 - 18 *t))
    # (ok ok so this part of da code is used to get the baground with a slight diffrent hue and apparently it gets darker as the t grows , which leads to a gradient ngl its still a bit confusing but i get the gist of it ) 
sun_x = rng.randrange(WIDTH // 5 , WIDTH *4 //5)
sun_y = rng.randrange(HEIGHT // 5 , HEIGHT //3)
r = rng.randrange(int(HEIGHT* 0.06), int(HEIGHT *0.11))
# (here dis code help pick a random position and size for the sun :O)
draw.ellipse([sun_x - r, sun_y - r, sun_x + r, sun_y +r], fill=hsl(sky_hue + 15, 90 ,98))
# (so dis line draws the sun as a circle on the canvas by making the height and width equal (i still did not understand how this works but meh))
def grow_tree( x , y , length , t , blossom_hue):
    # (so this line is a reusable code for drawing one tree it isnt called yet ofc )
    tips =[]
    #(empty list to store blossoms)
    trunk= hsl(15 ,25, 50 - 30 * t)
    #(brown colour  for the trunk :3)
    draw.line([(x,HEIGHT +10), (x,y)], fill=trunk, width=max(1, round(length *0.12)))
    def branch(x, y, angle, length, width, depth):
        #(dis function draws the branch where the angle is the direction and width is the thickness and depth is the split count)
        x2 = x + length * math.cos(angle)
        y2 = y - length * math.sin(angle)
        #(this finds the ending of the branch using trig :o here y - is used cuz y grows downwards apparently :o)
        draw.line([(x, y), (x2, y2)], fill=trunk, width=max(1, round(width)))
        #(draws da branch)
        if depth <=4:
            tips.append((x2, y2))
            #(saves the end tip to add blossoms hehe )
        if depth ==0:
            return
            #(stops at zero so that it doesnt spread forever)
        kids = 2 if rng.random() <0.7 else 3  
        #(gamble btw 2 or 3 branches)
        for i in range(kids):
            turn = (i - (kids - 1) /2) * 0.7 + rng.uniform(-0.2, 0.2)
            branch(x2, y2, angle + turn, length * rng.uniform(0.7, 0.85), width * 0.7, depth -1)
            #(this block is the part that draws the branches and turns them into a tree)
    branch(x, y, math.pi / 2 + rng.uniform(-0.15, 0.15), length, length * 0.12, 8)
    #(this starts the whole tree the math.pi points straight up)
    for tx , ty in tips:
        for _ in range(4):
            #(for each tip it draws 4 blossoms)
            bx = tx + rng.gauss(0, length * 0.06)
            by = ty + rng.gauss(0, length * 0.06)
            #(moves the blossoms away from the tip and gauss uses a bell curve to make it look more natural)
            br = length * rng.uniform(0.02, 0.045)
            color = hsl(blossom_hue + rng.uniform(-8,8), 70 +10 * t, 88 - 18 * t + rng.uniform(-8, 6))
            #(this is the blossom color it makes the near trees look more saturated and slightly darker)
            draw.ellipse([bx - br, by -br, bx + br, by + br], fill =color)
            #(dis draws the blossoms as a circle )
tree_count = rng.randint(5,7)
depths = sorted(rng.random() for _ in range(tree_count))
petal_hues =[]
#(chooses 5 to 7 trees and sorts them so that far trees come first and the near trees come last and the near trees are drawn on the top)
for i, t in enumerate(depths):
   x= (i + 0.5 )/ tree_count * WIDTH + rng.uniform(-0.05, 0.05) * WIDTH
   y= HEIGHT * (0.58 + 0.2 * t)
   size = HEIGHT * (0.07 + 0.07 * t)
  #(loop tru the trees and spreads the tress in an even row  with a little shift so they arnt in a perfect row  and the far trees  start higher up and are smoller and  the near trees are lower and bigger)
   color_name, hue = rng.choice(leafs)
   petal_hues.append(hue)
   print(f"tree {i +1}: {color_name}")
   grow_tree(x, y, size, t, hue)
   #(picks a random color pair remmbers the hue for the blossom and prints color name then draws tree)
for _ in range(250):
   px, py = rng.uniform(0, WIDTH), rng.uniform(0, HEIGHT)
   pr = rng.uniform(3, 9) * SCALE
   draw.ellipse([px - pr, py -pr * 0.6, px +pr, py +pr * 0.6], fill=hsl(rng.choice(petal_hues), 70, 92))
   #(250 times it draws a oval in one the  tree colors which are the petals that fell off)
image = image.resize((WIDTH, HEIGHT), Image.LANCZOS)
image.save(f"wollpaper-{seed}.png")
print("saved", f"wollpaper-{seed}.png")
      


    