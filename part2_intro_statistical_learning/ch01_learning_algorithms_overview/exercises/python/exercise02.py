"""
Chapter 1 exercise 2 -- K-means clustering (distance, assignment, and update)
Part II: Introduction to Statistical Learning

HOMEWORK: implement each TODO. This fleshes out the "Unsupervised
Learning" paradigm from ch01_text.tex Section 2 into a full (if tiny)
Lloyd's-algorithm iteration: assign each point to its nearest centroid,
then recompute each centroid as the mean of the points assigned to it.

Run with:  python3 exercise02.py
Reference solution: solutions/exercise02_solution.py
"""


def euclidean_dist2(p, q):
    """Squared Euclidean distance between 2D points p=(x,y), q=(x,y)."""
    # TODO
    raise NotImplementedError("TODO: euclidean_dist2")


def kmeans_assign(points, centroids):
    """For each point, return the index of the nearest centroid (by
    euclidean_dist2)."""
    # TODO
    raise NotImplementedError("TODO: kmeans_assign")


def kmeans_update_centroids(points, assignments, k):
    """Recompute each of the k centroids as the mean of the points
    currently assigned to it (assignments[i] is the cluster index of
    points[i]). Return a list of k (x,y) tuples."""
    # TODO
    raise NotImplementedError("TODO: kmeans_update_centroids")


def kmeans_iterate(points, centroids, n_iters):
    """Run n_iters rounds of assign -> update, returning the final list
    of centroids. Provided for you -- not part of this exercise."""
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
