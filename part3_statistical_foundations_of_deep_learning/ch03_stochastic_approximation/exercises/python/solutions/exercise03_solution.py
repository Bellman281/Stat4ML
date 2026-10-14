"""Chapter 3 -- reference solution (Core)."""
# level: core


def sgd_step(theta, grad, lr):
    return theta - lr * grad


def inverse_time_lr(t, a0):
    return a0 / t


def quad_grad(theta, target):
    return 2 * (theta - target)


def main():
    print("sgd_step        :", sgd_step(5.0, 2.0, 0.1))
    print("inverse_time_lr :", inverse_time_lr(4, 0.5))
    print("quad_grad       :", quad_grad(5.0, 3.0))
    th = sgd_step(5.0, quad_grad(5.0, 3.0), 0.25)
    print("one step toward 3:", th)


if __name__ == "__main__":
    main()
