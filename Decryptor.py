def cipher_ophalen():
    cipher = input("geef de cipher text in: \n")
    return cipher.upper()  #returned text in upper --> later word text doorzocht op hoofdletters, om te vermijden dat sommige letters 2 keer vervangen worden


def key_ophalen():
    alfa = "abcdefghijklmnopqrstuvwxqyz"
    keys = {}
    for i in alfa:

        key = input("key van " + i + ": ")
        keys[i] = key   #zet iedere key in een dictionary

    return keys


def decryption():
    cipher = cipher_ophalen()
    key = key_ophalen()
    for i in key:
        cipher = cipher.replace(i.upper(), key[i])  #zoekt de letters op alfabetische volgorde in text + vervangt ze met key
    print(cipher)


decryption()
