#caesar cipher code

def encrypt(p,k):
    plain_text=p
    key=k
    list_of_values=[]
    final=""
    for i in range(0,len(plain_text)):
        cval=ord(plain_text[i])
        cno=cval+key
        if plain_text[i].islower():
            if cno>122:
                cno=(cno % 122)+96
            list_of_values.append(chr(cno))
        elif plain_text[i].isupper():
            if cno>90:
                cno=(cno % 90)+64
            list_of_values.append(chr(cno))
        elif plain_text[i].isspace():
            list_of_values.append(chr(cval))
        else:
            list_of_values.append(chr(cno))

    for i in list_of_values:
        final+=i
    print("Cipher-Text:",final)
    return final

def decrypt(c,k):
    cipher_text=c
    key=k
    list_of_values=[]
    final=""
    for i in range(0,len(cipher_text)):
        cval=ord(cipher_text[i])
        cno=cval-key
        if cipher_text[i].islower():
            if cno<=96:
                cno=(cno)+26
            list_of_values.append(chr(cno))
        elif cipher_text[i].isupper():
            if cno<=64:
                cno=(cno)+26
            list_of_values.append(chr(cno))
        elif cipher_text[i].isspace():
            list_of_values.append(chr(cval))
        else:
            list_of_values.append(chr(cno))

    for i in list_of_values:
        final+=i
    print("Plain-Text:",final)

    return final
