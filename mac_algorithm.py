#Message Authentication Code

import caesar

sent_message=''
key=0
def sender():
    global key
    global sent_message
    plain_text=input("Enter the plain-text:")
    key=int(input("Enter the key:"))
    final=Caesar.encrypt(plain_text,key)
    sent_message=plain_text+'xx'+final
    print("Sent message:",sent_message)

def reciever():
    lis=sent_message.split('xx')
    plain_tex=lis[0]
    cipher_tex=lis[1]
    print("Recieved Message:",sent_message)
    dec=Caesar.decrypt(cipher_tex,key)
    print("Decrypted message:",dec)
    if plain_tex==dec:
        print("Successfull")
    else:
        print("Message changed!")

while True:
    print("\nMAC code transmission")
    choice=int(input("1. Send \n2. Recieve \n3. Exit \nEnter your choice:"))
    if choice==1:
        sender()
    elif choice==2:
        reciever()
    elif choice==3:
        exit()
    
