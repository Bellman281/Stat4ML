//! Chapter 1 exercise 3 -- Online variance (Welford's algorithm) and
//! semi-supervised pseudo-label accuracy
//! Part II: Introduction to Statistical Learning
//!
//! HOMEWORK: implement each `todo!()`. ch01_text.tex Section 4 (Online
//! Learning) gives the running-mean update; this exercise extends it to
//! running VARIANCE via Welford's algorithm, and implements a toy
//! version of the "teacher generates pseudo-labels" idea from Section 3.
//!
//! Build & run: rustc --edition 2021 exercise03.rs -o /tmp/ex03 && /tmp/ex03
//! Reference solution: solutions/exercise03_solution.rs

#[derive(Clone, Copy)]
struct WelfordState {
    n: u64,
    mean: f64,
    m2: f64,
}

fn online_variance_update(state: WelfordState, new_x: f64) -> WelfordState {
    // TODO: n' = n+1; delta = new_x - mean; mean' = mean + delta/n';
    // delta2 = new_x - mean'; m2' = m2 + delta*delta2.
    todo!("online_variance_update")
}

fn variance_from_state(state: WelfordState) -> f64 {
    // TODO: population variance = m2 / n.
    todo!("variance_from_state")
}

fn pseudo_label_accuracy(teacher_preds: &[i32], true_labels: &[i32]) -> f64 {
    // TODO: fraction of teacher_preds matching true_labels.
    todo!("pseudo_label_accuracy")
}

/// Provided for you -- not part of this exercise.
fn semi_supervised_combined_accuracy(labeled_acc: f64, labeled_frac: f64, pseudo_acc: f64, unlabeled_frac: f64) -> f64 {
    labeled_frac * labeled_acc + unlabeled_frac * pseudo_acc
}

fn main() {
    let stream = [4.0, 6.0, 8.0, 2.0, 10.0];
    let mut state = WelfordState { n: 0, mean: 0.0, m2: 0.0 };
    for &x in &stream {
        state = online_variance_update(state, x);
    }
    let var = variance_from_state(state);
    println!("online variance = {var}  (expect 8.0)");

    let acc = pseudo_label_accuracy(&[1, 0, 1, 1, 0], &[1, 0, 0, 1, 0]);
    println!("pseudo_label_accuracy = {acc}  (expect 0.8)");

    let combined = semi_supervised_combined_accuracy(0.95, 0.1, acc, 0.9);
    println!("semi_supervised_combined_accuracy = {combined:.4}");
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_online_variance() {
        let stream = [4.0, 6.0, 8.0, 2.0, 10.0];
        let mut state = WelfordState { n: 0, mean: 0.0, m2: 0.0 };
        for &x in &stream {
            state = online_variance_update(state, x);
        }
        let var = variance_from_state(state);
        assert!((var - 8.0).abs() < 1e-9, "got {var}");
    }

    #[test]
    fn test_pseudo_label_accuracy() {
        let acc = pseudo_label_accuracy(&[1, 0, 1, 1, 0], &[1, 0, 0, 1, 0]);
        assert!((acc - 0.8).abs() < 1e-9, "got {acc}");
    }
}
