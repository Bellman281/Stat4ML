"""Chapter 10 -- reference solution (Research)."""
# level: research


def gaussian_score(x, mu, sigma2):
    return -(x - mu) / sigma2


def denoising_target(x_noisy, x_clean, sigma2):
    return -(x_noisy - x_clean) / sigma2


def langevin_step(x, score, step):
    return x + step * score


def main():
    print("gaussian_score  :", gaussian_score(3.0, 1.0, 2.0))
    print("denoising_target:", denoising_target(3.0, 1.0, 2.0))
    print("langevin_step   :", langevin_step(3.0, -1.0, 0.5))


if __name__ == "__main__":
    main()
