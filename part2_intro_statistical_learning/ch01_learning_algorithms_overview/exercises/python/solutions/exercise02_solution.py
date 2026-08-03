"""Reference solution for exercise02.py (Chapter 1, Part II, Exercise 2)."""


def euclidean_dist2(p, q):
    return (p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2


def kmeans_assign(points, centroids):
    assignments = []
    for p in points:
        dists = [euclidean_dist2(p, c) for c in centroids]
        assignments.append(dists.index(min(dists)))
    return assignments


def kmeans_update_centroids(points, assignments, k):
    sums = [[0.0, 0.0] for _ in range(k)]
    counts = [0] * k
    for p, a in zip(points, assignments):
        sums[a][0] += p[0]
        sums[a][1] += p[1]
        counts[a] += 1
    return [(sums[i][0] / counts[i], sums[i][1] / counts[i]) for i in range(k)]


def kmeans_iterate(points, centroids, n_iters):
    for _ in range(n_iters):
        assignments = kmeans_assign(points, centroids)
        centroids = kmeans_update_centroids(points, assignments, len(centroids))
    return centroids


def main():
    print(f"euclidean_dist2((0,0),(3,4)) = {euclidean_dist2((0, 0), (3, 4))}  (expect 25)")

    points = [(0.0, 0.0), (0.2, 0.1), (5.0, 5.0), (5.1, 4.9)]
    centroids = [(1.0, 1.0), (4.0, 4.0)]
    assignments = kmeans_assign(points, centroids)
    print(f"assignments = {assignments}  (expect [0, 0, 1, 1])")

    updated = kmeans_update_centroids(points, assignments, 2)
    print(f"updated centroids = {updated}  (expect ~[(0.1, 0.05), (5.05, 4.95)])")

    final = kmeans_iterate(points, centroids, 5)
    print(f"after 5 iterations = {final}  (should have converged)")


if __name__ == "__main__":
    main()
