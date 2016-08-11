from PIL import Image
im = Image.open("arrow.jpeg") #build the image object.
pix = im.load() #build the image object this has all the pixels

image_croped_x = (im.size[0] - (im.size[0]%10))
image_croped_y = (im.size[1] - (im.size[1]%10))

red,green,blue = 0,0,255
image_done = line_done = block_done = False
y_point = y_count = x_start = x_point = color_count = 0  
x_end = 10

while not image_done:
	if line_done:
		if x_point >= image_croped_x - 10:
			print "Image is done."
			image_done == True
			break
		else:
			x_start += 10
			x_end += 10
			line_done = y_point = 0
	else:
		print "Image is not done - State: %r" % image_done

	while not line_done:
		if block_done: 
			if y_point >= image_croped_y - 10: 
				print "line is Done"
				line_done = True
				break
			else:
				print color_count
				if color_count == 0:
					red,green,blue = 255,0,0
					color_count += 1
				elif color_count == 1:
					green,red,blue = 255,0,0
					color_count += 1
				elif color_count == 2:
					blue,red,green,color_count = 255,0,0,0
				y_count = 0
				block_done = False
		while not block_done:
			if y_count == 9:
				print "block is done"
				block_done = True    
				break        
			for x_point in range(x_start ,x_end):
				pix[x_point,y_point] = (red, green , blue)
			if not block_done: 
				y_point += 1
				y_count += 1    
im.show()
