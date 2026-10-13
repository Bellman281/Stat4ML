# Chapter 07: Clustering

_Part II -- Introduction to Statistical Learning_

Grouping unlabelled data. The chapter treats **k-means as coordinate descent**
on the within-cluster sum of squares -- which is exactly why "assign to nearest
centre" and "move each centre to its mean" can never make the clustering worse,
and why Lloyd's algorithm always stops. From there: soften the assignment and you
get the **Gaussian mixture** of Chapter 6; drop centres for density and you get
**DBSCAN**, which finds arbitrary shapes and labels outliers as noise.

## Contents

- `ch07_text.tex` / `ch07_text.pdf` -- the chapter text
- `figures/kmeans_panel.png` -- Lloyd iterations from a poor start + the
  monotone objective
- `source_slides/` -- the original lecture slides, exactly as taught
- `exercises/python/`, `exercises/r/` -- for each drill: the homework
  exercise, a **broken** copy to debug, and a reference solution, in both
  languages

## Topics

- The k-means objective (within-cluster sum of squares / inertia)
- k-means as coordinate descent; optimality of the assignment and update steps
- Lloyd's algorithm and its convergence; local minima, restarts, k-means++
- Gaussian mixture models as soft clustering (link to Chapter 6 / EM)
- DBSCAN: core points, density-reachability, noise

## Drills

| Exercise | Tier | What you build |
|---|---|---|
| `exercise07` | core | `sq_dist`, `nearest`, `centroid` -- the k-means primitives |
| `exercise08` | proof | `inertia`, `assign_step`, `update_step` -- one Lloyd step can't raise J |
| `exercise09` | research | `kpp_weight` (k-means++), `is_core` (DBSCAN), `silhouette` |

Run one: `python3 exercise08_buggy.py` and fix until the tests pass. Or drive
them from the repo-root runner: `python3 drill.py next --level master`.

## Source

Original slide deck preserved at `source_slides/Chapter_8__Clustrering.pdf`
(the original course's numbering drifted from the topic order used here).
