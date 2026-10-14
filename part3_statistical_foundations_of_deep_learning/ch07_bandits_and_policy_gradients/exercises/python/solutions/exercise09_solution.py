"""Chapter 7 -- reference solution (Research)."""
# level: research


def logit_score(a, probs):
    return [(1.0 if i == a else 0.0) - probs[i] for i in range(len(probs))]


def advantage(R, baseline):
    return R - baseline


def grad_estimate(R, b, a, probs):
    return [(R - b) * s for s in logit_score(a, probs)]


def expected_grad(rewards, b, probs):
    n = len(probs)
    acc = [0.0] * n
    for a in range(n):
        g = grad_estimate(rewards[a], b, a, probs)
        for i in range(n):
            acc[i] += probs[a] * g[i]
    return acc


def main():
    probs = [0.2, 0.5, 0.3]; rewards = [1.0, 2.0, 3.0]
    print("advantage       :", advantage(3.0, 2.0))
    print("grad_estimate   :", grad_estimate(3.0, 2.0, 1, probs))
    print("E[grad], b=0    :", [round(x, 6) for x in expected_grad(rewards, 0.0, probs)])
    print("E[grad], b=5    :", [round(x, 6) for x in expected_grad(rewards, 5.0, probs)])


if __name__ == "__main__":
    main()
