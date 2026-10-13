"""
Chapter 8 -- RUSTLINGS-STYLE EXERCISE (Python, Proof tier)
Part II: Introduction to Statistical Learning

Two deliberate bugs (cross_entropy, ce_grad). Fix one function at a time until
all tests pass. Do not edit run_tests(). The key test checks the chapter's
identity dL/dz = p - y against a numerical gradient.
"""
# level: proof
import math


def softmax(zs):
    m = max(zs)
    exps = [math.exp(z - m) for z in zs]
    tot = sum(exps)
    return [e / tot for e in exps]


def cross_entropy(p, y):
    # BUG: cross-entropy is -sum y*log(p); the leading minus sign is missing.
    return sum(yk * math.log(pk) for pk, yk in zip(p, y))


def ce_grad(p, y):
    # BUG: the gradient at the logits is p - y, not y - p (ch08_text.tex Sec 2).
    return [yk - pk for pk, yk in zip(p, y)]


def run_tests():
    failures = []

    def check(name, cond, detail=""):
        print(f"[{'PASS' if cond else 'FAIL'}] {name}{(': ' + detail) if detail else ''}")
        if not cond:
            failures.append(name)

    z = [2.0, 0.5, -1.0]
    y = [1.0, 0.0, 0.0]
    p = softmax(z)

    # cross-entropy must be positive here and equal -log p_true
    L = cross_entropy(p, y)
    check("cross_entropy", abs(L - (-math.log(p[0]))) < 1e-9, f"got {L}")

    # the gradient must equal p - y directly...
    g = ce_grad(p, y)
    expected = [p[k] - y[k] for k in range(len(p))]
    check("ce_grad == p - y", all(abs(a - b) < 1e-9 for a, b in zip(g, expected)),
          f"got {g}")

    # ...and must match finite differences of L(softmax(z))
    eps = 1e-6
    for k in range(len(z)):
        zp = z[:]; zp[k] += eps
        zm = z[:]; zm[k] -= eps
        num = (cross_entropy(softmax(zp), y) - cross_entropy(softmax(zm), y)) / (2 * eps)
        check(f"grad[{k}] matches numeric", abs(g[k] - num) < 1e-4, f"{g[k]:.6f} vs {num:.6f}")

    print()
    if failures:
        print(f"{len(failures)} test(s) FAILED: {failures}")
        raise SystemExit(1)
    print("All tests passed!")


if __name__ == "__main__":
    run_tests()
