"""
Chapter 4 exercise -- Funk SVD SGD step and biases (Research tier)
Part II: Introduction to Statistical Learning

HOMEWORK: ch04_text.tex Section 3. Implement:
  - predict_bias : mu + b_u + b_i + p.q
  - sgd_update   : one SGD step on an observed cell. With err = r - p.q,
                     p <- p + lr*(err*q - lam*p),  q <- q + lr*(err*p - lam*q).
                     Use the OLD p when updating q. Return (p_new, q_new, err).

Run with:  python3 exercise06.py
Reference solution: solutions/exercise06_solution.py
"""
# level: research


def predict(p, q):
    return sum(pi * qi for pi, qi in zip(p, q))


def predict_bias(mu, bu, bi, p, q):
    # TODO: mu + b_u + b_i + p.q
    raise NotImplementedError("TODO: predict_bias")


def sgd_update(p, q, r, lr, lam):
    # TODO: err = r - p.q ; step p and q toward each other with a ridge shrink;
    # return (p_new, q_new, err)
    raise NotImplementedError("TODO: sgd_update")


def main():
    print("predict_bias :", predict_bias(3.5, 0.2, -0.1, [1.0, 0.0], [2.0, 1.0]))
    p_new, q_new, err = sgd_update([1.0, 0.5], [0.5, 2.0], 4.0, 0.1, 0.05)
    print("err          :", err)
    print("p_new        :", p_new)
    print("q_new        :", q_new)


if __name__ == "__main__":
    main()
