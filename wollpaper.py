import math
import random
import sys
from PIL import Image, ImageDraw

WIDTH , HEIGHT = 2500 , 1400

seed = int(sys.argv[1]) if len(sys.argv) > 1 else random.randrange(1000)
hue = rng.randrange(360)
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
    