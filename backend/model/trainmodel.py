import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer

from sklearn.model_selection import train_test_split

from sklearn.linear_model import LogisticRegression

from sklearn.pipeline import Pipeline

import joblib


# LOAD DATASET
columns = [
    "target",
    "ids",
    "date",
    "flag",
    "user",
    "text"
]


df = pd.read_csv(
    "sentiment.csv",
    encoding="latin-1",
    names=columns
)


# KEEP ONLY REQUIRED COLUMNS
df = df[["target", "text"]]


# CONVERT LABELS
# 0 = Negative
# 4 = Positive
df["target"] = df["target"].replace(4, 1)


# SMALLER DATA FOR FAST TRAINING
df = df.sample(20000)


# INPUT / OUTPUT
X = df["text"]

y = df["target"]


# SPLIT DATA
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# PIPELINE
model = Pipeline([

    (
        "tfidf",
        TfidfVectorizer(stop_words="english")
    ),

    (
        "classifier",
        LogisticRegression()
    )

])


# TRAIN MODEL
print("Training model...")

model.fit(X_train, y_train)


# ACCURACY
accuracy = model.score(X_test, y_test)

print("Accuracy:", accuracy)


# SAVE MODEL
joblib.dump(
    model,
    "communication_model.pkl"
)

print("Model saved successfully")