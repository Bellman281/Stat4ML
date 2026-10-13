"""Chapter 6 -- reference solution (Proof)."""
# level: proof
import math


def log_evidence(joint):
    return math.log(sum(joint))


def elbo(q, joint):
    return sum(qz * (math.log(jz) - math.log(qz)) for qz, jz in zip(q, joint))


def kl(q, p):
    return sum(qz * math.log(qz / pz) for qz, pz in zip(q, p))


def main():
    joint = [0.2, 0.3]; q = [0.5, 0.5]; post = [0.4, 0.6]
    print("log_evidence :", log_evidence(joint))
    print("elbo         :", elbo(q, joint))
    print("kl           :", kl(q, post))
    print("elbo + kl    :", elbo(q, joint) + kl(q, post))


if __name__ == "__main__":
    main()
