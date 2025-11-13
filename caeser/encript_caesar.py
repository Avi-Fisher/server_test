
def encript_caeser(text, key):
    text = text
    cipher = ""
    for letter in text:
        shifted = ord(letter) + key
        if letter == " ":
            cipher += letter
            continue
        if shifted < 97:
            shifted += 26
        if shifted > 122:
            shifted -= 26
        cipher += chr(shifted)
    return cipher
