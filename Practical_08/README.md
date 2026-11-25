# Practical 08: Decision Tree Classifier

**Dataset:** Breast Cancer Wisconsin dataset from scikit-learn (569 rows, 30 features)

**Aim:** Build decision trees with entropy and Gini and find the best root node.

## Steps

1. Load the data and split it 80/20.
2. Compare entropy and Gini trees at different depths.
3. Evaluate the best model with a confusion matrix and report.
4. Plot the tree and feature importances.
5. Calculate information gain to find the best root node.

## Results

- Best model: entropy with maximum depth 3, test accuracy 94.74%.
- Best root node: worst radius <= 16.795 with information gain 0.5652.
- The calculated root matches the root chosen by scikit-learn.

## How to run

Open the notebook in the same folder with Jupyter Notebook or Google Colab and run all cells. The data is read from the Datasets folder one level above.

Required libraries: pandas, numpy, matplotlib, scipy, scikit-learn.
