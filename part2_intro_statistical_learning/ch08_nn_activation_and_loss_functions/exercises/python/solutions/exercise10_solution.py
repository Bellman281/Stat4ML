"""Chapter 8 -- reference solution (Research)."""
# level: research


def relu_grad(zs):
    return [1.0 if z > 0 else 0.0 for z in zs]


def grad_logits(p, y):
    return [pk - yk for pk, yk in zip(p, y)]


def grad_W(delta, x):
    return [[delta[i] * x[j] for j in range(len(x))] for i in range(len(delta))]


def main():
    print("relu_grad  :", relu_grad([-1.0, 0.0, 2.0]))
    p = [0.7, 0.2, 0.1]; y = [1.0, 0.0, 0.0]
    delta = grad_logits(p, y)
    print("grad_logits:", delta)
    print("grad_W     :", grad_W(delta, [1.0, 2.0]))


if __name__ == "__main__":
    main()
