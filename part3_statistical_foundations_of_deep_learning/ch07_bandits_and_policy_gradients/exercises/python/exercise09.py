"""
Chapter 7 exercise -- baselines as control variates (Research tier)
Part III: Statistical Foundations of Deep Learning & RL

HOMEWORK: implement each TODO using ch07_text.tex Section 3. A baseline b is
subtracted from the reward; because the score is mean-zero, this changes the
estimator's variance but NOT its expectation.
  - advantage       : R - baseline.
  - grad_estimate   : (R - b) * logit_score(a, probs)  (vector).
  - expected_grad   : sum_a p_a * grad_estimate(rewards[a], b, a, probs), the
                      true gradient -- which must not depend on b.

The test checks that expected_grad is identical for two different baselines.

Run with:  python3 exercise09.py
Reference solution: solutions/exercise09_solution.py
"""
# level: research


def logit_score(a, probs):  # provided (from Section 2)
    return [(1.0 if i == a else 0.0) - probs[i] for i in range(len(probs))]


def advantage(R, baseline):
    """R - baseline."""
    raise NotImplementedError("TODO: advantage")


def grad_estimate(R, b, a, probs):
    """(R - b) * logit_score(a, probs), element-wise."""
    raise NotImplementedError("TODO: grad_estimate")


def expected_grad(rewards, b, probs):
    """sum_a probs[a] * grad_estimate(rewards[a], b, a, probs) (vector)."""
    raise NotImplementedError("TODO: expected_grad")


def main():
    probs = [0.2, 0.5, 0.3]; rewards = [1.0, 2.0, 3.0]
    print("advantage       :", advantage(3.0, 2.0))
    print("grad_estimate   :", grad_estimate(3.0, 2.0, 1, probs))
    print("E[grad], b=0    :", [round(x, 6) for x in expected_grad(rewards, 0.0, probs)])
    print("E[grad], b=5    :", [round(x, 6) for x in expected_grad(rewards, 5.0, probs)])


if __name__ == "__main__":
    main()
