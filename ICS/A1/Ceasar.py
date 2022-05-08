plaintext = "abcdefghijklmnopqrstuvwxyz"
f=''
a= input("Enter the string to be encrypted: ")
key = int(input("Enter key: "))

a= a.lower()
for x in a:
    if(x in plaintext):
        pos = plaintext.find(x)
        pos = (pos+key)%26
        f+= (plaintext[pos])
    else:
        f+=x
print("decrypted string is: ",f)            
