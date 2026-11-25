# Practical 07: Regression and ANOVA

**Dataset:** Datasets/TeachingRatings.csv (463 rows, 13 columns)

**Aim:** Fit regression models and a one-way ANOVA and interpret them.

## Steps

1. Regression of evaluation on gender.
2. One-way ANOVA of beauty score on age group.
3. Regression of evaluation on beauty score.

## Results

- Evaluation ~ gender: slope 0.168, R-squared 0.022, p = 0.00124, reject H0.
- ANOVA: F = 15.189, p = 4.09e-07, reject H0.
- Evaluation ~ beauty: slope 0.133, R-squared 0.036, p = 4.25e-05, reject H0.

## How to run

Open the notebook in the same folder with Jupyter Notebook or Google Colab and run all cells. The data is read from the Datasets folder one level above.

Required libraries: pandas, numpy, matplotlib, scipy.
