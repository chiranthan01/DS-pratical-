# Practical 12: Metropolis Algorithm and Deterministic Model

**Dataset:** Part A: coin flip example (21 heads in 30 flips). Part B: Datasets/sunspots.csv

**Aim:** Part A: implement the Metropolis algorithm. Part B: build a deterministic model of the sunspot cycle.

## Steps

1. Part A: write the Metropolis algorithm and sample the posterior of a coin probability.
2. Compare the samples with the exact Beta(22, 10) posterior.
3. Compare different step sizes and acceptance rates.
4. Part B: fit the equation count = A x sin^2(pi x (t - t0) / P) to the sunspot data.
5. Plot the fit and residuals and forecast the next five years.

## Results

- All numbers are printed in the notebook after each step in the Result lines.
- The sampled mean and standard deviation match the exact Beta posterior.
- A moderate step width gives the best balance of acceptance rate and movement.
- The deterministic model follows the 11-year cycle but not the change in peak height.

## How to run

Open the notebook in the same folder with Jupyter Notebook or Google Colab and run all cells. The data is read from the Datasets folder one level above.

Required libraries: pandas, numpy, matplotlib, scipy.
