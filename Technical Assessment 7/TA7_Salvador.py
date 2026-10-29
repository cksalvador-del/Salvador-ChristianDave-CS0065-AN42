
from sklearn.tree import DecisionTreeClassifier, plot_tree
import matplotlib.pyplot as plt
import pandas as pd

# Dataset from Laboratory Activity 3
data = pd.DataFrame({
    "Size": ["Big", "Big", "Small", "Small",
             "Big", "Big", "Small", "Small"],
    "Orbit": ["Near", "Far", "Near", "Far",
              "Near", "Far", "Near", "Far"],
    "Habitable": ["Yes", "Yes", "Yes", "Yes",
                  "No", "No", "No", "No"],
    "Count": [20, 170, 139, 45, 130, 30, 11, 255]
})

# Convert categorical values into numbers
X = pd.get_dummies(data[["Size", "Orbit"]], dtype=int)
y = data["Habitable"]

# Train ID3-style decision tree using entropy
model = DecisionTreeClassifier(
    criterion="entropy",
    random_state=0
)

model.fit(X, y, sample_weight=data["Count"])

# Predict the two requested planets
planets = pd.DataFrame({
    "Size": ["Big", "Small"],
    "Orbit": ["Far", "Near"]
})

planets_encoded = pd.get_dummies(
    planets, dtype=int
).reindex(columns=X.columns, fill_value=0)

predictions = model.predict(planets_encoded)

print("Decision Tree Predictions:")
print("Big and Far:", predictions[0])
print("Small and Near:", predictions[1])

# Draw the decision tree
plt.figure(figsize=(12, 7))
plot_tree(
    model,
    feature_names=X.columns,
    class_names=model.classes_,
    filled=True,
    rounded=True,
    proportion=False
)
plt.title("ID3 Decision Tree - Planet Habitability")
plt.tight_layout()
plt.show()
