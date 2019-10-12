#!/usr/bin/python
from gimpfu import register, PF_IMAGE, PF_DRAWABLE, PF_STRING, PF_OPTION, main,gimp

def encodeColor(data):
	# Shift and mask the bits to transform three 8-bit values into one 16 bit
	return str((ord(data[0]) << 8) & 0xf800 | (ord(data[1]) << 3) & 0x07e0 | (ord(data[2]) >> 3))

def export565array(timg, tdrawable, filename):
	pr =tdrawable.get_pixel_rgn(0, 0, timg.width,timg.height, False, False);
	i=0
	j=0
	size = timg.width*timg.height
	# Header comment
	output = "# Python code Exported from Gimp\n\n\n\n" 
	output += "\"data\": [" 
	while (j<timg.height-1):
		while (i<timg.width-1):
			output += encodeColor(pr[i,j]) + ", "
			i+=1
		output += encodeColor(pr[i,j]) #the last column, no comma
		output += ",\n" #end of each row
		j+=1
		i=0
	while (i<timg.width-1): #the last row, no comma
		output += encodeColor(pr[i,j]) + ","
		i+=1
	output += encodeColor(pr[i,j]) #the last column, no comma
	output += "\n]"
	savefile = open(filename,"w")
	savefile.write(output)
	savefile.close() 


register(
		"export565array",
		"Saves image data to Python dict in RGB565 format",
		"For use with AWTRIX API",
		"rince$pozor,ch"
        "Based on exportC.py by David Muriuki Karibe",
		"Rince 2019",
		"2019",
		"Export 565 Array",
		"RGB*, GRAY*, INDEXED*",
		[
		(PF_IMAGE, "timg", "Input image", None),
		(PF_DRAWABLE, "tdrawable", "Input drawable", None),
		(PF_STRING,"filename","file to save code to","untitled.c"),
		],
		[],#no return params from the plugin function
		export565array, menu="<Image>/File/Export/")

main()
