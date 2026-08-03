//! Chapter 1 exercise 2 -- K-means clustering (distance, assignment, and update)
//! Part II: Introduction to Statistical Learning
//!
//! HOMEWORK: implement each `todo!()`. This fleshes out "Unsupervised
//! Learning" (ch01_text.tex Section 2) into a full Lloyd's-algorithm
//! iteration: assign points to their nearest centroid, then recompute
//! each centroid as the mean of its assigned points.
//!
//! Build & run: rustc --edition 2021 exercise02.rs -o /tmp/ex02 && /tmp/ex02
//! Reference solution: solutions/exercise02_solution.rs

type Point = (f64, f64);

fn euclidean_dist2(p: Point, q: Point) -> f64 {
    // TODO: squared Euclidean distance.
    todo!("euclidean_dist2")
}

fn kmeans_assign(points: &[Point], centroids: &[Point]) -> Vec<usize> {
    // TODO: for each point, the index of the nearest centroid.
    todo!("kmeans_assign")
}

fn kmeans_update_centroids(points: &[Point], assignments: &[usize], k: usize) -> Vec<Point> {
    // TODO: recompute each centroid as the mean of its assigned points.
    todo!("kmeans_update_centroids")
}

/// Provided for you -- not part of this exercise.
fn kmeans_iterate(points: &[Point], mut centroids: Vec<Point>, n_iters: usize) -> Vec<Point> {
    for _ in 0..n_iters {
        let assignments = kmeans_assign(points, &centroids);
        centroids = kmeans_update_centroids(points, &assignments, centroids.len());
    }
    centroids
}

fn main() {
    println!("euclidean_dist2((0,0),(3,4)) = {}  (expect 25)", euclidean_dist2((0.0, 0.0), (3.0, 4.0)));

    let points = vec![(0.0, 0.0), (0.2, 0.1), (5.0, 5.0), (5.1, 4.9)];
    let centroids = vec![(1.0, 1.0), (4.0, 4.0)];
    let assignments = kmeans_assign(&points, &centroids);
    println!("assignments = {assignments:?}  (expect [0, 0, 1, 1])");

    let updated = kmeans_update_centroids(&points, &assignments, 2);
    println!("updated centroids = {updated:?}");

    let final_centroids = kmeans_iterate(&points, centroids, 5);
    println!("after 5 iterations = {final_centroids:?}");
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_dist() {
        assert!((euclidean_dist2((0.0, 0.0), (3.0, 4.0)) - 25.0).abs() < 1e-9);
    }

    #[test]
    fn test_assign() {
        let points = vec![(0.0, 0.0), (0.2, 0.1), (5.0, 5.0), (5.1, 4.9)];
        let centroids = vec![(1.0, 1.0), (4.0, 4.0)];
        assert_eq!(kmeans_assign(&points, &centroids), vec![0, 0, 1, 1]);
    }

    #[test]
    fn test_update() {
        let points = vec![(0.0, 0.0), (0.2, 0.1), (5.0, 5.0), (5.1, 4.9)];
        let updated = kmeans_update_centroids(&points, &[0, 0, 1, 1], 2);
        assert!((updated[0].0 - 0.1).abs() < 1e-9 && (updated[0].1 - 0.05).abs() < 1e-9);
        assert!((updated[1].0 - 5.05).abs() < 1e-9 && (updated[1].1 - 4.95).abs() < 1e-9);
    }
}
