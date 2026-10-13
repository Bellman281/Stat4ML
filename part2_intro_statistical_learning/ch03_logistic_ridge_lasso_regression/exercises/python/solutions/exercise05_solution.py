"""Chapter 3 -- reference solution (Research)."""
# level: research
def l1_penalty(beta, lam):
    return lam * sum(abs(b) for b in beta)


def l2_penalty(beta, lam):
    return lam * sum(b * b for b in beta)


def elastic_net_penalty(beta, lam, alpha):
    return lam * (alpha * sum(abs(b) for b in beta) + (1 - alpha) * sum(b * b for b in beta))


def main():
    b = [1.0, -2.0, 3.0]
    print("l1          :", l1_penalty(b, 1.0))
    print("l2          :", l2_penalty(b, 1.0))
    print("elastic net :", elastic_net_penalty(b, 1.0, 0.25))


if __name__ == "__main__":
    main()
