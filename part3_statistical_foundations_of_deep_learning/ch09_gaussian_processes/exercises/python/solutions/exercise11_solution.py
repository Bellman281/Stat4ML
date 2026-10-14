"""Chapter 9 -- reference solution (Research)."""
# level: research


def relu(z):
    return max(0.0, z)


def nn_features(x, W, b):
    return [relu(W[j] * x + b[j]) for j in range(len(W))]


def nngp_kernel(feat1, feat2):
    return sum(a * b for a, b in zip(feat1, feat2)) / len(feat1)


def main():
    W = [1.0, -1.0, 2.0]; b = [0.0, 0.0, 0.0]
    f1 = nn_features(1.0, W, b)
    f2 = nn_features(-1.0, W, b)
    print("relu(-2), relu(3):", relu(-2.0), relu(3.0))
    print("nn_features(1)   :", f1)
    print("nngp k(1,1)      :", nngp_kernel(f1, f1))
    print("nngp k(1,-1)     :", nngp_kernel(f1, f2))


if __name__ == "__main__":
    main()
