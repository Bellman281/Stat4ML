# Contributing

Thanks for helping build this out! This repo grows by chapter, and every
chapter follows the same contract so the whole book stays consistent and
so readers always know what to expect. Please read `ROADMAP.md` first --
it lists exactly which chapters are missing and in what priority order,
so new contributions land where they're most useful instead of colliding.

## Repository layout

```
part1_statistics_foundations/        Part I  (Statistics Foundation for ML)
part2_intro_statistical_learning/    Part II (Introduction to Statistical Learning)
part3_advanced_statistical_learning/ Part III (Advanced Statistical Learning for DL)
  ch01_<slug>/
    README.md               chapter summary, status (PILOT/STUB), topic list
    ch01_text.tex            the chapter text (LaTeX)
    ch01_text.pdf            compiled chapter text
    figures/                 chapter figures
    source_slides/           original course slide PDF, preserved unmodified (if one exists)
    homework/                original homework PDF, preserved unmodified (if one exists)
    exercises/
      python/
        exercise01.py            working homework exercise
        exercise01_buggy.py      Rustlings-style broken exercise (reader fixes it)
        solutions/exercise01_solution.py
        exercise02.py, exercise02_buggy.py, solutions/exercise02_solution.py  (2nd exercise)
        exercise03.py, exercise03_buggy.py, solutions/exercise03_solution.py  (3rd exercise)
      r/            (same file pattern, .R)
      rust/         (same file pattern, .rs)
```

**Every chapter needs at least three exercises per language**, each
covering a different piece of the chapter's material (not three
variations on the same formula) -- see "Exercises" below.

Every chapter's original source PDF (when one exists) is preserved
unmodified under `source_slides/` -- never edit or delete it. Likewise for
a chapter's original homework PDF under `homework/`, when one exists. If a
chapter has no original slide deck, its `README.md` says so explicitly
(see `AUDIT.md` for the current list of these gaps) -- do not silently
invent a "source" for it.

**Two files remain at the repository root and are never to be moved into
a chapter: `PreReq0_Calculus.pdf`** (a general prerequisite, not tied to
any single chapter) **and `LICENSE`.** Every other original Stat4ML slide
deck and homework PDF has already been moved into its matching chapter's
`source_slides/`/`homework/` folder (see the mapping below) -- new
contributions should follow that same pattern rather than dropping loose
PDFs back at the root. `distributions.ipynb` has been retired in favor of
`part1_statistics_foundations/ch03_distribution_functions/distributions_demo.py`,
a plain Python script with the same plots/derivations.

| Original root file | Now lives at |
|---|---|
| `STAT4ML_Slide_1.pdf` | `part1_statistics_foundations/ch01_probability_theory_foundations/source_slides/` |
| `STAT4ML_Slide_2__Moments.pdf` | `part1_statistics_foundations/ch02_moments/source_slides/` |
| `STAT4ML_Slide_3__Distributions.pdf` | `part1_statistics_foundations/ch03_distribution_functions/source_slides/` |
| `STAT4ML_Slide_4__Multivariate_Dist_.pdf` | `part1_statistics_foundations/ch04_conditional_and_multivariate_distributions/source_slides/` |
| `STAT4ML_Slide_5__Convergence_in_Probability.pdf` | `part1_statistics_foundations/ch05_convergence_concepts/source_slides/` |
| `STAT4ML_Slide_6__MLE.pdf` | `part1_statistics_foundations/ch06_maximum_likelihood_estimation/source_slides/` |
| `STAT4ML_Slide_7__Bayesian_Estimation.pdf` | `part1_statistics_foundations/ch07_bayesian_estimation/source_slides/` |
| `PreReq1_Matrix_Calculus.pdf` | `part1_statistics_foundations/ch00_matrix_algebra_review/source_slides/` |
| `Homework1.pdf` | `part1_statistics_foundations/ch01_probability_theory_foundations/homework/` |
| `Homework2.pdf` | `part1_statistics_foundations/ch02_moments/homework/` |
| `Homework3.pdf` | `part1_statistics_foundations/ch03_distribution_functions/homework/` |
| `STAT4ML_Homework4.pdf` | `part1_statistics_foundations/ch04_conditional_and_multivariate_distributions/homework/` |
| `STAT4ML_Homework5.pdf` | `part1_statistics_foundations/ch05_convergence_concepts/homework/` |
| `STAT4ML_Homework6.pdf` | `part1_statistics_foundations/ch06_maximum_likelihood_estimation/homework/` |
| `STAT4ML_Homework7.pdf` | `part1_statistics_foundations/ch07_bayesian_estimation/homework/` |
| `distributions.ipynb` | retired; see `ch03_distribution_functions/distributions_demo.py` |

## Adding or finishing a chapter

Use `part1_statistics_foundations/ch00_matrix_algebra_review/`,
`ch01_probability_theory_foundations/`, and `ch02_moments/`, and
`part2_intro_statistical_learning/ch01_learning_algorithms_overview/`
as the reference examples -- they are the four fully-authored ("PILOT")
chapters this reorganization produced, and every new chapter should match
their shape.

1. **Text (`chNN_text.tex`).** Expanded textbook prose, not a slide
   outline: an abstract/intro paragraph, one `\section` per topic with
   real definitions/theorems/worked examples (not just bullet points),
   and a "Summary" + "Exercises" section at the end. If the chapter has a
   `source_slides/` PDF, ground the text in it, but expand -- don't just
   transcribe bullets. Start every chapter with
   `\usepackage{../../stat4ml_style}` (two directory levels up from
   `partX/chYY/`) instead of a bespoke preamble -- this is the
   shared style that gives every chapter its colored Definition/Theorem/
   Example boxes, `tryit`/`editorialnote`/`summarybox` callouts, and
   colored section headings; see `stat4ml_style.sty` itself for the
   full list of environments it provides. Compile locally before opening
   a PR:
   ```
   pdflatex -interaction=nonstopmode chNN_text.tex   # run twice, for cross-references
   ```
2. **Exercises.** Write **at least three exercises per language**, each
   exercising a different part of the chapter (not three variations on
   the same formula) -- see the pilot chapters for the range this can
   take (e.g. Chapter 0 covers core matrix ops, LU decomposition, and
   eigenvalues as three separate exercises). Each exercise is three files
   per language:
   - `exerciseNN.<ext>` -- a homework assignment with `TODO`/`raise
     NotImplementedError`/`todo!()` stubs the reader fills in themselves.
     Include a `main()`/demo at the bottom that exercises the functions.
   - `exerciseNN_buggy.<ext>` -- **fully implemented**, but with 2-5
     deliberate, clearly-commented bugs (`# BUG: ...`) that each break one
     specific, checkable property from the chapter text (an axiom, an
     identity, a formula). Include a test harness at the bottom
     (`run_tests()` in Python/R, `#[test]` functions in Rust) that the
     reader runs repeatedly while fixing bugs one at a time -- this is
     the "Rustlings" pattern this repo uses throughout. **Do not** let the
     reader need to write new logic here; the only job is finding and
     fixing the planted bugs.
   - `solutions/exerciseNN_solution.<ext>` -- the correct, complete
     reference implementation (used both as the homework answer key and
     as the "fixed" reference for the buggy exercise).

   Before opening a PR, actually run every file in all three languages
   for every exercise and confirm: the buggy version fails its tests (and
   the failure output clearly points at the bug), the solution
   passes/runs cleanly, and the homework stub raises/panics on its first
   unfinished TODO. See the pilot chapters' exercises for the exact
   test-harness pattern to copy.

   Language notes:
   - Python: standard library only unless the chapter genuinely needs
     something else (state it in the exercise docstring if so).
   - R: base R only (no non-base packages) unless the chapter needs one.
   - Rust: prefer a single `.rs` file with `#[cfg(test)] mod tests` and
     `rustc --edition 2021 --test file.rs -o /tmp/bin && /tmp/bin` so
     exercises don't require network access to fetch crates. If a
     chapter genuinely needs a crate, a small Cargo project is fine --
     just document the exact `cargo test` invocation in the chapter's
     README.

3. **Chapter `README.md`.** Update the status line from `STUB` to `PILOT`
   (or just `complete`, once more than three chapters exist) once you've
   filled in real content, and remove the "Editorial note" about missing
   content if you've resolved it.

## Fixing an audited bug or typo

`AUDIT.md` lists every typo/bug found in the original slide decks, plus a
few items flagged "verify against the rendered PDF" that need a second
pair of eyes before being treated as confirmed. If you fix one:
- Fix it in the new `chNN_text.tex` (never edit the original PDF under
  `source_slides/`).
- Update `AUDIT.md` to mark the item resolved (don't delete the entry --
  keep the history of what was found and fixed).

## Adding a whole new chapter that isn't in `ROADMAP.md` yet

Open an issue/discussion first with the proposed topic and where it fits
(which Part, which chapter number) -- `ROADMAP.md` is meant to be a living
document, and chapter numbering is easiest to keep consistent if it's
agreed before the text is written, not after.

## License

The whole repository is GPLv2 (see `LICENSE` and `ABOUT.md`). By
submitting a contribution you agree it is licensed under GPLv2 as well --
please don't port in GPL-incompatible code.

## Code of conduct

Be kind, be specific, and default to explaining *why* something is wrong
rather than just asserting that it is -- this repo's whole premise is
spoon-feeding the reader, and that applies to contributor discussion too.
