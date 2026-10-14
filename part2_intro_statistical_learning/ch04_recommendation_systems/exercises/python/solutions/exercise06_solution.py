"""Chapter 4 -- reference solution (Research): Funk SVD SGD step and biases."""
# level: research


def predict(p, q):
    return sum(pi * qi for pi, qi in zip(p, q))


def predict_bias(mu, bu, bi, p, q):
    """Full prediction with the bias terms: mu + b_u + b_i + p.q."""
    return mu + bu + bi + predict(p, q)


def sgd_update(p, q, r, lr, lam):
    """One Funk-SVD step on observed cell (u, i). Returns (p_new, q_new, err).
    err = r - p.q ; each factor moves toward the other in proportion to err,
    with a ridge shrink. q_new uses the OLD p."""
    err = r - predict(p, q)
    p_new = [pi + lr * (err * qi - lam * pi) for pi, qi in zip(p, q)]
    q_new = [qi + lr * (err * pi - lam * qi) for pi, qi in zip(p, q)]
    return p_new, q_new, err


def main():
    print("predict_bias :", predict_bias(3.5, 0.2, -0.1, [1.0, 0.0], [2.0, 1.0]))
    p_new, q_new, err = sgd_update([1.0, 0.5], [0.5, 2.0], 4.0, 0.1, 0.05)
    print("err          :", err)
    print("p_new        :", p_new)
    print("q_new        :", q_new)


if __name__ == "__main__":
    main()
