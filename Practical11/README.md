# Practical 11: Sunspot Data with a Gamma Model

**Dataset:** Datasets/sunspots.csv (monthly mean total sunspot number, January 1749 to November 2018)

**Aim:** Model sunspot counts with a gamma distribution and estimate its parameters a and b with a Metropolis sampler.

## Steps

1. Plot the monthly sunspot numbers over the years.
2. Cut the data into 12-year blocks that reset every 12 years and fit a gamma shaped curve to the average block.
3. Draw the histogram of sunspot counts with a gamma fit.
4. Run the Metropolis sampler from a = 4 and b = 10 for the first 50 samples, all samples and the last 50 samples.
5. Plot the traces of a and b, drop the burn-in and draw their histograms.
6. Predict a and b with 95% intervals and predict new monthly counts.

## Results

- All numbers are printed in the notebook after each step in the Result lines.
- The histogram is right skewed and matches a gamma distribution.
- More data gives a narrower posterior for a and b.
- The sampler uses +1 on the counts because a gamma distribution cannot take the value 0.

## How to run

Open the notebook in the same folder with Jupyter Notebook or Google Colab and run all cells. The data is read from the Datasets folder one level above.

Required libraries: pandas, numpy, matplotlib, scipy.
