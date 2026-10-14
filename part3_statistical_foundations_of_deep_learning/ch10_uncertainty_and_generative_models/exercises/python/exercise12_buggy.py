"""
Chapter 10 -- RUSTLINGS-STYLE EXERCISE (Python, Research tier)
Part III: Statistical Foundations of Deep Learning & RL

Two deliberate bugs (gaussian_score, langevin_step). Fix one function at a time
until all tests pass. Do not edit run_tests(). The last test checks that the DSM
target equals the score of the noising kernel (they must agree).
"""
# level: research


def gaussian_score(x, mu, sigma2):
    # BUG: the score points TOWARD the mean: -(x - mu)/sigma2. This has the sign
    # flipped (it would push samples away from the mode).
    return (x - mu) / sigma2


def denoising_target(x_noisy, x_clean, sigma2):
    return -(x_noisy - x_clean) / sigma2


def langevin_step(x, score, step):
    # BUG: generation moves UPHILL along the score: x + step*score, not against it.
    return x - step * score


def run_tests():
    failures = []

    def check(name, got, expected, tol=1e-9):
        ok = abs(got - expected) < tol
        print(f"[{'PASS' if ok else 'FAIL'}] {name}: got={got!r} expected={expected!r}")
        if not ok:
            failures.append(name)

    check("gaussian_score", gaussian_score(3.0, 1.0, 2.0), -1.0)
    check("denoising_target", denoising_target(3.0, 1.0, 2.0), -1.0)
    check("langevin_step", langevin_step(3.0, -1.0, 0.5), 2.5)
    # DSM target equals the score of the Gaussian noising kernel p(x_noisy|x_clean)
    check("DSM target = score", denoising_target(3.0, 1.0, 2.0),
          gaussian_score(3.0, 1.0, 2.0))

    print()
    if failures:
        print(f"{len(failures)} test(s) FAILED: {failures}")
        raise SystemExit(1)
    print("All tests passed!")


if __name__ == "__main__":
    run_tests()
