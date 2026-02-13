# Quantum Signal Processing (QST)

```math
\begin{align}
  & W(a) = \mqty[
    a & i \sqrt{1-a^2} \\
    i\sqrt{1-a^2} & a
  ]
  \\
  & U_{\vb*\phi} = e^{i \phi_{0}Z} \prod_{k=1}^{d} W(a) e^{i \phi_{k} Z}
  = \mqty[
    P(a) & iQ^{*}(a)\sqrt{1-a^2} \\
    iQ(a)\sqrt{1-a^2} & P^{*}(a)
    ]
\end{align}
```
* $\deg \qty(P) \leq d \qc \deg \qty(Q) \leq d-1$
* $P$ はパリティ $d \mod 2$ で $Q$はパリティ $d-1 \mod 2$
* $\det U_{\vb*\phi} = \abs{P}^2 + \qty(1-a^2) \abs{Q}^2 = 1$
