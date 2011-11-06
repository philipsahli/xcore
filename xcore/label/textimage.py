from PIL import Image, ImageChops, ImageDraw,\
    ImageFilter, ImageFont, ImageColor
from cStringIO import StringIO
from django.conf import settings
import fnmatch
import os

path_list = getattr(settings, 'XCORE_FONTS_DIR', [])
path_list.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), "font"))
fonts = {}

for path in path_list:
    for root, dirnames, filenames in os.walk(path):
        for file in filenames:
            if file.endswith('.ttf') or file.endswith('.otf'):
                name = file.replace(".ttf", "")
                name = name.replace(".otf", "")
                fonts[name] = os.path.join(root, file)

def get_label(text="TEXT", text_color="white", text_size=22, text_font="GeosansLight"):

    try:
        font = ImageFont.truetype(fonts.get(text_font), text_size)
    except Exception, e:
        raise e

    if not font:
        raise Exception("No font found for %s" % text_font)
    output = StringIO()

    # based on http://nedbatchelder.com/blog/200801/truly_transparent_text_with_pil.html

    im = Image.new("RGB", (500, 100), (0, 0, 0))
    alpha = Image.new("L", im.size, "black")
    
    imtext = Image.new("L", im.size, 0)
    drtext = ImageDraw.Draw(imtext)

    # darken() included for fix lighter color
    drtext.text((1,1), text, font=font, fill=tohex(darken((inverted(text_color)))))
    w, h = drtext.textsize(text, font=font)

    # get the ligther out of image
    alpha = ImageChops.lighter(alpha, imtext)

    # solidcolor part
    solidcolor = Image.new("RGBA", im.size, text_color)

    # to receive nice borders
    immask = Image.eval(imtext, lambda p: 255 * (int(p != 0)))
    im = Image.composite(solidcolor, im, immask)
    im.putalpha(alpha)
    im.filter(ImageFilter.SMOOTH_MORE)

    shadowc = im.crop((0, 0, w+3, h+3))
    shadowc.load()

    blur_f = 10
    count = 0

    while count < blur_f:
        shadowc.filter(ImageFilter.BLUR)
        count+=1
    
    shadowc.save(output, "PNG")
    return output

def inverted(color):
    rgb = ImageColor.getrgb(color)
    inv=255
    return inv-rgb[0], inv-rgb[1], inv-rgb[2]

def tohex(rgb):
    # from http://blog.affien.com/archives/2004/12/20/rgb-to-hex-and-why-the-python-interactive-mode-is-so-damned-handy/
    return "#%02X%02X%02X" % (rgb[0], rgb[1], rgb[2])

def darken(rgb, darken_factor=0.2, rgb_darker=[]):
    for v in rgb:
        v = v / darken_factor
        if (v>255):
           v=255
        rgb_darker.append(v)
    return rgb_darker

