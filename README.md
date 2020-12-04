# mac-algo
MAC stands for Message Authentication Code
MAC is used for verifying the authenticity of a message, with the help of this the authenticity of a transferred message is verified.

The message is appended with that of cipher text and then sent along with the message.
At the time of verification the key and encrypted data is checked by the help of MAC. As the message is attached to the cipher text also, by decryting the cipher and comparing it to the actual message it can be determined if the message has been altered or not.

# important
for this demo, the cipher technique used is Caesar cipher, any cipher can be used with it, by just replacing the import file and taking in care the encrypt and decrypt function.
