# Practical 01: Matrix Operations and Encoding

**Dataset:** Datasets/StudentsPerformance.csv (1000 rows, 8 columns)

**Aim:** Convert scores to NumPy arrays, perform matrix operations and apply one-hot encoding.

## Steps

1. Load the data and check its structure.
2. Convert the three score columns to an array and find shape, size and dimensions.
3. Select the first four rows of math and reading scores and split them into matrices A and B.
4. Perform addition, subtraction, element-wise product, matrix product, determinant, inverse and transpose.
5. Apply one-hot encoding to the five categorical columns.

## Results

- Array shape is (1000, 3), size 3000, 2 dimensions.
- A + B = [[162, 167], [116, 147]]
- A - B = [[-18, -23], [22, 33]]
- Matrix product = [[9864, 10944], [10440, 11685]]
- Determinant of A is 1512, so the inverse exists.
- One-hot encoding increases the columns from 8 to 20.

## How to run

Open the notebook in the same folder with Jupyter Notebook or Google Colab and run all cells. The data is read from the Datasets folder one level above.

Required libraries: pandas, numpy, matplotlib, scipy.
