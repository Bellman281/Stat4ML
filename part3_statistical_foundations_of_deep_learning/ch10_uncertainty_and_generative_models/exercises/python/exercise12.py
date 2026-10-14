"""
Chapter 10 exercise -- score matching and diffusion (Research tier)
Part III: Statistical Foundations of Deep Learning & RL

HOMEWORK: implement each TODO using ch10_text.tex Section 3.
  - gaussian_score    : the score of a Gaussian, grad_x log N(x; mu, sigma2)
                        = -(x - mu) / sigma2.
  - denoising_target  : the DSM regression target -(x_noisy - x_clean)/sigma2.
  - langevin_step     : one step UPHILL along the score, x + step * score.

Run with:  python3 exercise12.py
Reference solution: solutions/exercise12_solution.py
"""
# level: research


def gaussian_score(x, mu, sigma2):
    """Score of a Gaussian density: -(x - mu) / sigma2."""
    raise NotImplementedError("TODO: gaussian_score")


def denoising_target(x_noisy, x_clean, sigma2):
    """Denoising score-matching target: -(x_noisy - x_clean) / sigma2."""
    raise NotImplementedError("TODO: denoising_target")


def langevin_step(x, score, step):
    """One Langevin / gradient-ascent step along the score: x + step * score."""
    raise NotImplementedError("TODO: langevin_step")


def main():
    print("gaussian_score  :", gaussian_score(3.0, 1.0, 2.0))
    print("denoising_target:", denoising_target(3.0, 1.0, 2.0))
    print("langevin_step   :", langevin_step(3.0, -1.0, 0.5))


if __name__ == "__main__":
    main()
