#base16 conversion.
import base64

#determine whether user wants to convert from base16 to base64 or vice versa
question = input('Do you want to decode Base16 string to Base64? (y/n): ')

#take the string input
input1 = input('Please input the string data: ')

#based on the answer choice, run code from the statement below.
if question == 'y':
	#decodes a base16 string to base64
	option3 = base64.b16decode(input1)
	return option3
else:
	#encode a string from base64 to base16
	option2 = base64.b16encode(input1)
	return option2




