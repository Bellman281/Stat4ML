"""
Chapter 9 -- RUSTLINGS-STYLE EXERCISE (Python, Research tier)
Part III: Statistical Foundations of Deep Learning & RL

Two deliberate bugs (relu, nngp_kernel). Fix one function at a time until all
tests pass. Do not edit run_tests().
"""
# level: research


def relu(z):
    # BUG: ReLU is max(0, z) -- it zeros NEGATIVES; this zeros positives.
    return min(0.0, z)


def nn_features(x, W, b):
    return [relu(W[j] * x + b[j]) for j in range(len(W))]


def nngp_kernel(feat1, feat2):
    # BUG: the NNGP kernel AVERAGES over units (divide by the count); this only
    # sums, so it grows with the hidden width instead of converging.
    return sum(a * b for a, b in zip(feat1, feat2))


def run_tests():
    failures = []

    def check(name, got, expected, tol=1e-9):
        if isinstance(expected, list):
            ok = len(got) == len(expected) and all(abs(a - b) < tol for a, b in zip(got, expected))
        else:
            ok = abs(got - expected) < tol
        print(f"[{'PASS' if ok else 'FAIL'}] {name}: got={got!r} expected={expected!r}")
        if not ok:
            failures.append(name)

    W = [1.0, -1.0, 2.0]; b = [0.0, 0.0, 0.0]
    check("relu_neg", relu(-2.0), 0.0)
    check("relu_pos", relu(3.0), 3.0)
    f1 = nn_features(1.0, W, b)
    f2 = nn_features(-1.0, W, b)
    check("nn_features", f1, [1.0, 0.0, 2.0])
    check("nngp_same", nngp_kernel(f1, f1), (1.0 + 0.0 + 4.0) / 3)
    check("nngp_cross", nngp_kernel(f1, f2), 0.0)

    print()
    if failures:
        print(f"{len(failures)} test(s) FAILED: {failures}")
        raise SystemExit(1)
    print("All tests passed!")


if __name__ == "__main__":
    run_tests()
