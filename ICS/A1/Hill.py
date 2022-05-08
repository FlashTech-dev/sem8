import string

letters = string.ascii_lowercase + string.ascii_uppercase + " "

size_l = len(letters)

def encrypt(pt, key):

	while(len(pt) % 2 != 0):
		pt += " "
		
	ct = ""
	
	for i in range(0, len(pt), 2):
		ct += letters[(letters.index(pt[i]) * key[0][0] + 
				letters.index(pt[i+1]) * key[0][1]) % size_l]
				
		ct += letters[(letters.index(pt[i]) * key[1][0] + 
				letters.index(pt[i+1]) * key[1][1]) % size_l]
	
	return ct
	
	
def inv(key):
	det = key[0][0] * key[1][1] - key[1][0] * key[0][1]
	
	while det < 0:
		det = det + size_l
	
	det = det % size_l
	
	new_det = 1
	while((new_det * det) % size_l != 1): 
		new_det+= 1
	
	det = new_det
	
	ikey = [[[], []], [[], []]]
	
	ikey[0][0] = ((key[1][1]) * det) % size_l
	ikey[0][1] = ((size_l - key[0][1]) * det) % size_l
	ikey[1][0] = ((size_l - key[1][0]) * det) % size_l
	ikey[1][1] = ((key[0][0]) * det) % size_l

	return ikey

def decrypt(ct, key):
	key = inv(key)

	print("inverse", key)
	
	dt = ""
	for i in range(0, len(ct), 2):	
		dt += letters[(letters.index(ct[i]) * key[0][0] + 
				letters.index(ct[i+1]) * key[0][1]) % size_l]
				
		dt += letters[(letters.index(ct[i]) * key[1][0] + 
				letters.index(ct[i+1]) * key[1][1]) % size_l]
	
	return dt

pt = input("Enter you text:")
print("Plain text:", pt)

key = [[], []]

print("Enter 2x2 matrix key for cipher: ")
key[0].append(int(input()) % size_l)
key[0].append(int(input()) % size_l)
key[1].append(int(input()) % size_l)
key[1].append(int(input()) % size_l)
print(key)

ct = encrypt(pt, key)
print("Cipher Text: ", ct)

dt = decrypt(ct, key)
print("Decrypted Text: ", dt)

