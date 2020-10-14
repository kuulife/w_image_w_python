from PIL import Image
#first picture
mask = Image.open('mask.png')
#secong picture
matrix = Image.open('word_matrix.png')

#check the size of images
print('mask.png size is: {}'.format(mask.size))
print('word_matrix.png size is: {}'.format(matrix.size))

#resizing mask.png bcs its smaller than matrix image
mask = mask.resize((1015,559))

#adding transparency to the image
#max transparency is 0 and min is 255
mask.putalpha(220)

#pasting mask image to the matrix image
matrix.paste(mask,(0,0),mask)
#open image and show the result
matrix.show()
