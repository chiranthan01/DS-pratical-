# Practical 06: Statistical Tests

**Dataset:** Datasets/TeachingRatings.csv (463 rows, 13 columns)

**Aim:** Apply t-test, ANOVA, chi-square test and correlation test.

## Steps

1. t-test of evaluation score between men and women.
2. ANOVA of beauty score across four age groups.
3. Chi-square test of tenure and gender.
4. Pearson correlation of evaluation and beauty score.

## Results

- t-test: t = 3.2667, p = 0.0012, reject H0.
- ANOVA: F = 13.782, p = 1.28e-08, reject H0.
- Chi-square: 2.2068, p = 0.1374, fail to reject H0.
- Correlation: r = 0.189, p = 4.25e-05, reject H0 (very weak positive).

## How to run

Open the notebook in the same folder with Jupyter Notebook or Google Colab and run all cells. The data is read from the Datasets folder one level above.

Required libraries: pandas, numpy, matplotlib, scipy.
