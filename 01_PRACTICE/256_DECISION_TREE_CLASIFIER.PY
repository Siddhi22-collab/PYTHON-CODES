from sklearn.tree import DecisionTreeClassifier

# Example dataset (Features: [Age, Hours Studied], Target: Pass/Fail)
X = [[18, 1], [19, 2], [20, 3], [21, 5], [22, 6], [23, 7], [24, 9]]
y = [0, 0, 0, 1, 1, 1, 1]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

dt_model = DecisionTreeClassifier()
dt_model.fit(X_train, y_train)

y_pred = dt_model.predict(X_test)
print("Predicted:", y_pred)
print("Accuracy:", accuracy_score(y_test, y_pred))
