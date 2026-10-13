"""Chapter 5 -- reference solution (Core)."""
# level: core
import math


def var_of_sample_mean(sigma2, n):
    return sigma2 / n


def chebyshev_bound(sigma2, n, eps):
    return sigma2 / (n * eps ** 2)


def running_mean(data):
    out, total = [], 0.0
    for i, x in enumerate(data, start=1):
        total += x
        out.append(total / i)
    return out


def clt_standardized(xbar, mu, sigma, n):
    return (xbar - mu) / (sigma / math.sqrt(n))


def main():
    print("Var(Xbar) sigma2=4,n=100 :", var_of_sample_mean(4.0, 100))
    print("Chebyshev bound           :", chebyshev_bound(4.0, 100, 0.5))
    print("running mean of [2,4,6]   :", running_mean([2, 4, 6]))
    print("standardized (1.6,1,2,100):", clt_standardized(1.6, 1.0, 2.0, 100))


if __name__ == "__main__":
    main()
