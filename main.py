from fastapi import  FastAPI , HTTPException
import uvicorn
from caeser.Caesar import Caesar
from caeser.encript_caesar import encript_caeser
from fence.Fence import Fence
from fence.encrption import *





app = FastAPI()


@app.get("/")
def root():

    return "Hello"


@app.get("/test")
def root():

    return {"msg":"hi from test"}


@app.get("/test/{name}")
def root(name):

    with open("names.txt","a") as f:
        f.writelines(f"{name} \n")

    return {"msg":"saved user"}


@app.post("/caesar")
def caesar_post(caesar:Caesar):
    print("in f")
    text = encript_caeser(caesar.text,caesar.offset)

    if caesar.mode == "encrypt":
        text = encript_caeser(caesar.text, caesar.offset)
        return {"encrypted_text": text}

    elif caesar.mode == "decrypt":
        text = encript_caeser(caesar.text, caesar.offset * -1)
        return {"decrypted_text": text}

    else:
        raise HTTPException(status_code=400, detail="We can only 'encrypt' and 'decrypt'")


@app.get("/fence/encrypt")
def fence_encrypt(text:str):

    text = encription_fence(text)

    return { "encrypted_text": text }


@app.post("/fence/decrypt")
def fence_decrypt(fence:Fence):

    text = decrypt_fence(fence.text)
    return {"decrypted": text}



































