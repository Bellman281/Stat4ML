"""
Chapter 7 -- RUSTLINGS-STYLE EXERCISE (Python, Proof tier)
Part II: Introduction to Statistical Learning

Two deliberate bugs (inertia, assign_step). Fix one function at a time until
all tests pass. Do not edit run_tests().
"""
# level: proof


def sq_dist(a, b):
    return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2


def inertia(data, labels, centroids):
    # BUG: J sums the SQUARED distance to the assigned centroid. This uses the
    # centroid at index i (the point's position) instead of labels[i].
    return sum(sq_dist(data[i], centroids[labels[i]]) for i in range(len(data))) ** 0.5


def assign_step(data, centroids):
    # BUG: the assignment minimises distance, so it is argmin, not argmax
    # (ch07_text.tex Section 2, assignment step is optimal).
    return [max(range(len(centroids)), key=lambda k: sq_dist(x, centroids[k])) for x in data]


def update_step(data, labels, K):
    out = []
    for k in range(K):
        members = [data[i] for i in range(len(data)) if labels[i] == k]
        if members:
            n = len(members)
            out.append([sum(p[0] for p in members) / n, sum(p[1] for p in members) / n])
        else:
            out.append([0.0, 0.0])
    return out


def run_tests():
    failures = []

    def check(name, cond, detail=""):
        print(f"[{'PASS' if cond else 'FAIL'}] {name}{(': ' + detail) if detail else ''}")
        if not cond:
            failures.append(name)

    data = [[0, 0], [1, 0], [10, 0], [11, 0]]
    cents = [[0, 0], [5, 0]]

    labels = assign_step(data, cents)
    check("assign_step", labels == [0, 0, 1, 1], f"got {labels}")

    j_before = inertia(data, labels, cents)
    check("inertia", abs(j_before - 62.0) < 1e-9, f"got {j_before}")

    cents2 = update_step(data, labels, 2)
    j_after = inertia(data, labels, cents2)
    # the chapter's guarantee: one iteration cannot increase J
    check("monotone (J_after <= J_before)", j_after <= j_before + 1e-9,
          f"{j_after} <= {j_before}")
    check("J_after value", abs(j_after - 1.0) < 1e-9, f"got {j_after}")

    print()
    if failures:
        print(f"{len(failures)} test(s) FAILED: {failures}")
        raise SystemExit(1)
    print("All tests passed!")


if __name__ == "__main__":
    run_tests()
