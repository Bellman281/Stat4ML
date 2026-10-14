"""
Chapter 9 exercise -- the NNGP kernel (Research tier)
Part III: Statistical Foundations of Deep Learning & RL

HOMEWORK: implement each TODO using ch09_text.tex Section 3. A wide random net's
covariance is the per-unit expectation E[phi(w x + b) phi(w x' + b)], which we
estimate by averaging over the hidden units.
  - relu         : max(0, z).
  - nn_features  : [ relu(W[j]*x + b[j]) for each unit j ].
  - nngp_kernel  : mean over units of feat1[j] * feat2[j].

Run with:  python3 exercise11.py
Reference solution: solutions/exercise11_solution.py
"""
# level: research


def relu(z):
    """max(0, z)."""
    raise NotImplementedError("TODO: relu")


def nn_features(x, W, b):
    """Hidden activations [relu(W[j]*x + b[j]) for each unit j]."""
    raise NotImplementedError("TODO: nn_features")


def nngp_kernel(feat1, feat2):
    """Monte Carlo NNGP kernel: mean over units of feat1[j] * feat2[j]."""
    raise NotImplementedError("TODO: nngp_kernel")


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
