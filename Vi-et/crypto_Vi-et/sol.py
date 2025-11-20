from sympy import symbols, Eq, solve
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import hashlib

a, b, c = symbols('a b c')

eq1 = Eq(a * b * c, 15864378984956659850534060107405422568891641699308509134070157505662198692417476378386001170963905568690006431674713)
eq2 = Eq(a + b + c, 779122598205443694565344617967399722167)
eq3 = Eq(a*b + b*c + c*a, 196487786916397904192643381759626074607590751745631772329891131596526673844879)

solution = solve((eq1, eq2, eq3))
for sol in solution:
    a1, b1, c1 = sol[a], sol[b], sol[c]
    print(f'W1{{{123*a1  + 456*b1 + 789*c1}}}')