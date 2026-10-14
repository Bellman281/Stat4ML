"""Chapter 8 -- reference solution (Research)."""
# level: research
import math


def softmax_weights(scores):
    m = max(scores)
    e = [math.exp(s - m) for s in scores]
    tot = sum(e)
    return [ei / tot for ei in e]


def attention(scores, values):
    w = softmax_weights(scores)
    return sum(wi * vi for wi, vi in zip(w, values))


def pmi(p_xy, p_x, p_y):
    return math.log(p_xy / (p_x * p_y))


def main():
    print("softmax_weights :", softmax_weights([0.0, 0.0]))
    print("attention       :", attention([0.0, 0.0], [2.0, 4.0]))
    print("pmi             :", pmi(0.1, 0.2, 0.25))


if __name__ == "__main__":
    main()
