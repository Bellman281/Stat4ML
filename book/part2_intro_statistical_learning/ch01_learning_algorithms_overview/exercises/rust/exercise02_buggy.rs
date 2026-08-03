//! Chapter 1 -- RUSTLINGS-STYLE EXERCISE (Rust edition), Exercise 2
//! Part II: Introduction to Statistical Learning
//!
//! Three deliberate bugs are hiding below (in euclidean_dist2,
//! kmeans_assign, and kmeans_update_centroids). Find and fix each one
//! so every `#[test]` passes. Do not edit the tests.
//!
//! Build & run: rustc --edition 2021 --test exercise02_buggy.rs -o /tmp/ex02_buggy_test && /tmp/ex02_buggy_test

type Point = (f64, f64);

fn euclidean_dist2(p: Point, q: Point) -> f64 {
    // BUG: subtracts instead of adds the two squared terms.
    (p.0 - q.0).powi(2) - (p.1 - q.1).powi(2)
}

fn kmeans_assign(points: &[Point], centroids: &[Point]) -> Vec<usize> {
    // BUG: picks the FARTHEST centroid (max distance) instead of the
    // nearest one.
    points
        .iter()
        .map(|&p| {
            let mut best = 0;
            let mut best_d = f64::NEG_INFINITY;
            for (i, &c) in centroids.iter().enumerate() {
                let d = euclidean_dist2(p, c);
                if d > best_d {
                    best_d = d;
                    best = i;
                }
            }
            best
        })
        .collect()
}

fn kmeans_update_centroids(points: &[Point], assignments: &[usize], k: usize) -> Vec<Point> {
    // BUG: ignores `assignments` -- every centroid becomes the mean of
    // ALL points.
    let _ = assignments;
    let n = points.len() as f64;
    let mean_x = points.iter().map(|p| p.0).sum::<f64>() / n;
    let mean_y = points.iter().map(|p| p.1).sum::<f64>() / n;
    vec![(mean_x, mean_y); k]
}

fn kmeans_iterate(points: &[Point], mut centroids: Vec<Point>, n_iters: usize) -> Vec<Point> {
    for _ in 0..n_iters {
        let assignments = kmeans_assign(points, &centroids);
        centroids = kmeans_update_centroids(points, &assignments, centroids.len());
    }
    centroids
}

fn main() {
    println!("euclidean_dist2((0,0),(3,4)) (buggy) = {}", euclidean_dist2((0.0, 0.0), (3.0, 4.0)));
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_dist() {
        assert!((euclidean_dist2((0.0, 0.0), (3.0, 4.0)) - 25.0).abs() < 1e-9, "got {}", euclidean_dist2((0.0, 0.0), (3.0, 4.0)));
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
        assert!((updated[0].0 - 0.1).abs() < 1e-9 && (updated[0].1 - 0.05).abs() < 1e-9, "got {:?}", updated);
        assert!((updated[1].0 - 5.05).abs() < 1e-9 && (updated[1].1 - 4.95).abs() < 1e-9, "got {:?}", updated);
    }
}
