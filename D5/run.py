import matplotlib
matplotlib.use("Agg")
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.tree import DecisionTreeClassifier, plot_tree

data = load_wine()
X, y = data.data, data.target
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=3, stratify=y)
print("Train size:", len(X_train), "Test size:", len(X_test))

full = DecisionTreeClassifier(random_state=3).fit(X_train, y_train)
full_leaves, full_depth = full.get_n_leaves(), full.get_depth()
full_acc = full.score(X_test, y_test)
print(f"Full tree -> leaves: {full_leaves}, depth: {full_depth}, test acc: {full_acc:.4f}")

alphas = full.cost_complexity_pruning_path(X_train, y_train).ccp_alphas
print("Number of alphas:", len(alphas))
cv_acc, n_leaves = [], []
for a in alphas:
    clf = DecisionTreeClassifier(random_state=3, ccp_alpha=a)
    cv_acc.append(cross_val_score(clf, X_train, y_train, cv=5).mean())
    n_leaves.append(clf.fit(X_train, y_train).get_n_leaves())
cv_acc = np.array(cv_acc)
for a,c,l in zip(alphas,cv_acc,n_leaves):
    print(f"alpha={a:.6f}  cv_acc={c:.4f}  leaves={l}")

fig, ax1 = plt.subplots(figsize=(8, 5))
ax1.plot(alphas, cv_acc, marker="o", color="tab:blue", label="CV accuracy")
ax1.set_xlabel("ccp_alpha"); ax1.set_ylabel("5-fold CV accuracy")
ax2 = ax1.twinx()
ax2.plot(alphas, n_leaves, marker="s", color="tab:red", label="Number of leaves")
ax2.set_ylabel("Number of leaves")
h1, l1 = ax1.get_legend_handles_labels()
h2, l2 = ax2.get_legend_handles_labels()
ax1.legend(h1 + h2, l1 + l2, loc="best")
plt.title("CV accuracy and tree size vs ccp_alpha")
plt.savefig("/mnt/user-data/outputs/plot_cv_leaves.png", dpi=110, bbox_inches="tight")

best_idx = np.where(np.isclose(cv_acc, cv_acc.max()))[0][-1]
best_alpha = alphas[best_idx]
print(f"Best alpha: {best_alpha:.6f}, CV acc: {cv_acc[best_idx]:.4f}")
pruned = DecisionTreeClassifier(random_state=3, ccp_alpha=best_alpha).fit(X_train, y_train)
p_leaves, p_depth = pruned.get_n_leaves(), pruned.get_depth()
p_acc = pruned.score(X_test, y_test)
print(f"Pruned tree -> leaves: {p_leaves}, depth: {p_depth}, test acc: {p_acc:.4f}")
print("Leaves reduced by:", full_leaves - p_leaves, f"({(full_leaves - p_leaves) / full_leaves:.1%})")
print(f"Test accuracy change: {p_acc - full_acc:+.4f}")
plt.figure(figsize=(12, 7))
plot_tree(pruned, feature_names=data.feature_names, class_names=data.target_names, filled=True)
plt.title("Pruned decision tree (wine dataset)")
plt.savefig("/mnt/user-data/outputs/plot_pruned_tree.png", dpi=110, bbox_inches="tight")
