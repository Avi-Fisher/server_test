from fastapi import  FastAPI , HTTPException
import uvicorn
import pydantic
from caeser.Caesar import Caesar
from caeser.encript_caesar import encript_caeser
from fence.Fence import Fence





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
        f.writelines(name)

    return name

@app.post("/caesar/")
def caesar_post(caesar:Caesar):
    text = encript_caeser(caesar.text,caesar.offset)

    if caesar.mode == "encrypt":
        return { "encrypted_text": text }

    elif caesar.mode == "decrypt":
        return {"decrypted_text": text}

    else:
        raise HTTPException(status_code=400, detail="We can only 'encrypt' and 'decrypt'")


@app.get("/fence/encrypt/{text}")
def fence_encrypt(text:str):

    return { "encrypted_text": text }





@app.post("/fence/decrypt")
def fence_decrypt(fence:Fence):

    return {"decrypted": "..."}



































