"""
Chapter 7 exercise -- the policy gradient and the score (Proof tier)
Part III: Statistical Foundations of Deep Learning & RL

HOMEWORK: implement each TODO using ch07_text.tex Section 2. For a softmax
policy over logits, the score of action a (gradient of log pi wrt the logits) is
the vector  e_a - p,  i.e. (1 if i==a else 0) - p_i.
  - softmax      : the policy probabilities.
  - logit_score  : the score vector e_a - p for action a.
  - pg_grad      : the REINFORCE estimate R * logit_score(a, p).

The test checks the mean-zero-score identity: sum_a p_a * logit_score(a) = 0.

Run with:  python3 exercise08.py
Reference solution: solutions/exercise08_solution.py
"""
# level: proof
import math


def softmax(logits):
    m = max(logits)
    e = [math.exp(z - m) for z in logits]
    s = sum(e)
    return [ei / s for ei in e]


def logit_score(a, probs):
    """Score vector for action a: [ (1 if i==a else 0) - probs[i] for all i ]."""
    raise NotImplementedError("TODO: logit_score")


def pg_grad(R, a, probs):
    """REINFORCE gradient estimate: R * logit_score(a, probs) (element-wise)."""
    raise NotImplementedError("TODO: pg_grad")


def main():
    p = softmax([0.0, 0.5, -0.5])
    print("softmax     :", p)
    print("logit_score :", logit_score(1, [0.2, 0.5, 0.3]))
    print("pg_grad     :", pg_grad(2.0, 1, [0.2, 0.5, 0.3]))
    # mean score over the policy should be the zero vector
    mean = [sum(p[a] * logit_score(a, p)[i] for a in range(3)) for i in range(3)]
    print("mean score  :", [round(x, 12) for x in mean])


if __name__ == "__main__":
    main()
