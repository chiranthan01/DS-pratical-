# Practical 10: Principal Component Analysis

**Dataset:** Datasets/wine.csv (178 rows, 14 columns)

**Aim:** Reduce the wine features to two principal components and show class separation.

## Steps

1. Describe the data and draw boxplots by class.
2. Draw a scatter plot and the covariance matrix.
3. Standardize the features.
4. Apply PCA with two components and plot the classes.

## Results

- PC1 explains 36.20% and PC2 explains 19.21% of the variance.
- Total variance explained by two components is 55.41%.
- The three wine classes separate clearly on the two components.

## How to run

Open the notebook in the same folder with Jupyter Notebook or Google Colab and run all cells. The data is read from the Datasets folder one level above.

Required libraries: pandas, numpy, matplotlib, scipy, seaborn, scikit-learn.
