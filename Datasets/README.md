# Datasets

| File | Rows × columns | Used in | Source |
|---|---|---|---|
| `TeachingRatings.csv` | 463 × 13 | Practicals 1 | copied from the original repository |
| `StudentsPerformance.csv` | 1000 × 8 | Practicals 6, 8 | copied from the original repository |
| `wine.csv` | 178 × 14 | Practicals 2, 9 | scikit-learn `load_wine` (UCI Wine), class names added |
| `diabetes_progression.csv` | 442 × 12 | Practicals 3, 7 | scikit-learn `load_diabetes(scaled=False)`, target renamed `progression`, `patient_id` added |
| `breast_cancer.csv` | 569 × 31 | Practicals 4, 10 | scikit-learn `load_breast_cancer`, `diagnosis` label added |
| `iris.csv` | 150 × 5 | Practical 5 | scikit-learn `load_iris`, `species` label added |

All files are plain CSV so the scripts load them with `pd.read_csv`, exactly as you would with a downloaded dataset.
