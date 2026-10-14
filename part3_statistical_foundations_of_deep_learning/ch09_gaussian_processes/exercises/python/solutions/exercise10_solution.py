"""Chapter 9 -- reference solution (Proof)."""
# level: proof


def gp_post_mean(k_star, k_11, sigma2, y):
    return k_star / (k_11 + sigma2) * y


def gp_post_var(k_ss, k_star, k_11, sigma2):
    return k_ss - k_star ** 2 / (k_11 + sigma2)


def main():
    print("gp_post_mean :", gp_post_mean(0.6, 1.0, 0.1, 2.0))
    print("gp_post_var  :", gp_post_var(1.0, 0.6, 1.0, 0.1))
    print("var at data  :", gp_post_var(1.0, 1.0, 1.0, 0.0))


if __name__ == "__main__":
    main()
