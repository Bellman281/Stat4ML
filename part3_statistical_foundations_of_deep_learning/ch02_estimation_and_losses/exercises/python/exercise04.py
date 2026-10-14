"""
Chapter 2 exercise -- the score function (Research tier)
Part III: Statistical Foundations of Deep Learning & RL

HOMEWORK: implement each TODO using ch02_text.tex Section 3. The score is the
gradient of the log-likelihood; the MLE is where the total score vanishes.
  - gaussian_score : d/dmu log N(y; mu, sigma^2) = (y - mu) / sigma^2.
  - bernoulli_score: d/dp log Bernoulli(y; p) = (y - p) / (p(1-p)).
  - mle_mean       : the mu solving sum_i (y_i - mu)/sigma^2 = 0, i.e. the mean.

The test checks that the total Gaussian score is zero at mle_mean.

Run with:  python3 exercise04.py
Reference solution: solutions/exercise04_solution.py
"""
# level: research


def gaussian_score(y, mu, sigma2):
    """Score of the Gaussian mean: (y - mu) / sigma2."""
    raise NotImplementedError("TODO: gaussian_score")


def bernoulli_score(y, p):
    """Score of the Bernoulli parameter: (y - p) / (p (1 - p))."""
    raise NotImplementedError("TODO: bernoulli_score")


def mle_mean(ys):
    """The mu that sets the total Gaussian score to zero (the sample mean)."""
    raise NotImplementedError("TODO: mle_mean")


def main():
    ys = [2.0, 4.0, 6.0]
    print("gaussian_score :", gaussian_score(3.0, 1.0, 2.0))
    print("bernoulli_score:", bernoulli_score(1, 0.5))
    mu = mle_mean(ys)
    print("mle_mean       :", mu)
    print("total score@mle:", sum(gaussian_score(y, mu, 1.0) for y in ys))


if __name__ == "__main__":
    main()
