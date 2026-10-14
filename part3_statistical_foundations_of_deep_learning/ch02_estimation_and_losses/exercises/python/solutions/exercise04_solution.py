"""Chapter 2 -- reference solution (Research)."""
# level: research


def gaussian_score(y, mu, sigma2):
    return (y - mu) / sigma2


def bernoulli_score(y, p):
    return (y - p) / (p * (1 - p))


def mle_mean(ys):
    return sum(ys) / len(ys)


def main():
    ys = [2.0, 4.0, 6.0]
    print("gaussian_score :", gaussian_score(3.0, 1.0, 2.0))
    print("bernoulli_score:", bernoulli_score(1, 0.5))
    mu = mle_mean(ys)
    print("mle_mean       :", mu)
    print("total score@mle:", sum(gaussian_score(y, mu, 1.0) for y in ys))


if __name__ == "__main__":
    main()
