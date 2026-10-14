"""
Chapter 3 exercise -- the SGD step and schedules (Core tier)
Part III: Statistical Foundations of Deep Learning & RL

HOMEWORK: implement each TODO using ch03_text.tex Sections 1-2.
  - sgd_step        : one Robbins-Monro / SGD update, theta - lr * grad.
  - inverse_time_lr : the schedule a_t = a0 / t.
  - quad_grad       : gradient of (theta - target)^2, which is 2(theta - target).

Run with:  python3 exercise03.py
Reference solution: solutions/exercise03_solution.py
"""
# level: core


def sgd_step(theta, grad, lr):
    """One SGD update: move against the gradient, theta - lr * grad."""
    raise NotImplementedError("TODO: sgd_step")


def inverse_time_lr(t, a0):
    """The 1/t schedule: a0 / t."""
    raise NotImplementedError("TODO: inverse_time_lr")


def quad_grad(theta, target):
    """Gradient of (theta - target)^2 with respect to theta."""
    raise NotImplementedError("TODO: quad_grad")


def main():
    print("sgd_step        :", sgd_step(5.0, 2.0, 0.1))
    print("inverse_time_lr :", inverse_time_lr(4, 0.5))
    print("quad_grad       :", quad_grad(5.0, 3.0))
    # one SGD step on (theta-3)^2 from theta=5 with lr=0.25
    th = sgd_step(5.0, quad_grad(5.0, 3.0), 0.25)
    print("one step toward 3:", th)


if __name__ == "__main__":
    main()
