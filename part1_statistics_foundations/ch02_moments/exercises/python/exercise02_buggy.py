"""
Chapter 2 -- RUSTLINGS-STYLE EXERCISE (Python edition)
Part I: Statistics Foundation for ML

Four deliberate bugs are hiding below (in variance, correlation,
normal_mgf_theoretical, and normal_mgf_monte_carlo). Run this file, read
the first failing assertion, fix ONLY that function, and re-run -- repeat
until you see "All tests passed!". Do not edit run_tests().
"""
import math
import random


def expected_value(values, probs):
    # Correct.
    return sum(v * p for v, p in zip(values, probs))


def variance(values, probs):
    # BUG: this is the exact mistake called out in ch02_text.tex Section
    # 1.2 -- returns E[X^2] and forgets to subtract (E[X])^2.
    ex2 = expected_value([v * v for v in values], probs)
    return ex2


def covariance(xy_values, joint_probs):
    # Correct.
    ex = sum(x * p for (x, y), p in zip(xy_values, joint_probs))
    ey = sum(y * p for (x, y), p in zip(xy_values, joint_probs))
    exy = sum(x * y * p for (x, y), p in zip(xy_values, joint_probs))
    return exy - ex * ey


def correlation(cov_xy, var_x, var_y):
    # BUG: divides by the variances themselves instead of the standard
    # deviations (forgot the sqrt from ch02_text.tex Section 2, Def 2.2).
    return cov_xy / (var_x * var_y)


def normal_mgf_theoretical(t, mu, sigma2):
    # BUG: missing the "/2" in the exponent -- should be
    # exp(mu*t + sigma2*t^2/2), not exp(mu*t + sigma2*t^2).
    return math.exp(mu * t + sigma2 * t * t)


def _standard_normal_pair(rng):
    u1, u2 = rng.random(), rng.random()
    u1 = max(u1, 1e-12)
    r = math.sqrt(-2.0 * math.log(u1))
    theta = 2.0 * math.pi * u2
    return r * math.cos(theta), r * math.sin(theta)


def normal_mgf_monte_carlo(t, mu, sigma2, n, seed=0):
    # BUG: forgets to scale by sigma (uses standard-normal Z directly as
    # if sigma2 were always 1), so the estimate is wrong whenever
    # sigma2 != 1.
    rng = random.Random(seed)
    total = 0.0
    count = 0
    while count < n:
        z1, z2 = _standard_normal_pair(rng)
        for z in (z1, z2):
            if count >= n:
                break
            x = mu + z  # <-- missing "* math.sqrt(sigma2)"
            total += math.exp(t * x)
            count += 1
    return total / n


# --------------------------------------------------------------------------
# Test harness -- do not edit below this line.
# --------------------------------------------------------------------------
def run_tests():
    failures = []

    def check(name, got, expected, tol=1e-6):
        ok = abs(got - expected) < tol
        status = "PASS" if ok else "FAIL"
        print(f"[{status}] {name}: got={got!r} expected={expected!r}")
        if not ok:
            failures.append(name)

    xs, ps = [0, 1, 2, 3], [1 / 8, 3 / 8, 3 / 8, 1 / 8]
    check("expected_value (Binomial(3,0.5))", expected_value(xs, ps), 1.5)
    check("variance (Binomial(3,0.5))", variance(xs, ps), 0.75)

    xy = [(0, 0), (0, 1), (1, 0), (1, 1)]
    joint = [0.4, 0.1, 0.1, 0.4]
    cov = covariance(xy, joint)
    check("covariance (positively associated)", cov, 0.15)

    check("correlation(cov=0.16, var_x=0.25, var_y=0.25)",
          correlation(0.16, 0.25, 0.25), 0.64)

    theo = normal_mgf_theoretical(0.4, 2.0, 4.0)
    check("normal_mgf_theoretical(t=0.4, mu=2.0, sigma2=4.0)", round(theo, 5),
          round(math.exp(2.0 * 0.4 + 4.0 * 0.4 * 0.4 / 2.0), 5))

    mc = normal_mgf_monte_carlo(0.4, 2.0, 4.0, 300_000, seed=7)
    expected_mc = math.exp(2.0 * 0.4 + 4.0 * 0.4 * 0.4 / 2.0)
    check("normal_mgf_monte_carlo(t=0.4, mu=2.0, sigma2=4.0) ~ theoretical",
          round(mc, 1), round(expected_mc, 1), tol=0.15)

    print()
    if failures:
        print(f"{len(failures)} test(s) FAILED: {failures}")
        raise SystemExit(1)
    print("All tests passed!")


if __name__ == "__main__":
    run_tests()
