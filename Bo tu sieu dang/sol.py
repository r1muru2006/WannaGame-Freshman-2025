from Crypto.Util.number import inverse, long_to_bytes
from sage.all import crt

e = 0x10001
m1 = 2**1024 - 3
m2 = 2**1022 - 2
m3 = 2**1020 - 1
m4 = 2**1018
c = 2027792127378145444099302510462900300257442068928010403052259994880511317607407514908720534902489134379904618947792557805368190009359079320337075768626232418980864987406619809977532904702783433112202254001367719098893178820312980355187703995660867067442830169498602243151057835147454968516377852012013934653

factor_m1 = [
    13,
    107,
    87671,
    3870037838243,
    279462107025143615623321823017,
    1325706410421371952032007611396267,
]
lst_d = []
for f in factor_m1:
    d = inverse(e, f - 1)
    lst_d.append(d)

cts = []
for k in range(4):
    s2 = c + k * m4
    for j in range(4):
        s1 = s2 + j * m3
        for i in range(4):
            t = s1 + i * m2
            cts.append(t)
            
lst_k = []
for ct in cts:
    for d, f in zip(lst_d, factor_m1):
        k = pow(ct, d, f)
        lst_k.append(k)
    x = crt(lst_k, factor_m1)
    flag = long_to_bytes(x)
    lst_k.clear()
    if b'W1{' in flag:
        print(flag)
        break
