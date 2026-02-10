import os
import numpy as np
from PIL import Image
import joblib

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

from local_model import extract_all_features, features_to_vector


# ===============================
# ABSOLUTE PATH FIX (IMPORTANT)
# ===============================
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATASET_PATH = os.path.join(BASE_DIR, "dataset")

print("BASE DIR :", BASE_DIR)
print("DATASET  :", DATASET_PATH)

if not os.path.isdir(DATASET_PATH):
    raise Exception("❌ dataset folder NOT FOUND")


LABELS = {
    "Tomato_Late_Blight": 0,
    "Tomato_Early_Blight": 1,
    "Potato_Late_Blight": 2,
    "Potato_Early_Blight": 3,
    "Healthy": 4
}


X = []
y = []

print("\n📂 Reading dataset...\n")

for label_name, label_id in LABELS.items():
    folder = os.path.join(DATASET_PATH, label_name)
    print("➡ Checking:", folder)

    if not os.path.isdir(folder):
        raise Exception(f"❌ Folder missing: {folder}")

    for file in os.listdir(folder):
        img_path = os.path.join(folder, file)

        if not os.path.isfile(img_path):
            continue

        try:
            img = Image.open(img_path).convert("RGB")
        except:
            print("⚠ Skipped:", img_path)
            continue

        features = extract_all_features(img)
        vector = features_to_vector(features)

        X.append(vector)
        y.append(label_id)


X = np.array(X)
y = np.array(y)

print("\n🧠 Training model...\n")

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = RandomForestClassifier(
    n_estimators=200,
    max_depth=15,
    random_state=42
)

model.fit(X_train, y_train)

pred = model.predict(X_test)
acc = accuracy_score(y_test, pred)

print(f"\n✅ Training completed")
print(f"🎯 Accuracy: {acc*100:.2f}%")

joblib.dump(model, "ml_model.pkl")
print("💾 Model saved as ml_model.pkl")

print(model.predict(X_test[:5]))
print(y_test[:5])
