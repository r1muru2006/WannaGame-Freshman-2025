# Solution


We have: $\phi=(p-1)*(q-1)=n-p-q+1=n-hint+1$

$d \equiv e^{-1} \mod \phi \Leftrightarrow d*e \equiv 1 \mod \phi \Leftrightarrow d*e = k*\phi + 1, k \in \mathbb{N^*}$

$\Leftrightarrow d*e = k*(n-hint+1)+1 \Leftrightarrow n = \dfrac{d*e-1}{k}+hint - 1$

Next, we will bruteforce k to find n and then try that n to decode m. If in m there is the phrase "W1{", then that is the flag to find.




Here is my [script](./sol.py)

    Flag: W1{phi_phai_la_game_rac_so_1_vn}
