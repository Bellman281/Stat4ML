"""
Chapter 4 -- RUSTLINGS-STYLE EXERCISE (Python, Research tier)
Part III: Statistical Foundations of Deep Learning & RL

Two deliberate bugs (gaussian_kl, elbo). Fix one function at a time until all
tests pass. Do not edit run_tests().
"""
# level: research
import math


def gaussian_kl(mu, sigma2):
    # BUG: the KL has -log(sigma2), not +log(sigma2) (ch04_text.tex Section 2).
    return 0.5 * (sigma2 + mu ** 2 - 1 + math.log(sigma2))


def mc_expectation(samples):
    return sum(samples) / len(samples)


def elbo(recon_loglik, mu, sigma2):
    # BUG: the ELBO SUBTRACTS the KL (reconstruction minus KL), not adds it.
    return recon_loglik + gaussian_kl(mu, sigma2)


def run_tests():
    failures = []

    def check(name, got, expected, tol=1e-9):
        ok = abs(got - expected) < tol
        print(f"[{'PASS' if ok else 'FAIL'}] {name}: got={got!r} expected={expected!r}")
        if not ok:
            failures.append(name)

    check("kl_prior_equals_prior", gaussian_kl(0.0, 1.0), 0.0)   # KL(N(0,1)||N(0,1))=0
    check("kl_shifted", gaussian_kl(1.0, 1.0), 0.5)
    check("kl_scaled", gaussian_kl(0.0, 2.0), 0.5 * (2 - 1 - math.log(2)))
    check("mc_expectation", mc_expectation([-2.0, -1.0, -3.0]), -2.0)
    check("elbo", elbo(-2.0, 1.0, 1.0), -2.0 - 0.5)

    print()
    if failures:
        print(f"{len(failures)} test(s) FAILED: {failures}")
        raise SystemExit(1)
    print("All tests passed!")


if __name__ == "__main__":
    run_tests()
