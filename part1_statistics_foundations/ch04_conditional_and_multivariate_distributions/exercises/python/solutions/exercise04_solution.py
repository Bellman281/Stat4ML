"""Chapter 4 -- reference solution (Core)."""
# level: core
JOINT = {(0, 0): 0.3, (0, 1): 0.2, (1, 0): 0.1, (1, 1): 0.4}


def marginal_x_prob(joint, x0):
    return sum(p for (x, y), p in joint.items() if x == x0)


def conditional_y_prob(joint, y0, x0):
    return joint.get((x0, y0), 0.0) / marginal_x_prob(joint, x0)


def joint_covariance(joint):
    ex = sum(x * p for (x, y), p in joint.items())
    ey = sum(y * p for (x, y), p in joint.items())
    exy = sum(x * y * p for (x, y), p in joint.items())
    return exy - ex * ey


def main():
    print("P(X=0)        :", marginal_x_prob(JOINT, 0))
    print("P(Y=1 | X=0)  :", conditional_y_prob(JOINT, 1, 0))
    print("P(Y=1 | X=1)  :", conditional_y_prob(JOINT, 1, 1))
    print("Cov(X,Y)      :", joint_covariance(JOINT))


if __name__ == "__main__":
    main()
