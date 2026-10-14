"""
Chapter 8 exercise -- attention as kernel smoothing, and PMI (Research tier)
Part III: Statistical Foundations of Deep Learning & RL

HOMEWORK: implement each TODO using ch08_text.tex Sections 2-3.
  - softmax_weights : the attention weights, softmax of the scores.
  - attention       : the Nadaraya-Watson output, sum_i weight_i * value_i.
  - pmi             : pointwise mutual information log( p(x,y) / (p(x) p(y)) ).

Run with:  python3 exercise10.py
Reference solution: solutions/exercise10_solution.py
"""
# level: research
import math


def softmax_weights(scores):
    """Softmax of the scores (the attention weights, summing to 1)."""
    raise NotImplementedError("TODO: softmax_weights")


def attention(scores, values):
    """Nadaraya-Watson / attention output: sum_i softmax(scores)_i * values_i."""
    raise NotImplementedError("TODO: attention")


def pmi(p_xy, p_x, p_y):
    """Pointwise mutual information: log( p(x,y) / (p(x) * p(y)) )."""
    raise NotImplementedError("TODO: pmi")


def main():
    print("softmax_weights :", softmax_weights([0.0, 0.0]))
    print("attention       :", attention([0.0, 0.0], [2.0, 4.0]))
    print("pmi             :", pmi(0.1, 0.2, 0.25))


if __name__ == "__main__":
    main()
