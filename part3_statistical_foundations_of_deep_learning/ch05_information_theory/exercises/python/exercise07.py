"""
Chapter 5 exercise -- mutual information and perplexity (Research tier)
Part III: Statistical Foundations of Deep Learning & RL

HOMEWORK: implement each TODO using ch05_text.tex Sections 2-3. `joint` is a 2-D
list (list of rows) giving p(x, y) over a grid, summing to 1.
  - perplexity        : exp(cross-entropy in nats).
  - joint_entropy     : H(X, Y) = -sum p(x,y) log p(x,y)  (skip zero cells).
  - mutual_information : I(X;Y) = sum p(x,y) log( p(x,y) / (p(x) p(y)) ).

Run with:  python3 exercise07.py
Reference solution: solutions/exercise07_solution.py
"""
# level: research
import math


def perplexity(cross_entropy_nats):
    """Perplexity = exp(cross-entropy)."""
    raise NotImplementedError("TODO: perplexity")


def joint_entropy(joint):
    """H(X,Y) = -sum_{x,y} p(x,y) log p(x,y), skipping zero cells."""
    raise NotImplementedError("TODO: joint_entropy")


def mutual_information(joint):
    """I(X;Y) = sum p(x,y) log( p(x,y) / (p(x) p(y)) ), skipping zero cells."""
    raise NotImplementedError("TODO: mutual_information")


def main():
    corr = [[0.5, 0.0], [0.0, 0.5]]      # perfectly correlated
    indep = [[0.25, 0.25], [0.25, 0.25]] # independent
    print("perplexity(log 5)   :", perplexity(math.log(5)))
    print("joint_entropy(corr) :", joint_entropy(corr))
    print("MI(correlated)      :", mutual_information(corr))
    print("MI(independent)     :", mutual_information(indep))


if __name__ == "__main__":
    main()
