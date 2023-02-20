#Lab exercise (Brute-forcing Caesar cipher encryption)
#Amir Shahir bin Roslan <-Single gang poggers omegalul

#This Caesar encryption brute-force program algorithm is quite straightforward. First, encrypt the ciphertext then decrypt it by looping the shift 26 times (length of alphabet)
#Why alphabet? Because the ciphertext only contains alphabet character only.

#caesar encryption function
def encrypt(text,s):
	enc_output = ""

	for char in text:
		if char.isalpha():
			char_code = ord(char)
			if char.isupper():
				enc_output += chr((char_code + s - 65) % 26 + 65)
			else:
				enc_output += chr((char_code + s - 97) % 26 + 97)
		elif char.isnumeric():
			enc_output += str((int(char) + s) % 10)
		else:
			enc_output += char
	return enc_output

#caesar decryption function
def decrypt(text, i):
	dec_output = ""
	
	for char in text:

			if char.isupper(): 

				c_index = ord(char) - ord('A')
				#shift the current character to left by key positions to get its original position
				c_og_pos = (c_index - i) % 26 + ord('A')
				c_og = chr(c_og_pos)
				dec_output += c_og
			elif char.islower(): 
				c_index = ord(char) - ord('a') 
				c_og_pos = (c_index - i) % 26 + ord('a')
				c_og = chr(c_og_pos)
				dec_output += c_og
			elif char.isdigit():
				#If number,shift its actual value (minus instead of addition)
				c_og = (int(char) - i) % 10
				dec_output += str(c_og)
			else:
				#No changes? leave it
				dec_output += char

	return dec_output
#main program for this script

print("+++++++++++++++++++++++++++++++++")
print("Caesar Cipher encryptor/decryptor")
print("+++++++++++++++++++++++++++++++++")
print("")
print("1 - Encrypt cipher")
print("2 - Decrypt cipher")
print("")
i_select = int(input("Enter your selection: "))

#encrypts input text based on the shift specified
if i_select == 1:
	print("")
	i_plaintext = input("Type the words/sentences you want to encrypt: ")
	print("")
	i_shift = int(input("How many shift(s)?: "))
	print("")
	print("Your encrypted word are: "+encrypt(i_plaintext,i_shift))
	print("")

#outputs all 26 shift results.
elif i_select  == 2:
	print("")
	i_ciphertext = input("Type the words/sentences you want to decrypt (This will bruteforce all possible shifts): ")
	print("")
	for i in range(26):
		print("Shift "+str(i)+" : "+decrypt(i_ciphertext, i))
else:
	print("")
	print("Wrong choice, boi! Run it again lol :D")



