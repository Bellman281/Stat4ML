# About This Repository

## Mission

This repository aims to be a single, self-contained, **spoon-fed** source
for the statistics underlying modern machine learning, deep learning,
reinforcement learning, and large-language-model training. "Spoon-fed"
here means concretely: every chapter comes with (1) expanded prose text,
not just slide bullets, colorfully typeset (`book/stat4ml_style.sty`) so
definitions, theorems, examples, and editorial asides are visually easy
to tell apart at a glance; (2) at least three working homework exercises
per chapter in Python, R, and Rust, each covering a different piece of
the chapter's material; and (3) a Rustlings-style broken-code counterpart
for every exercise, in every language, so you learn each idea twice --
once building it, once debugging it. Nothing is assumed to be "obvious"
or left as pure self-study; where a step is non-trivial, it is worked out
in full rather than skipped.

## The trio of courses

This repo (`Stat4ML`) is the first of a three-part sequence taught by
Omid Safarzadeh:

1. **Statistics Foundation for ML** (`book/part1_statistics_foundations/`)
   -- probability theory, moments, distributions, convergence concepts,
   and estimation (MLE and Bayesian). Course text: Casella & Berger,
   *Statistical Inference*, 2nd ed.
2. **Introduction to Statistical Learning** (`book/part2_intro_statistical_learning/`)
   -- regression, regularization, resampling, unsupervised learning, EM,
   clustering, and the on-ramp into neural networks and Transformers.
   Course texts: James, Witten, Hastie & Tibshirani, *An Introduction to
   Statistical Learning*; Murphy, *Machine Learning: A Probabilistic
   Perspective*.
3. **Advanced Statistical Learning for DL** (`book/part3_advanced_statistical_learning/`)
   -- originally announced as "to be announced"; scaffolded here from the
   topic list already sketched for it (GANs, AutoML, NAS, advanced vision
   and language models, and more).

All three used to live as two separate repositories
(`Stat4ML` and `Intro_Statistical_Learning`); they have been merged into
this single repo so the whole sequence can be read, exercised, and
audited as one coherent book. The original flat files at the repository
root (slide PDFs, homework PDFs, prerequisite PDFs, the `distributions.ipynb`
notebook) are preserved exactly as they were -- nothing was deleted or
moved. The new `book/` tree is purely additive.

See `ROADMAP.md` for where the content goes from here: closing gaps in
the existing three parts, and two proposed new parts (Reinforcement
Learning, and Large Language Model Training) to complete the "statistics
for ML, DL, RL, and LLM training" ambition.

## Instructor

**Omid Safarzadeh**
LinkedIn: https://www.linkedin.com/in/omidsafarzadeh/
Instagram: @deepdatascientists

## Course registration

- STAT4ML (Statistics Foundation for ML), cohort 2: https://forms.gle/ZqLJLmv1K5nGVx3m7
- Introduction to Statistical Learning, cohort 1: https://forms.gle/gRqq7uCp9FVcqgej9

## License

The whole repository is licensed under the **GNU General Public License
v2 (GPLv2)** -- see `LICENSE` at the repo root.

Note on how this came to be: the two source repositories used different
licenses before this merge (`Stat4ML` was MIT; `Intro_Statistical_Learning`
was GPLv2). As of this reorganization, the instructor has relicensed the
combined repository as GPLv2 throughout, so `book/part1_statistics_foundations/`
(and the original `Stat4ML` files preserved at the repo root) are now
covered by the same GPLv2 terms as `book/part2_intro_statistical_learning/`
and `book/part3_advanced_statistical_learning/`. If you have a copy of the
old MIT-licensed `Stat4ML` from before this change, note that new
contributions and this merged repository going forward are GPLv2-only.
If you contribute new chapters, contribute them under GPLv2 as well.
