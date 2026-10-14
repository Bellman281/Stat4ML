"""Chapter 5 -- reference solution (Research)."""
# level: research
import math


def perplexity(cross_entropy_nats):
    return math.exp(cross_entropy_nats)


def joint_entropy(joint):
    h = 0.0
    for row in joint:
        for pxy in row:
            if pxy > 0:
                h -= pxy * math.log(pxy)
    return h


def mutual_information(joint):
    nx, ny = len(joint), len(joint[0])
    px = [sum(joint[i]) for i in range(nx)]
    py = [sum(joint[i][j] for i in range(nx)) for j in range(ny)]
    mi = 0.0
    for i in range(nx):
        for j in range(ny):
            pxy = joint[i][j]
            if pxy > 0:
                mi += pxy * math.log(pxy / (px[i] * py[j]))
    return mi


def main():
    corr = [[0.5, 0.0], [0.0, 0.5]]
    indep = [[0.25, 0.25], [0.25, 0.25]]
    print("perplexity(log 5)   :", perplexity(math.log(5)))
    print("joint_entropy(corr) :", joint_entropy(corr))
    print("MI(correlated)      :", mutual_information(corr))
    print("MI(independent)     :", mutual_information(indep))


if __name__ == "__main__":
    main()
