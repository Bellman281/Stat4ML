"""
Chapter 4 -- RUSTLINGS-STYLE EXERCISE (Python, Research tier)
Part II: Introduction to Statistical Learning

Funk SVD: one SGD step over an observed cell (ch04_text.tex Section 3), plus
the bias prediction mu + b_u + b_i + p.q. Two deliberate bugs (predict_bias,
sgd_update). Fix one function at a time until all tests pass. Do not edit
run_tests().
"""
# level: research


def predict(p, q):
    return sum(pi * qi for pi, qi in zip(p, q))


def predict_bias(mu, bu, bi, p, q):
    # BUG: the item bias b_i is dropped. The full model is mu + b_u + b_i + p.q.
    return mu + bu + predict(p, q)


def sgd_update(p, q, r, lr, lam):
    # BUG: the residual sign is flipped. It must be err = r - p.q (the amount
    # the prediction falls short); with the sign reversed the step climbs the
    # loss instead of descending it.
    err = predict(p, q) - r
    p_new = [pi + lr * (err * qi - lam * pi) for pi, qi in zip(p, q)]
    q_new = [qi + lr * (err * pi - lam * qi) for pi, qi in zip(p, q)]
    return p_new, q_new, err


def run_tests():
    failures = []

    def check(name, got, expected, tol=1e-9):
        ok = abs(got - expected) < tol
        print(f"[{'PASS' if ok else 'FAIL'}] {name}: got={got!r} expected={expected!r}")
        if not ok:
            failures.append(name)

    # 3.5 + 0.2 + (-0.1) + (1*2 + 0*1) = 5.6
    check("predict_bias", predict_bias(3.5, 0.2, -0.1, [1.0, 0.0], [2.0, 1.0]), 5.6)

    p, q, r, lr, lam = [1.0, 0.5], [0.5, 2.0], 4.0, 0.1, 0.05
    sq_before = (r - predict(p, q)) ** 2
    p_new, q_new, err = sgd_update(p, q, r, lr, lam)
    check("err", err, 2.5)                 # r - p.q = 4 - 1.5
    check("p_new0", p_new[0], 1.12)
    check("p_new1", p_new[1], 0.9975)
    check("q_new0", q_new[0], 0.7475)
    check("q_new1", q_new[1], 2.115)

    # the step should DECREASE the squared error on this cell
    sq_after = (r - predict(p_new, q_new)) ** 2
    check("step_decreases_error", 1.0 if sq_after < sq_before else 0.0, 1.0)

    print()
    if failures:
        print(f"{len(failures)} test(s) FAILED: {failures}")
        raise SystemExit(1)
    print("All tests passed!")


if __name__ == "__main__":
    run_tests()
