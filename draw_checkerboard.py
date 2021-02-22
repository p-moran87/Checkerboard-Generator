# drawing with PIL (Python Image Library)
# draw and save a small French flag (blue, white, red)
from PIL import Image, ImageDraw
# create a new 24x16 pixel image surface (default is black bg)
img = Image.new("RGB", (64, 64))
# set up the new image surface for drawing
draw = ImageDraw.Draw (img)

# Makes an 8 x 8 grid checkerboard
w = 8
h = 8

for j in range(0,64,8):
	for i in range(0,64,8):
		if ((j / 8) % 2 ==0 ) and ((i / 8) % 2 ==0):
			colour_type = 'white'
		elif ((j / 8) % 2 >0 ) and ((i / 8) % 2 >0):
			colour_type = 'white'

		else:
			colour_type = 'black'

		draw.polygon([(i,j),(i+w,j), (i+w,j+h), (i,j+h)], fill=colour_type)

img.save("checkerboard.png")
# optionally look at the image you have drawn
img.show()