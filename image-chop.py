from PIL import Image
im = Image.open("arrow2.png") #build the image object.
pix = im.load() #build the image object this has all the pixels

#Get the width and hight of the image for iterating over and make sure it's devisable by 10.
image_croped_x = (im.size[0] - (im.size[0]%10))
image_croped_y = (im.size[1] - (im.size[1]%10))

#setting some vars.

red = 0
green = 0
blue = 255
image_done = False
line_done = False
block_done = False
y_point = 0
y_count = 0
x_start = 0 
x_end   = 10
x_point = 0  
color_count = 0



while image_done == False:
	#print "Here are some stats. image_croped_x =\n image_croped_x: %d \n image_croped_y: %d\n " % (image_croped_x , image_croped_y)
	if line_done == True:
		if x_point >= image_croped_x - 10:
			print "Image is done."
			image_done == True
			break
		else:
			x_start += 10
			x_end += 10
			line_done = False
			y_point = 0
			#print "here are some stats on the image \n x_start: %d\n x_end: %d\n line_done: %r\n y_point: %d\n" % (x_start, x_end, line_done, y_point )
			
		
	else:
		print "Image is not done - State: %r" % image_done

	while line_done == False:
		if block_done == True: 
			if y_point >= image_croped_y - 10:
				print "line is Done"
				line_done = True
				break
			else:
				print color_count
				if color_count == 0:
					red = 255
					green = 0 
					blue = 0
					color_count += 1
				elif color_count == 1:
					green = 255
					red = 0
					blue = 0
					color_count += 1
				elif color_count == 2:
					blue = 255
					red = 0 
					green = 0
					color_count = 0
				
				y_count = 0
				block_done = False
				
		
		while block_done == False:
			if y_count == 9:
				print "block is done"
				block_done = True	
				break		
			for x_point in range(x_start ,x_end):
				pix[x_point,y_point] = (red, green , blue)
			if block_done == False: 
				y_point += 1
				y_count += 1
			
	
im.show()
