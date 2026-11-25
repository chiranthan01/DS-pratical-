# Practical 04: Data Visualization

**Dataset:** Datasets/TeachingRatings.csv (463 rows, 13 columns)

**Aim:** Compare all records with unique instructors and visualize evaluation scores.

## Steps

1. Remove repeated instructors using the prof column.
2. Compare age statistics of all records and unique instructors.
3. Bar chart of average evaluation by division.
4. Scatter plots of age and evaluation, then by gender, then by gender and tenure.

## Results

- 463 records belong to 94 unique instructors.
- Mean age is 48.37 (all records) and 47.55 (unique instructors).
- Average evaluation: lower division 4.087, upper division 3.953.
- Correlation between age and evaluation is -0.052, so age has almost no effect.

## How to run

Open the notebook in the same folder with Jupyter Notebook or Google Colab and run all cells. The data is read from the Datasets folder one level above.

Required libraries: pandas, numpy, matplotlib, scipy.
