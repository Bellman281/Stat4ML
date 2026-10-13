"""Chapter 6 -- reference solution (Core)."""
# level: core
import math


def gaussian_pdf(x, mu, s2):
    return math.exp(-(x - mu) ** 2 / (2 * s2)) / math.sqrt(2 * math.pi * s2)


def responsibility(x, pis, mus, s2s, k):
    w = [pis[j] * gaussian_pdf(x, mus[j], s2s[j]) for j in range(len(pis))]
    return w[k] / sum(w)


def weighted_mean(xs, resps):
    return sum(r * xi for r, xi in zip(resps, xs)) / sum(resps)


def main():
    print("gaussian_pdf(0,0,1) :", gaussian_pdf(0.0, 0.0, 1.0))
    print("responsibility      :", responsibility(0.0, [0.5, 0.5], [-1, 1], [1, 1], 0))
    print("weighted_mean       :", weighted_mean([1, 2, 3], [1, 1, 0]))


if __name__ == "__main__":
    main()
