

def encription_fence(text):

    text = text.replace(" ","")
    text1 = ""
    text2 = ""

    for i,c in enumerate(text):

        if i % 2 == 0:
            text1 += c
        else:
            text2 += c

    return text1+text2


def decrypt_fence(text):

    if len(text) % 2 == 1:
        text1 = text[0:(len(text)//2)+1]
        text2 = text[(len(text)//2)+1:]
    else:
        text1 = text[0:(len(text) // 2)]
        text2 = text[(len(text) // 2):]

    new_text = ""

    for i in range(len(text2)):

        try:
            new_text += text1[i]
        except:
            pass

        new_text += text2[i]


    return new_text




