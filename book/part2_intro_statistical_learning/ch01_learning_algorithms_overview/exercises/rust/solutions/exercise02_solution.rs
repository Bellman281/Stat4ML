//! Reference solution for exercise02.rs (Chapter 1, Part II, Exercise 2)

type Point = (f64, f64);

fn euclidean_dist2(p: Point, q: Point) -> f64 {
    (p.0 - q.0).powi(2) + (p.1 - q.1).powi(2)
}

fn kmeans_assign(points: &[Point], centroids: &[Point]) -> Vec<usize> {
    points
        .iter()
        .map(|&p| {
            let mut best = 0;
            let mut best_d = f64::INFINITY;
            for (i, &c) in centroids.iter().enumerate() {
                let d = euclidean_dist2(p, c);
                if d < best_d {
                    best_d = d;
                    best = i;
                }
            }
            best
        })
        .collect()
}

fn kmeans_update_centroids(points: &[Point], assignments: &[usize], k: usize) -> Vec<Point> {
    let mut sums = vec![(0.0, 0.0); k];
    let mut counts = vec![0usize; k];
    for (&p, &a) in points.iter().zip(assignments) {
        sums[a].0 += p.0;
        sums[a].1 += p.1;
        counts[a] += 1;
    }
    (0..k).map(|i| (sums[i].0 / counts[i] as f64, sums[i].1 / counts[i] as f64)).collect()
}

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
