"""Chapter 6 -- reference solution (Research)."""
# level: research
import math


def avg_negloglik(theta, data):
    n = len(data)
    return sum(0.5 * (x - theta) ** 2 + 0.5 * math.log(2 * math.pi) for x in data) / n


def fisher_scoring_mean(data, init, iters):
    n = len(data)
    theta = init
    for _ in range(iters):
        theta = theta + sum(x - theta for x in data) / n
    return theta


def naive_variance(data):
    return 1.0 / len(data)


def sandwich_variance(data, theta):
    n = len(data)
    B = sum((x - theta) ** 2 for x in data)
    return B / (n ** 2)


def main():
    data = [1.0, 3.0, 2.0, 6.0, 4.0, 2.0, 5.0, 1.0]
    th = fisher_scoring_mean(data, 0.0, 1)
    print(f"Fisher scoring theta = {th}")
    print(f"avg NLL at 3.0       = {avg_negloglik(3.0, data):.4f}")
    print(f"naive var (1/n)      = {naive_variance(data)}")
    print(f"sandwich var         = {sandwich_variance(data, th)}")


if __name__ == "__main__":
    main()
