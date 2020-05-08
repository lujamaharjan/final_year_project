
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

		epixels.append(temp)
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
	e = encryption(27)
	print(e)
	z = decryption(e)
	print(z)
	
	
if __name__ == "__main__":
	main()


