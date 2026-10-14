"""Chapter 7 -- reference solution (Core)."""
# level: core
import math


def ucb_index(mean, n, t, c):
    return mean + math.sqrt(c * math.log(t) / n)


def argmax_index(values):
    return max(range(len(values)), key=lambda i: values[i])


def cumulative_regret(mu_star, chosen_means):
    return sum(mu_star - m for m in chosen_means)


def main():
    print("ucb_index         :", ucb_index(0.5, 4, 100, 2.0))
    print("argmax_index      :", argmax_index([1.0, 5.0, 3.0]))
    print("cumulative_regret :", cumulative_regret(1.0, [0.8, 0.9, 1.0]))


if __name__ == "__main__":
    main()
