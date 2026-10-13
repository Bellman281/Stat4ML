"""
Chapter 5 -- RUSTLINGS-STYLE EXERCISE (Python, Proof tier)
Part II: Introduction to Statistical Learning

Two deliberate bugs (projected_variance, top_eigenvalue_2x2). Fix one
function at a time until all tests pass. Do not edit run_tests().
"""
# level: proof
import math


def matvec2(S, w):
    return [S[0][0] * w[0] + S[0][1] * w[1],
            S[1][0] * w[0] + S[1][1] * w[1]]


def projected_variance(S, w):
    # BUG: the variance is w . (S @ w), a scalar; this returns only the first
    # component of S @ w (ch05_text.tex Section 2).
    return matvec2(S, w)[0]


def top_eigenvalue_2x2(S):
    # BUG: the LARGEST eigenvalue uses the + root; this uses the - root
    # (the smallest).
    tr = S[0][0] + S[1][1]
    det = S[0][0] * S[1][1] - S[0][1] * S[1][0]
    return (tr - math.sqrt(tr * tr - 4 * det)) / 2


def run_tests():
    failures = []
    def check(name, got, expected, tol=1e-5):
        ok = (got == expected) if isinstance(expected, list) else abs(got - expected) < tol
        print(f"[{'PASS' if ok else 'FAIL'}] {name}: got={got!r} expected={expected!r}")
        if not ok: failures.append(name)

    check("matvec2", matvec2([[2, 0], [0, 1]], [1, 0]), [2, 0])
    check("projected_variance", projected_variance([[2, 0], [0, 1]], [0.6, 0.8]), 1.36)
    check("top_eigenvalue_2x2", top_eigenvalue_2x2([[2.0, 0.8], [0.8, 0.6]]), 2.3627416998)

    print()
    if failures:
        print(f"{len(failures)} test(s) FAILED: {failures}")
        raise SystemExit(1)
    print("All tests passed!")


if __name__ == "__main__":
    run_tests()
