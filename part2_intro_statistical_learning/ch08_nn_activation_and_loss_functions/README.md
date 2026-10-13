# Chapter 08: Neural Networks -- Activations and Loss Functions

_Part II -- Introduction to Statistical Learning_

Stacking the linear models of the earlier chapters and bending them with
nonlinearities. The chapter assembles the three pieces that make a network
trainable -- **activations**, the **loss**, and **backpropagation** -- around
one centrepiece: the softmax cross-entropy gradient collapses to a clean
`p - y`, and backprop is just that derivative reused layer by layer.

## Contents

- `ch08_text.tex` / `ch08_text.pdf` -- the chapter text
- `figures/nn_panel.png` -- activation functions, a 2-12-2 net's learned
  decision boundary on two half-moons, and the cross-entropy loss falling
- `source_slides/` -- the original lecture slides, exactly as taught
- `exercises/python/`, `exercises/r/` -- for each drill: the homework
  exercise, a **broken** copy to debug, and a reference solution, in both
  languages

## Topics

- Layers as affine map + activation; why a nonlinearity is required
- Activations: sigmoid, tanh, ReLU; softmax (and numerical stability)
- Loss: MSE, cross-entropy
- The softmax cross-entropy gradient, dL/dz = p - y (with proof)
- Backpropagation: the chain rule as a backward pass

## Drills

| Exercise | Tier | What you build |
|---|---|---|
| `exercise08` | core | `sigmoid`, `relu`, stable `softmax` |
| `exercise09` | proof | `cross_entropy`, `ce_grad`; the identity dL/dz = p - y vs finite differences |
| `exercise10` | research | `relu_grad`, `grad_logits`, `grad_W` -- one backward pass, checked against numeric dL/dW |

Run one: `python3 exercise09_buggy.py` and fix until the tests pass. Or drive
them from the repo-root runner: `python3 drill.py next --level phd`.

## Source

Original slide deck preserved at
`source_slides/Chapter_9__Activation_and_loss_functions.pdf` (the original
course's numbering drifted from the topic order used here).
