import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
import joblib

# ---------------- LOAD DATA ----------------
df = pd.read_csv("dataset/UNSW_NB15.csv")

print("Dataset shape:", df.shape)

# ---------------- CLEAN ----------------
df = df.replace([float("inf"), -float("inf")], 0)
df = df.fillna(0)

# ---------------- ENCODE CATEGORICAL ----------------
for col in df.select_dtypes(include=["object"]).columns:
    if col != "label":
        le = LabelEncoder()
        df[col] = le.fit_transform(df[col].astype(str))

# ---------------- SPLIT ----------------
X = df.drop("label", axis=1)
y = df["label"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# ---------------- MODEL ----------------
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# ---------------- SAVE ----------------
joblib.dump(model, "model.pkl")

print("🔥 Model trained & saved successfully")