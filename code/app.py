
'''
 program to demonstrated the Adi Shamir's Visual Secret Sharing
'''

# libraries used

from PIL import Image
from numpy import *
import math


# global variables
total_Shares = 4
threshold = 3
list_of_cofficient = [3,5,7,11,13,17,19,23]

# change image to matrix
def  changeImageToMatrix(imagename):
	img = Image.open(imagename) # opens image
	image_as_array = array(img) # converts into numpy array
	return image_as_array


# Encryption
def encryption(pixel):
	epixels = list() # for storeing encrypted images

	for i in range(total_Shares):
		temp  = pixel
		for j in range(1,threshold):
			temp = temp + list_of_cofficient[j-1] * int(math.pow(i+1,j))

		epixels.append(temp % 256)
	return epixels


# Decryption
def decryption(epixel):
	dpixel = 0
	for i in range(1,threshold+1):
		li = 1
		for j in range(1,threshold+1):
			if i != j:
				li = li * (-j/(i-j))
		dpixel = dpixel + epixel[i-1] * li
	return dpixel





def main():
	image = changeImageToMatrix('test.jpg')
	image = list(image)
	encrypted_images = list()
	for b in range(total_Shares):
		encrypted_images.append(image)
	encrypted_images = array(encrypted_images)
	# for encrypting the image and store all shares in one list
	for i in range(len(image)):
		for j in range(len(image[i])):
			for k in range(len(image[i][j])):
				encrypt = encryption(image[i][j][k])
				# print(encrypt)
				for b in range(total_Shares):
					encrypted_images[b][i][j][k] = encrypt[b]
					

					
	
	for b in range(total_Shares):
		encrypted_images[b] =array(encrypted_images[b])
		Image.fromarray(encrypted_images[b],'RGB').show()

	# for decrypting the image and show
	decrypted_image = array(image)
	for i in range(len(image)):
		for j in range(len(image[i])):
			for k in range(len(image[i][j])):
				row = []
				for b in range(threshold):
					row.append(encrypted_images[b][i][j][k])
				colorpixel = decryption(row)
			decrypted_image[i][j][k] = colorpixel

	Image.fromarray(decrypted_image,'RGB').show()

	print(image)
	print("_________________________")
	print(encrypted_images[0])
	# print("_________________________")
	# print(encrypted_images[1])
	# print("_________________________")
	# print(encrypted_images[2])

	# print("_________________________")
	# print(decrypted_image)


if __name__ == "__main__":
	main()


