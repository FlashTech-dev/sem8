p= int(input("Enter prime no 1: "))
q= int(input("Enter prime no 2: "))
a= int(input("Enter private key for A :"))
b= int(input("Enter private key for B :"))

A= (q**a)%p
B= (q**b)%p

S_A=(B**a)%p
S_B=(A**b)%p
if(S_A==S_B):
    print("they can communicate with private key: ", S_A)
else:
    print("They cannot communicate")    