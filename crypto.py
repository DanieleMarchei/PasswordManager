from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto import Random
import struct
import os

def encrypt(key, fileIn, fileOut):
    if len(key) % 16 != 0:
        padLen = len(key) % 16
        key += "0" * padLen
        
    mode = AES.MODE_CBC
    iv = Random.new().read(AES.block_size)
    cipher = AES.new(key,mode,IV = iv)
    chunksize = 64*1024
    filesize = os.path.getsize("original.txt")
    with open(fileIn, "rb") as infile:
        with open(fileOut, "wb") as outfile:
            outfile.write(struct.pack("<Q", filesize))
            outfile.write(iv)
            outfile.write(key)
            while True:
                chunk = infile.read(chunksize)
                if len(chunk) == 0:
                    break
                elif len(chunk) % 16 != 0:
                    chunk += " " * (16 - len(chunk) % 16)

                outfile.write(cipher.encrypt(chunk))

def decrypt(key, fileIn, fileOut):
    if len(key) % 16 != 0:
        padLen = len(key) % 16
        key += "0" * padLen
        
    chunksize = 24*1024
    with open(fileIn, "rb") as infile:
        originsize = struct.unpack("<Q", infile.read(struct.calcsize("Q")))[0]
        iv = infile.read(16)
        hash = infile.read(32)
        if hashstr(key) != hash:
            raise Exception("You entered the wrong key")

        key = hashstr(key)
        mode = AES.MODE_CBC
        decrypt = AES.new(key, mode, IV = iv)
        with open(fileOut, "wb") as outfile:
            while True:
                chunk = infile.read(chunksize)
                if len(chunk) == 0:
                    break

                outfile.write(decrypt.decrypt(chunk))

            outfile.truncate(originsize)

def hashstr(string):
    hash = SHA256.new()
    hash.update(string)
    return hash.digest()
