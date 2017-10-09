import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter

########## CONSTANTS ###############

SIZE = 25,25
POSITION_BOUNDS = 2 # max 300 
ROTATION_DEG = 90
MAX_SIZE = 25 # % change in size
THICKNESS = 5
MARKS_INDEX = 5

####################################

cards = np.zeros(5)

circle = Image.open("zener-images/circle.jpg")
plus = Image.open("zener-images/plus.jpg")
square = Image.open("zener-images/square.jpg")
star = Image.open("zener-images/star.jpg")
wavy = Image.open("zener-images/wavy.jpg")
circle.resize((250,250))
plus.resize((250,250))
square.resize((250,250))
star.resize((250,250))
wavy.resize((250,250))
images = [circle,plus,square,star,wavy]
white = Image.new('RGBA', (300,300), (255,255,255,255)) 
orig_image = []

def position(n):
	temp_image = white
	x1 =  np.random.randint(POSITION_BOUNDS)
	y1 = np.random.randint(POSITION_BOUNDS)
	x2,y2 = orig_image[n].size
	temp_image.paste(orig_image[n],(x1,y1,x2+x1,y2+y1))
	orig_image[n] = temp_image
	

def orientation(n):
	orig_image[n].rotate(np.random.randint(ROTATION_DEG))


def size(n):
	width, height = orig_image[n].size
	percentage = np.random.randint(MAX_SIZE)
	orig_image[n].crop((int(width*0.01*percentage),
		int(height*0.01*percentage),
		(width-int(width*0.01*percentage)),
		(height-int(height*0.01*percentage))))

def thickness(n):
	thick= np.random.randint(THICKNESS)
	thin = np.random.randint(THICKNESS)
	for i in range(thick):
		orig_image[n] = orig_image[n].filter(ImageFilter.BLUR)
	for i in range(thin):
		orig_image[n] = orig_image[n].filter(ImageFilter.SHARPEN)

def marks(n):
	draw = ImageDraw.Draw(orig_image[n])
	x,y = orig_image[n].size
	for i in range(np.random.randint(MARKS_INDEX)):
		offset_1 = np.random.randint(x-1)
		offset_2 = np.random.randint(y-1)
		draw.point((x,y), fill=(0,0,0))

	for i in range(np.random.randint(MARKS_INDEX)):
		x1 = np.random.randint(x-1)
		x2 = np.random.randint(x-1)
		y1 = np.random.randint(y-1)
		y2 = np.random.randint(y-1)
		draw.line((x1,y1,x2,y2), fill=(0,0,0))

	for i in range(np.random.randint(MARKS_INDEX)):
		x1 = np.random.randint(x-1)
		x2 = np.random.randint(x-1)
		y1 = np.random.randint(y-1)
		y2 = np.random.randint(y-1)
		draw.ellipse((x1,y1,x2,y2), fill=(255,255,255))




for i in range(5):
	choice = np.random.randint(4)
	image = images[choice]
	orig_image.append(image)
	no_of_transformations = np.random.randint(10)
	for j in range(no_of_transformations):
		case = np.random.randint(5)
		# if case == 0:
		# 	position(i)
		# 	print i
		if case == 1:
			orientation(i)
		# elif case == 2:
		# 	size(i)
		# elif case == 3:
		# 	thickness(i)
		# else:
		# 	marks(i)
	orig_image[i].resize((250,250))
	file_name = ''
	file_name += str(i)+'_'
	if choice == 0:
		file_name += 'O'
	elif choice == 1:
		file_name += 'P'
	elif choice == 2:
		file_name += 'Q'
	elif choice == 3:
		file_name += 'S'
	else:
		file_name += 'W'
	orig_image[i].save(file_name+'.PNG',"PNG")