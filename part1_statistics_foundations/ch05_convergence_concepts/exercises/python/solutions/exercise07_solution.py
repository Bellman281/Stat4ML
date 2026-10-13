"""Chapter 5 -- reference solution (Research)."""
# level: research
import math


def mgf_standard_normal(t):
    return math.exp(t * t / 2)


def clt_mgf_limit(t, n):
    return (1 + t * t / (2 * n)) ** n


def delta_method_variance(gprime, sigma2):
    return gprime ** 2 * sigma2


def delta_method_sd(gprime, sigma2):
    return abs(gprime) * math.sqrt(sigma2)


def main():
    print("MGF N(0,1) at t=0.5 :", mgf_standard_normal(0.5))
    print("CLT MGF limit t=2   :", clt_mgf_limit(2.0, 1_000_000))
    print("delta variance      :", delta_method_variance(2.0, 3.0))
    print("delta sd            :", delta_method_sd(2.0, 3.0))


if __name__ == "__main__":
    main()
