# Practical 09: K-Nearest Neighbours

**Dataset:** Datasets/iris.csv (150 rows, 5 columns)

**Aim:** Classify iris species with KNN and find the best K.

## Steps

1. Explore the data and split it 80/20.
2. Standardize the features.
3. Train KNN with K = 5 and evaluate it.
4. Find the error rate for K = 1 to 30 using cross-validation.
5. Train the final model and plot decision regions.

## Results

- K = 5 gives 93.33% accuracy.
- Best K is 5 with cross-validation error 0.0333.
- With petal length and width only, accuracy is 96.67%.

## How to run

Open the notebook in the same folder with Jupyter Notebook or Google Colab and run all cells. The data is read from the Datasets folder one level above.

Required libraries: pandas, numpy, matplotlib, scipy, seaborn, scikit-learn.
