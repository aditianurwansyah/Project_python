import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

df = pd.read_csv('Teen_Mental_Health_Dataset.csv')
df_encoded = pd.get_dummies(df, columns=['gender', 'platform_usage', 'social_interaction_level'], drop_first=True)
x = df_encoded.drop('depression_label', axis=1)
y = df_encoded['depression_label']
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
rf_model.fit(X_train, y_train)
y_pred = rf_model.predict(X_test)

print("Akurasi model: {: .2f}%".format(accuracy_score(y_test, y_pred) * 100))
print("\nLaporan klasifikasi lengkap:\n")
print(classification_report(y_test, y_pred)) 