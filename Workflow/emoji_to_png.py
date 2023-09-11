#!/usr/bin/python3

import os
import sys
from PIL import Image, ImageDraw, ImageFont

glyph = os.getenv("glyph")
output = os.getenv("output")

back_ground_color = (50, 50, 50, 0)
width, height = 160,160
im = Image.new("RGBA", (width, height), back_ground_color)
draw = ImageDraw.Draw(im)

draw.text((width/2, height/2+25), glyph, font=ImageFont.truetype('/System/Library/Fonts/Apple Color Emoji.ttc', 160), anchor="mm", embedded_color=True)

im.save(output, 'PNG')