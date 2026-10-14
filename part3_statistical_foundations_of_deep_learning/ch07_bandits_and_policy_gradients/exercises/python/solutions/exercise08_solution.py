"""Chapter 7 -- reference solution (Proof)."""
# level: proof
import math


def softmax(logits):
    m = max(logits)
    e = [math.exp(z - m) for z in logits]
    s = sum(e)
    return [ei / s for ei in e]


def logit_score(a, probs):
    return [(1.0 if i == a else 0.0) - probs[i] for i in range(len(probs))]


def pg_grad(R, a, probs):
    return [R * s for s in logit_score(a, probs)]


def main():
    p = softmax([0.0, 0.5, -0.5])
    print("softmax     :", p)
    print("logit_score :", logit_score(1, [0.2, 0.5, 0.3]))
    print("pg_grad     :", pg_grad(2.0, 1, [0.2, 0.5, 0.3]))
    mean = [sum(p[a] * logit_score(a, p)[i] for a in range(3)) for i in range(3)]
    print("mean score  :", [round(x, 12) for x in mean])


if __name__ == "__main__":
    main()
