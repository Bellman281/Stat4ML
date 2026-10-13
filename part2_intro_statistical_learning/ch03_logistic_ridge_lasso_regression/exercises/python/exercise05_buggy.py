"""
Chapter 3 -- RUSTLINGS-STYLE EXERCISE (Python, Research tier)
Part II: Introduction to Statistical Learning

Two deliberate bugs (l1_penalty, elastic_net_penalty). Fix one function at a
time until all tests pass. Do not edit run_tests().
"""
# level: research
def l1_penalty(beta, lam):
    # BUG: the L1 penalty sums ABSOLUTE values, not the raw coefficients.
    return lam * sum(beta)


def l2_penalty(beta, lam):
    return lam * sum(b * b for b in beta)


def elastic_net_penalty(beta, lam, alpha):
    # BUG: alpha weights the L1 term and (1-alpha) the L2 term; these are
    # swapped here (ch03_text.tex Section 3).
    return lam * ((1 - alpha) * sum(abs(b) for b in beta) + alpha * sum(b * b for b in beta))


def run_tests():
    failures = []
    def check(name, got, expected, tol=1e-6):
        ok = abs(got - expected) < tol
        print(f"[{'PASS' if ok else 'FAIL'}] {name}: got={got!r} expected={expected!r}")
        if not ok: failures.append(name)

    b = [1.0, -2.0, 3.0]                    # sum|b| = 6, sum b^2 = 14
    check("l1_penalty", l1_penalty(b, 1.0), 6.0)
    check("l2_penalty", l2_penalty(b, 1.0), 14.0)
    check("elastic_net (alpha=0.25)", elastic_net_penalty(b, 1.0, 0.25), 12.0)

    print()
    if failures:
        print(f"{len(failures)} test(s) FAILED: {failures}")
        raise SystemExit(1)
    print("All tests passed!")


if __name__ == "__main__":
    run_tests()
