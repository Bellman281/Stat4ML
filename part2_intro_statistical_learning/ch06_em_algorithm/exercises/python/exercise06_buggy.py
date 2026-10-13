"""
Chapter 6 -- RUSTLINGS-STYLE EXERCISE (Python, Core tier)
Part II: Introduction to Statistical Learning

Two deliberate bugs (gaussian_pdf, responsibility). Fix one function at a
time until all tests pass. Do not edit run_tests().
"""
# level: core
import math


def gaussian_pdf(x, mu, s2):
    # BUG: the density has a 1/sqrt(2*pi*s2) normaliser out front; it's
    # dropped here (ch06_text.tex Section 1).
    return math.exp(-(x - mu) ** 2 / (2 * s2))


def responsibility(x, pis, mus, s2s, k):
    # BUG: a responsibility is NORMALISED by the total over components; this
    # returns the unnormalised pi_k N_k.
    return pis[k] * gaussian_pdf(x, mus[k], s2s[k])


def weighted_mean(xs, resps):
    return sum(r * xi for r, xi in zip(resps, xs)) / sum(resps)


def run_tests():
    failures = []
    def check(name, got, expected, tol=1e-6):
        ok = abs(got - expected) < tol
        print(f"[{'PASS' if ok else 'FAIL'}] {name}: got={got!r} expected={expected!r}")
        if not ok: failures.append(name)

    check("gaussian_pdf(0,0,1)", gaussian_pdf(0.0, 0.0, 1.0), 1 / math.sqrt(2 * math.pi))
    check("responsibility (symmetric)",
          responsibility(0.0, [0.5, 0.5], [-1, 1], [1, 1], 0), 0.5)
    check("weighted_mean", weighted_mean([1, 2, 3], [1, 1, 0]), 1.5)

    print()
    if failures:
        print(f"{len(failures)} test(s) FAILED: {failures}")
        raise SystemExit(1)
    print("All tests passed!")


if __name__ == "__main__":
    run_tests()
