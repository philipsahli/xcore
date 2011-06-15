

from PIL import Image, ImageChops, ImageDraw,\
    ImageFilter, ImageFont, ImageColor
from cStringIO import StringIO
import os


def get_label(text="TEXT", text_color="white", text_size=22):

    mpath = os.path.dirname(os.path.abspath(__file__))

    font = ImageFont.truetype(os.path.join(mpath, "font/Futura_BoldBT.ttf"), text_size)
    #font = ImageFont.truetype(mpath+"/font/Futura_Extra_BlackBT.ttf", 22)
    #font = ImageFont.load(mpath+"/pilfonts/timR24.pil")

    output = StringIO()

    im = Image.new("RGB", (500, 100), (0, 0, 0))
    alpha = Image.new("L", im.size, "black")
    imtext = Image.new("L", im.size, 0)
    drtext = ImageDraw.Draw(imtext)
    drtext.text((1,1), text, font=font, fill=tohex((inverted(text_color))))
    w, h = drtext.textsize(text, font=font)
    alpha = ImageChops.lighter(alpha, imtext)
    solidcolor = Image.new("RGBA", im.size, text_color)
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

def inverted(color):
    rgb = ImageColor.getrgb(color)
    inv=255
    return (inv-rgb[0], inv-rgb[1], inv-rgb[2])

def tohex(rgb):
    print rgb
    # from http://blog.affien.com/archives/2004/12/20/rgb-to-hex-and-why-the-python-interactive-mode-is-so-damned-handy/
    return "#%02X%02X%02X" % (rgb[0], rgb[1], rgb[2])

