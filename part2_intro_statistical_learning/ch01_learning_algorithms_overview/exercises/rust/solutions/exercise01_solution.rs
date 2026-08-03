//! Chapter 1 (Part II) -- reference solution (Rust).

fn simple_linear_regression_fit(xs: &[f64], ys: &[f64]) -> (f64, f64) {
    let n = xs.len() as f64;
    let xbar = xs.iter().sum::<f64>() / n;
    let ybar = ys.iter().sum::<f64>() / n;
    let num: f64 = xs.iter().zip(ys).map(|(x, y)| (x - xbar) * (y - ybar)).sum();
    let den: f64 = xs.iter().map(|x| (x - xbar).powi(2)).sum();
    let b1 = num / den;
    let b0 = ybar - b1 * xbar;
    (b0, b1)
}

fn predict(xs: &[f64], b0: f64, b1: f64) -> Vec<f64> {
    xs.iter().map(|x| b0 + b1 * x).collect()
}

fn mse(y_true: &[f64], y_pred: &[f64]) -> f64 {
    let n = y_true.len() as f64;
    y_true.iter().zip(y_pred).map(|(t, p)| (t - p).powi(2)).sum::<f64>() / n
}

fn kmeans_assign(points: &[(f64, f64)], centroids: &[(f64, f64)]) -> Vec<usize> {
    points
        .iter()
        .map(|&(px, py)| {
            centroids
                .iter()
                .map(|&(cx, cy)| ((px - cx).powi(2) + (py - cy).powi(2)).sqrt())
                .enumerate()
                .fold((0usize, f64::INFINITY), |(bi, bd), (i, d)| {
                    if d < bd {
                        (i, d)
                    } else {
                        (bi, bd)
                    }
                })
                .0
        })
        .collect()
}

fn online_mean_update(old_mean: f64, new_x: f64, n: u64) -> f64 {
    old_mean + (new_x - old_mean) / n as f64
}

fn main() {
    let xs = [1.0, 2.0, 3.0, 4.0, 5.0];
    let ys = [2.1, 3.9, 6.2, 7.8, 10.1];
    let (b0, b1) = simple_linear_regression_fit(&xs, &ys);
    let preds = predict(&xs, b0, b1);
    println!("Fitted line: y = {b0:.3} + {b1:.3} x, MSE = {:.4}", mse(&ys, &preds));

    let points = [(0.0, 0.0), (0.2, 0.1), (5.0, 5.0), (5.1, 4.9)];
    let centroids = [(0.0, 0.0), (5.0, 5.0)];
    println!("K-means assignments: {:?}", kmeans_assign(&points, &centroids));

    let stream = [4.0, 6.0, 8.0, 2.0, 10.0];
    let mut mean = stream[0];
    for (i, &x) in stream[1..].iter().enumerate() {
        let n = (i + 2) as u64;
        mean = online_mean_update(mean, x, n);
    }
    let batch_mean: f64 = stream.iter().sum::<f64>() / stream.len() as f64;
    println!("Final running mean = {mean:.4} (batch mean = {batch_mean:.4})");
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_simple_linear_regression_fit() {
        let xs = [1.0, 2.0, 3.0, 4.0, 5.0];
        let ys = [3.0, 5.0, 7.0, 9.0, 11.0];
        let (b0, b1) = simple_linear_regression_fit(&xs, &ys);
        assert!((b0 - 1.0).abs() < 1e-6);
        assert!((b1 - 2.0).abs() < 1e-6);
    }

    #[test]
    fn test_predict() {
        assert_eq!(predict(&[0.0, 1.0, 2.0], 1.0, 2.0), vec![1.0, 3.0, 5.0]);
    }

    #[test]
    fn test_mse() {
        assert!((mse(&[1.0, 2.0, 3.0], &[1.0, 2.0, 5.0]) - 4.0 / 3.0).abs() < 1e-9);
    }

    #[test]
    fn test_kmeans_assign() {
        let points = [(0.0, 0.0), (0.2, 0.1), (0.0, 5.0), (0.1, 5.1)];
        let centroids = [(0.0, 0.0), (0.0, 5.0)];
        assert_eq!(kmeans_assign(&points, &centroids), vec![0, 0, 1, 1]);
    }

    #[test]
    fn test_online_mean_update() {
        assert!((online_mean_update(5.0, 15.0, 2) - 10.0).abs() < 1e-9);
    }
}
