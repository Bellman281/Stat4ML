"""Chapter 8 -- reference solution (Proof)."""
# level: proof
import math


def softmax(zs):
    m = max(zs)
    exps = [math.exp(z - m) for z in zs]
    tot = sum(exps)
    return [e / tot for e in exps]


def cross_entropy(p, y):
    return -sum(yk * math.log(pk) for pk, yk in zip(p, y))


def ce_grad(p, y):
    return [pk - yk for pk, yk in zip(p, y)]


def main():
    z = [2.0, 0.5, -1.0]
    y = [1.0, 0.0, 0.0]
    p = softmax(z)
    print("p         :", p)
    print("loss      :", cross_entropy(p, y))
    print("grad (p-y):", ce_grad(p, y))


if __name__ == "__main__":
    main()
