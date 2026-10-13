"""Chapter 4 -- reference solution (Proof)."""
# level: proof
def group_mean(means, weights):
    return sum(wi * mi for wi, mi in zip(weights, means))


def within_var(vars_, weights):
    return sum(wi * vi for wi, vi in zip(weights, vars_))


def between_var(means, weights):
    em2 = sum(wi * mi * mi for wi, mi in zip(weights, means))
    em = sum(wi * mi for wi, mi in zip(weights, means))
    return em2 - em * em


def total_variance(vars_, means, weights):
    return within_var(vars_, weights) + between_var(means, weights)


def main():
    w, m, v = [0.5, 0.5], [0.0, 10.0], [1.0, 1.0]
    print("E[X]        :", group_mean(m, w))
    print("within var  :", within_var(v, w))
    print("between var :", between_var(m, w))
    print("total var   :", total_variance(v, m, w))


if __name__ == "__main__":
    main()
