"""
Chapter 6 -- RUSTLINGS-STYLE EXERCISE (Python, Proof tier)
Part II: Introduction to Statistical Learning

Two deliberate bugs (elbo, kl). Fix one function at a time until all tests
pass. Do not edit run_tests().
"""
# level: proof
import math


def log_evidence(joint):
    return math.log(sum(joint))


def elbo(q, joint):
    # BUG: the ELBO subtracts the entropy term log(q_z); this keeps only
    # sum_z q_z log(joint_z) (ch06_text.tex Section 2).
    return sum(qz * math.log(jz) for qz, jz in zip(q, joint))


def kl(q, p):
    # BUG: KL(q||p) uses log(q_z / p_z), not log(p_z / q_z).
    return sum(qz * math.log(pz / qz) for qz, pz in zip(q, p))


def run_tests():
    failures = []
    def check(name, got, expected, tol=1e-6):
        ok = abs(got - expected) < tol
        print(f"[{'PASS' if ok else 'FAIL'}] {name}: got={got!r} expected={expected!r}")
        if not ok: failures.append(name)

    joint = [0.2, 0.3]; q = [0.5, 0.5]; post = [0.4, 0.6]
    check("log_evidence", log_evidence(joint), math.log(0.5))
    check("elbo", elbo(q, joint),
          0.5 * math.log(0.4) + 0.5 * math.log(0.6))
    check("kl", kl(q, post),
          0.5 * math.log(0.5 / 0.4) + 0.5 * math.log(0.5 / 0.6))
    check("identity: elbo+kl=log_evidence", elbo(q, joint) + kl(q, post), math.log(0.5))

    print()
    if failures:
        print(f"{len(failures)} test(s) FAILED: {failures}")
        raise SystemExit(1)
    print("All tests passed!")


if __name__ == "__main__":
    run_tests()
