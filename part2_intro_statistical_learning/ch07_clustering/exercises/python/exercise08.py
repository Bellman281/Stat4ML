"""
Chapter 7 exercise -- the objective and its two optimal steps (Proof tier)
Part II: Introduction to Statistical Learning

HOMEWORK: implement each TODO using ch07_text.tex Section 2. You are
assembling one Lloyd iteration from its pieces: the objective J (inertia),
the optimal assignment (nearest centroid), and the optimal update (the mean).
The test then checks the chapter's claim -- one iteration cannot RAISE J.

Points are 2D lists [x, y]. Run with:  python3 exercise08.py
Reference solution: solutions/exercise08_solution.py
"""
# level: proof


def sq_dist(a, b):  # provided
    return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2


def inertia(data, labels, centroids):
    """Within-cluster sum of squares J = sum_i sq_dist(x_i, centroid of its label)."""
    raise NotImplementedError("TODO: inertia")


def assign_step(data, centroids):
    """Return the list of labels: each point's nearest-centroid index (the
    assignment that minimises J with centroids fixed)."""
    raise NotImplementedError("TODO: assign_step")


def update_step(data, labels, K):
    """Return K new centroids: each is the mean [x, y] of the points assigned
    to it (the centroids that minimise J with labels fixed)."""
    raise NotImplementedError("TODO: update_step")


def main():
    data = [[0, 0], [1, 0], [10, 0], [11, 0]]
    cents = [[0, 0], [5, 0]]
    labels = assign_step(data, cents)
    print("labels       :", labels)
    print("J before     :", inertia(data, labels, cents))
    cents2 = update_step(data, labels, 2)
    print("new centroids:", cents2)
    print("J after      :", inertia(data, labels, cents2))


if __name__ == "__main__":
    main()
