def gcd(a, b):
      if b == 0:
         return a
      else:
        return gcd(b, a % b)

plaintext = input("Enter plain text: ")
p = int(input("Enter value of p: "))
q = int(input("Enter value of q: "))

n = p*q
t = (p-1)*(q-1)

for e in range(2, t):
  if gcd(e, t) == 1:
    break
print("Public key of sender e: ", e)

for d in range(1, t):
  if e*d % t == 1:
    break
print("Private key of receiver d: ", d)

l = []
dencryptedtext = ""
for i in plaintext:
  x = pow(ord(i), e)
  y = x % n
  l.append(y)

for j in range(len(l)):
  x = pow(l[j], d)
  y = x % n
  dencryptedtext += chr(y)

print("Plaintext: ", plaintext)
print("Encrypted text", l)
print("Decrypted text: ", dencryptedtext)