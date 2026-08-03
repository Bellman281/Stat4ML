"""Chapter 2 -- reference solution."""
import math
import random


def expected_value(values, probs):
    return sum(v * p for v, p in zip(values, probs))


def variance(values, probs):
    mu = expected_value(values, probs)
    ex2 = expected_value([v * v for v in values], probs)
    return ex2 - mu * mu


def covariance(xy_values, joint_probs):
    ex = sum(x * p for (x, y), p in zip(xy_values, joint_probs))
    ey = sum(y * p for (x, y), p in zip(xy_values, joint_probs))
    exy = sum(x * y * p for (x, y), p in zip(xy_values, joint_probs))
    return exy - ex * ey


def correlation(cov_xy, var_x, var_y):
    return cov_xy / (math.sqrt(var_x) * math.sqrt(var_y))


def normal_mgf_theoretical(t, mu, sigma2):
    return math.exp(mu * t + sigma2 * t * t / 2.0)


def _standard_normal_pair(rng):
    u1, u2 = rng.random(), rng.random()
    u1 = max(u1, 1e-12)
    r = math.sqrt(-2.0 * math.log(u1))
    theta = 2.0 * math.pi * u2
    return r * math.cos(theta), r * math.sin(theta)


def normal_mgf_monte_carlo(t, mu, sigma2, n, seed=0):
    rng = random.Random(seed)
    sigma = math.sqrt(sigma2)
    total = 0.0
    count = 0
    while count < n:
        z1, z2 = _standard_normal_pair(rng)
        for z in (z1, z2):
            if count >= n:
                break
            x = mu + sigma * z
            total += math.exp(t * x)
            count += 1
    return total / n


def main():
    xs = [0, 1, 2, 3]
    ps = [1 / 8, 3 / 8, 3 / 8, 1 / 8]
    mu = expected_value(xs, ps)
    var = variance(xs, ps)
    print(f"E[X] = {mu}, Var(X) = {var}  (Binomial(3, 0.5): expect mean 1.5, var 0.75)")

    xy = [(0, 0), (0, 1), (1, 0), (1, 1)]
    joint = [0.4, 0.1, 0.1, 0.4]
    cov = covariance(xy, joint)
    var_x = variance([0, 1], [0.5, 0.5])
    print(f"Cov(X,Y) = {cov}, corr = {correlation(cov, var_x, var_x)}")

    mu_n, sigma2_n, t = 2.0, 4.0, 0.4
    theo = normal_mgf_theoretical(t, mu_n, sigma2_n)
    mc = normal_mgf_monte_carlo(t, mu_n, sigma2_n, 200_000, seed=7)
    print(f"Normal MGF at t={t}: theoretical={theo:.5f}, Monte Carlo={mc:.5f}")


if __name__ == "__main__":
    main()
