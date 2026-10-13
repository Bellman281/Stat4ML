"""Chapter 6 -- reference solution (Core)."""
# level: core
import math


def bernoulli_loglik(p, data):
    return sum(x * math.log(p) + (1 - x) * math.log(1 - p) for x in data)


def bernoulli_mle(data):
    return sum(data) / len(data)


def poisson_mle(data):
    return sum(data) / len(data)


def normal_mle(data):
    n = len(data)
    mu = sum(data) / n
    sigma2 = sum((x - mu) ** 2 for x in data) / n
    return (mu, sigma2)


def main():
    b = [1, 1, 0, 1, 0, 1, 0, 0, 1, 1]
    print(f"Bernoulli MLE p_hat = {bernoulli_mle(b)}")
    print(f"log-lik at 0.6     = {bernoulli_loglik(0.6, b):.4f}")
    print(f"Poisson MLE        = {poisson_mle([2,1,3,0,2,1,4,2])}")
    print(f"Normal MLE (mu,s2) = {normal_mle([2,4,4,4,5,5,7,9])}")


if __name__ == "__main__":
    main()
