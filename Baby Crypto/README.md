# Solution

Answer these questions one by one and put it into the challenge and we will know how it encrypts the data

1. 13 is very familiar to us because of the introduction to cryptography with the **ROT13 algorithm**
2. In this question, you could use Cyberchef tool to identify and decode the string. Then we know that it is a base85-encoded string. Therefore, the answer must be **Base85 Encoding**.
3. Finally, $1+1 = 0$ can be related to the $\mathbb{GF}(2)$ and the first thing come into our mind is **XOR function**.

When you answer all the questions, the real challenge become:
```python
import base64
import os

message = '???'
FLAG = open("flag.txt").read().encode()
assert FLAG in message

def rot13(text: bytes) -> bytes:
    return bytes(
        (c + 13 - 65) % 26 + 65 if 65 <= c <= 90 else
        (c + 13 - 97) % 26 + 97 if 97 <= c <= 122 else c
        for c in text
    )
    
def base85encode(text: bytes) -> bytes:
    return base64.b85encode(text)

def xor(a: bytes, b: bytes) -> bytes:
    return bytes(x ^ y for x, y in zip(a, b))

enc = rot13(message.encode())
weird = base85encode(enc)
key1, key2, key3 = [os.urandom(len(weird)) for _ in range(3)]

ct1 = xor(weird, key1)
ct2 = xor(key1, key2)
ct3 = xor(key2, key3)

with open("output.txt", "w") as o:
    o.write(f'ct1: {ct1.hex()}\nct2: {ct2.hex()}\nct3: {ct3.hex()}\n')
    # I will give you a chance with my last key :D
    o.write(f'key3: {key3.hex()}')
```

After that, we reverse through each algorithm and decode the ciphertext. This give us a long message and I believe that you're not blind to find the hidden flag in it :3.
Here is my [script](./solution.py)

    Flag: W1{D1d_y0U_GeT_r1Ck_r0lL3d?}