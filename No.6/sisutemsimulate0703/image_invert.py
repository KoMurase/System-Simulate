from PIL import Image, ImageOps

im = Image.open('2019-07-06.png').convert('RGB')
im_invert = ImageOps.invert(im)
im_invert.save('2019-07-06_invert.png')
