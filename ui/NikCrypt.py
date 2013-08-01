__author__ = 'user'


import bz2
import base64
from simplecrypt import

def nikEncrypt(text):
    textCrypt=base64.b16encode(text.encode('utf8'))
    textCrypt=bz2.compress(textCrypt)
    textCrypt=base64.b32encode(textCrypt)
    textCrypt=encrypt('SuDoKu',textCrypt)
    textCrypt = base64.b64encode(textCrypt).decode('utf8')
    return textCrypt

def nikDecrypt(text):
    textDecrypt=base64.b64decode(text)
    textDecrypt=decrypt('SuDoKu',textDecrypt)
    textDecrypt=base64.b32decode(textDecrypt)
    textDecrypt=bz2.decompress(textDecrypt)
    textDecrypt=base64.b16decode(textDecrypt).decode('utf8')
    return textDecrypt

