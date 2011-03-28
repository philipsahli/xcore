

from PIL import Image, ImageChops, ImageDraw,\
    ImageFilter, ImageFont
from cStringIO import StringIO
import os


def get_label(text="gugus"):

    mpath = os.path.dirname(os.path.abspath(__file__))

    # TODO: Font family and size as arg
    font = ImageFont.truetype(mpath+"/font/Futura_BoldBT.ttf", 22)
    #font = ImageFont.truetype(mpath+"/font/Futura_Extra_BlackBT.ttf", 22)
    #font = ImageFont.load(mpath+"/pilfonts/timR24.pil")

    output = StringIO()

    im = Image.new("RGB", (500, 100), (0, 0, 0))
    alpha = Image.new("L", im.size, "black")
    imtext = Image.new("L", im.size, 0)
    drtext = ImageDraw.Draw(imtext)
    drtext.text((1,1), text, font=font, fill="white")
    w, h = drtext.textsize(text, font=font)
    alpha = ImageChops.lighter(alpha, imtext)
    solidcolor = Image.new("RGBA", im.size, "#ffffff")
    immask = Image.eval(imtext, lambda p: 255 * (int(p != 0)))
    im = Image.composite(solidcolor, im, immask)
    im.putalpha(alpha)
    im.filter(ImageFilter.SMOOTH_MORE)

    shadowc = im.crop((0, 0, w+3, h+3))
    shadowc.load()

    blur_f = 10
    count = 0

    while count < blur_f:
        shadowc.filter(ImageFilter.SMOOTH)
        count+=1
    
    shadowc.save(output, "PNG")
    
    return output
