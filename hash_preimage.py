import hashlib
import os
import random
import string

def hash_preimage(target_string):
    if not all( [x in '01' for x in target_string ] ):
        print( "Input should be a string of bits" )
        return
    nonce = b'\x00'

    len_k = len(target_string)
    while True:
        x = ''.join(random.sample(string.ascii_letters, 30))
        byte_x = x.encode('utf-8')
        hex_x = bin(int(hashlib.sha256(byte_x).hexdigest(), 16))

        if hex_x[-len_k:] == target_string:
            return (byte_x)
        continue

    return( nonce )
