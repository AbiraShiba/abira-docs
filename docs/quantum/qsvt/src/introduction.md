# イントロダクション

## 目的

https://arxiv.org/abs/1606.02685 を参考に量子特異値変換（QSVT）を学ぶ。

## ここでの結果のまとめ

あるブロックエンコーディング
```math
\begin{align}
  & U = \mqty[
    A & * \\
    * & *
  ]
  \qc
  A = U \Sigma V^{\dagger}
\end{align}
```
されたユニタリ行列がある場合、$A$ の特異値 $\sigma_{i}$ に対して
```math
\begin{align}
  & \sigma_{i} \mapsto P(\sigma_{i})
\end{align}
```
と特異値が変換された行列
```math
\begin{align}
  & U = \mqty[
    P(A) & * \\
    * & *
  ]
  \qc
  P(A) := U P\qty(\Sigma) V^{\dagger}
\end{align}
```
を構築することが可能であるという理論がある。これが QSVT である。

この変換を用いることで
* Grover → 幾何学的振幅回転
* 位相推定 → フーリエ解析
* HHL → 位相推定＋条件付き回転
* ハミルトニアンシミュレーション → Trotter 展開

と今までの有名アルゴリズムを再解釈することが可能になる。つまり
* QSVT は「量子計算を多項式近似理論に還元する定理」である

という結論が得られることです。

## 関連の文献

* https://arxiv.org/abs/1409.3305
  * Fixed-point quantum search with an optimal number of queries について詳しい
* https://arxiv.org/abs/2105.02859
  * QSVTを用いた量子アルゴリズムの一般論を議論している

なんか殆どに Chuang がいてすごいですね……
