"""Chapter 8 -- reference solution (Core)."""
# level: core
import math


def sigmoid(z):
    return 1.0 / (1.0 + math.exp(-z))


def relu(z):
    return max(0.0, z)


def softmax(zs):
    m = max(zs)
    exps = [math.exp(z - m) for z in zs]
    tot = sum(exps)
    return [e / tot for e in exps]


def main():
    print("sigmoid(0) :", sigmoid(0))
    print("relu(-2,3) :", relu(-2), relu(3))
    print("softmax    :", softmax([1.0, 1.0, 1.0]))
    print("softmax big:", softmax([1000.0, 1000.0]))


if __name__ == "__main__":
    main()
