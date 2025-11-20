# Solution

### Analysis
We are given a Linear System over a Finite Field $\mathbb{F}_p$ (where $p=3671$) with introduced noise, resembling a simplified **Learning With Errors (LWE)** problem.

The encryption process is defined as:
$$b = A \cdot s + e$$

Where:
* $s$: The flag encoded as a vector in $\mathbb{F}_{3671}^{22}$.
* $A$: A known random $22 \times 22$ matrix.
* $e$: An unknown error vector where each $e_i \in \{2006, 2506\}$.

### Vulnerability
The security of LWE relies on the difficulty of determining the error term $e$. However, in this challenge, the error distribution is extremely narrow. Since each of the 22 elements of $e$ can only take one of two values, the entropy of the error vector is low.

The complexity to brute-force the error vector is $2^{22} \approx 4 \times 10^6$, which is computationally trivial on modern hardware.

### Solution Strategy
1.  Compute the inverse matrix $A^{-1}$.
2.  Iterate through all $2^{22}$ possible permutations of the error vector $e$.
3.  For each candidate $e'$, compute the potential flag vector:
    $$s' = A^{-1} \cdot (b - e')$$
4.  Convert $s'$ back to bytes and check for the flag prefix `W1{`.

Here is the full solution [script](./sol.py).

    Flag: W1{M3ss1_1s_t43_90AT!!!}