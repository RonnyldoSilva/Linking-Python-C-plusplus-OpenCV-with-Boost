import cv2
import numpy as np
import base64
import myModule

def base64_To_Numpy(jpg_as_text):
	encoded_data = jpg_as_text
	nparr = np.fromstring(encoded_data.decode('base64'), np.uint8)
	img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

	return img

if __name__ == '__main__' :

	# Read image
	img = cv2.imread("red_eyes.jpg", cv2.IMREAD_COLOR)
	
	# Image to Base64
	retval, buf = cv2.imencode('.jpg', img)
	jpg_as_text = base64.b64encode(buf)

	# Call c++ function from Module
	jpg_as_text = myModule.color2gray(jpg_as_text)	
	
	jpg_original = base64_To_Numpy(jpg_as_text)

	cv2.imshow('Red Eyes', jpg_original)
	cv2.waitKey(0)
