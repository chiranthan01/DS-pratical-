# Practical 05: Probability and Z-Test

**Dataset:** Datasets/TeachingRatings.csv (463 rows, 13 columns)

**Aim:** Find probabilities with the normal distribution and perform a two-tailed z-test.

## Steps

1. Find the mean and standard deviation of the evaluation score.
2. Find P(score > 4.5).
3. Find P(3.5 < score < 4.2).
4. Perform a two-tailed z-test for the basketball team sample.

## Results

- Mean 3.9983 and standard deviation 0.5549.
- P(score > 4.5) = 0.1829 (actual data 0.1706).
- P(3.5 < score < 4.2) = 0.4573 (actual data 0.3542).
- z = -1.4182, p-value = 0.1561, so we fail to reject H0.

## How to run

Open the notebook in the same folder with Jupyter Notebook or Google Colab and run all cells. The data is read from the Datasets folder one level above.

Required libraries: pandas, numpy, matplotlib, scipy.
