# Solution


We have: $leak \equiv p^2 + q^2 \mod n\Leftrightarrow (p+q)^2 \equiv leak + 2pq\equiv leak +2n\equiv leak \mod n$
```math
\Rightarrow (p+q)^2=leak+k*n\Leftrightarrow p+q = \sqrt{leak+k*n}
```

Next, we will bruteforce k to find $S=p+q$, combine it with $n=pq$ and then calculate the solution of the equation $x^2-Sx+n=0$ to get the results p, q (if p | n and p is prime, this is satisfied). Then use this pair (p, q) to find $\phi$, d and finally m.



Here is my [script](./sol.py)

    Flag: W1{i_hope_you_like_this_one}
