# Solution

From `chall.py`, we know the result after using XOR of original flag and shuffle flag with 3-char blocks.

The flag format is 'W1{...}', so we know a block is 'W1{'.

From that, I write a script that can give us the printable result of each block when xor-ing with block we know.

Then we choose the best and get the list of blocks which can combine into flag.

Here is my [script](./sol.py) and this is my choice:
```
Can see:  [(b'x0r', 0), (b'|u<', 2), (b'G.{', 3), (b'9?&', 5), (b'W {', 6), (b'3ry', 8), (b'{{E', 9), (b'P{B', 10), (b'|2E', 11)]
Enter choice: x0r
Can see:  [(b'r_v', 0), (b'St5', 1), (b'h/r', 2), (b'x!r', 5), (b'TzL', 8), (b'S3L', 10), (b'+-i', 11), (b'?pi', 12), (b'<rN', 13), (b'9.z', 14)]
Enter choice: r_v
Can see:  [(b'b@v', 1), (b'rNv', 4), (b'0rc', 5), (b'Y\\H', 9), (b'!Bm', 10), (b'3A~', 13)]
Enter choice: 0rc
Can see:  [(b' mc', 1), (b'w4n', 2), (b'^|>', 3), (b'0cc', 4), (b'T1a', 5), (b'78Z', 7), (b'cox', 9), (b'w2x', 10), (b't0_', 11), (b'qlk', 12)]
Enter choice: t0_
Can see:  [(b'd/_', 1), (b'3vR', 2), (b't!_', 4), (b'Xza', 6), (b'szf', 7), (b'_3a', 8), (b"'-D", 9), (b'3pD', 10), (b'5.W', 11)]
Enter choice: _3a
Can see:  [(b'tw&', 0), (b'O,a', 1), (b'1=<', 3), (b'_"a', 4), (b';pc', 5), (b'sy_', 6), (b'XyX', 7), (b'\x0c.z', 8)]
Enter choice: sy_
Can see:  [(b'cf_', 1), (b'4?R', 2), (b'sh_', 4), (b't3f', 6), (b' dD', 7), (b'49D', 8), (b'2gW', 9)]
Enter choice: t3f
Can see:  [(b'_w!', 0), (b'd,f', 1), (b'3uk', 2), (b't"f', 4), (b"'.}", 6), (b'3s}', 7), (b'5-n', 8)]
Enter choice: 3s}
Can see:  [(b'#l}', 1), (b't5p', 2), (b']} ', 3), (b'3b}', 4), (b'`nf', 6), (b'rmu', 7)]
Enter choice: rmu
Can see:  [(b'Y)2', 0), (b'bru', 1), (b'5+x', 2), (b'r|u', 4), (b'!pn', 6)]
Enter choice: bru
Can see:  [(b'I62', 0), (b'%4x', 1), (b'\x0c|(', 2), (b'bcu', 3), (b'1on', 5)]
Enter choice: 1on
Can see:  [(b'v)c', 1), (b'_a3', 2), (b'1~n', 3), (b'U,l', 4)]
Enter choice: _a3
Can see:  [(b't%t', 0), (b'_p3', 2), (b';"1', 3)]
Enter choice: _p3
Can see:  [(b't4t', 0), (b';31', 2)]
Enter choice: t4t
Can see:  [(b'3ry', 0)]
Enter choice: 3ry
[b'W1{', b'x0r', b'r_v', b'0rc', b't0_', b'_3a', b'sy_', b't3f', b'3s}', b'rmu', b'bru', b'1on', b'_a3', b'_p3', b't4t', b'3ry']
```

    Flag: W1{x0r_p3rmut4t1on_a3r_v3ry_3asy_t0_brut3f0rc3s}
