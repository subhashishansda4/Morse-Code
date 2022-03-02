# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 20:28:12 2022

@author: VAGUE
"""

from morse_codes import codes

# extracting each character from a word and matching it with its corresponding morse code
# adding 1 space between every character and '/' between every word
def encrypt(message):
    cipher = ''
    for letter in message:
        if letter != ' ':
            cipher += codes[letter] + ' '
        else:
            cipher += '/ '
    return cipher

# extracting characters from the given string till a space
# adding corresponding english alphabets to a variable that will store the result
# after getting two spaces, we will add space to our variable containing the decoded string
def decrypt(message):
    message += ' '
    decipher = ''
    citext = ''
    for letter in message:
        if letter != ' ':
            i = 0
            citext += letter
        else:
            i += 1
            if i == 2:
                decipher += ' '
            else:
                decipher += list(codes.keys())[list(codes.values()).index(citext)]
                citext = ''
                
    return decipher

# temporary message for encryption and decryption
def main():
    message = "Decision defines Destiny"
    result = encrypt(message.upper())
    print(result)
    
    message = "-.. . -.-. .. ... .. --- -. / -.. . ..-. .. -. . ... / -.. . ... - .. -. -.-- "
    result = decrypt(message)
    print(result)
    
if __name__ == "__main__":
    main()