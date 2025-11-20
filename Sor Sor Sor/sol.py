import string

def xor(a, b):
    return bytes(x ^ y for x, y in zip(a, b))

pr = string.printable
ct = bytes.fromhex('2f01090a6f042b4447101f0047460d6e0e5d001100422d156443022c4a3e074a392b033e531d1b47401b44423c411e08')
blocks = [ct[i:i+3] for i in range(0, len(ct), 3)]
l = len(blocks)
flag = []

temp = b'W1{'
flag.append(temp)
see = []
while True:
    for i in range(len(blocks)):
        res = xor(temp, blocks[i])
        if all(chr(res[j]) in pr for j in range(len(res))):
            see.append((res, i))
    print("Can see: ", see)
    temp = input('Enter choice: ').encode()
    for pair in see:
        if(pair[0] == temp):
            blocks.pop(pair[1])
    flag.append(temp)
    if len(flag) == l:
        print(flag)
        break
    see.clear()

