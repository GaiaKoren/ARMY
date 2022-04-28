import bencoder

from hashlib import sha1

f = open(r"C:\Users\princess\Downloads\sample.torrent", "rb")

info = bencoder.decode(f.read())

print(info)

for key in info:
    print(key)
    if key == b"info":
        for key in info[b"info"]:
            if key == b'pieces':
                print(info[b"info"][key].hex())