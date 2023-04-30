

import base64
import os
import time

#inspired by my brain thinking about it when i think how to decode faster without open your browser.
B = '\033[30m'
R = '\033[31m'
G = '\033[32m'
Y = '\033[33m'
b = '\033[34m'
M = '\033[35m'
Cy = '\033[36m'
W = '\033[37m'
R = '\033[39m'

banner='''

	     \033[34m乇几匚ㄖᗪ乇尺　ㄒ乇乂ㄒ\033[39m

        \033[31m[+]\033[33m https://github.com/Mika259 \033[31m[+]\033[36m	
	--------->> version 1.5 <<--------\033[39m
'''
menu ='''\033[32m
[+] Menu_option (select)
 |_
 | [1] \033[34mhex\033[32m
 |_
 | [2] \033[34mbase64\033[32m
 |_
 | [3] \033[34mhash\033[32m
 |_
   [4] \033[34mrot13\033[32m

'''
os.system('clear')

#loading animate
import time

def loading_animation(duration):
    animation = "|/-\\"
    idx = 0
    start_time = time.time()
    while time.time() - start_time < duration:
        print("\033[34mLoading " + animation[idx % len(animation)], end="\r")
        idx += 1
        time.sleep(0.1)

loading_animation(1.5)
print("\033[33m-- Welcome User --")

time.sleep(0.5)
print(banner)
print(menu)
user = input("\033[33mselect >> \033[39m")

def plan():
        if user == '1':
            hexOp()
        elif user == '2':
           base64Op()
        elif user == '3':
           hash()
        elif user == '4':
            rot13()
        else:
            print("\033[31mError Command!\033[39m")

def back():
	print(menu)
	user = input("\033[33mselect >> \033[39m")
	plan()

def home():
	inpusr = input("\033[34m\nEncode and Decode again (y/n) \033[39m")
	if inpusr == 'y':
	        back()
	elif inpusr == 'n':
	        print("\033[34mThanks For Using Me :)\033[39m")
	        exit()
	else:
	        exit()

def hex():
	# Text string to convert
	text_string = input("\ntext to hex :")
	# Convert the string to hexadecimal
	hex_string = text_string.encode('utf-8').hex()
	# Print the hexadecimal string
	print(f"hex :\n{hex_string}");home()

def unhex():
	# Hexadecimal string to convert
	hex_string = input("\nhex to text :")
	# Convert the hexadecimal string to plain text
	plain_text = bytes.fromhex(hex_string).decode('utf-8')
	# Print the plain text string
	print(f"text :\n{plain_text}");home()

def hexOp():
	usrOp1 = input("[1] Text to Hex / [2] Hex to Text : ")
	if usrOp1 == '1':
		hex()
	elif usrOp1 == '2':
		unhex()

def base64():
	import base64
	# Plain text string to encode
	plain_text = input("\nText to Base64 :")
	# Encode the string
	encoded_string = base64.b64encode(plain_text.encode('utf-8'))
	# Print the encoded string
	print(encoded_string.decode('utf-8'));home()

def unbase64():
	import base64
	# Base64-encoded string to decode
	encoded_string = input("\nBase64 to Text :")
	# Decode the string
	decoded_string = base64.b64decode(encoded_string)
	# Print the decoded string
	print(decoded_string.decode('utf-8'));home()

def base64Op():
	usrOp2 = input("[1] Text to Base64 / [2] Base64 to Text : ")
	if usrOp2 == '1':
		base64()
	elif usrOp2 == '2':
		unbase64()

def hash():
	import hashlib
	print("\033[31mYou cannot decode hash back to the first text anymore!\033[39m\n")
	# Plain text string to hash
	plain_text = input("Text to Hash :")
	# Hash the string using SHA-256 algorithm
	hashed_text = hashlib.sha256(plain_text.encode('utf-8')).hexdigest()
	# Print the hashed string
	print(f"Hashed :\n{hashed_text}");home()

def enRot13():
	# define the ROT13 alphabet mapping
	rot13_mapping = str.maketrans(
	    "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz",
	    "NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm"
	)
	# get the input string from the user
	input_string = input("\nEnter string to encrypt :")
	# encrypt the string using ROT13
	encrypted_string = input_string.translate(rot13_mapping)
	# display the encrypted string
	print("Encrypted string :\n", encrypted_string);home()

def deRot13():
    # define the ROT13 alphabet mapping
    rot13_mapping = str.maketrans(
    "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz",
    "NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm"
    )
    # get the input string from the user
    encrypted_string = input("\nEnter ROT13-encrypted string :")
    # decrypt the string using ROT13
    decrypted_string = encrypted_string.translate(rot13_mapping)
    # display the decrypted string
    print("Decrypted string :\n", decrypted_string);home()


def rot13():
    usrOp3 = input("[1] Encrypt into rot13 / [2] Decrypt into Text : ")
    if usrOp3 == '1':
        enRot13()
    elif usrOp3 == '2':
        deRot13()

plan()


#tool by mika259
#repory if have some bugs or problems
