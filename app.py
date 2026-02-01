from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import joblib
import os
import re

# --------------------------------------------------
# Basic setup
# --------------------------------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__, static_folder="frontend")
CORS(app)

# --------------------------------------------------
# Load ML model & vectorizer
# --------------------------------------------------
model = joblib.load(os.path.join(BASE_DIR, "hate_model.pkl"))
vectorizer = joblib.load(os.path.join(BASE_DIR, "tfidf_vectorizer.pkl"))

# --------------------------------------------------
# Utility
# --------------------------------------------------
def clean_text(text: str) -> str:
    return re.sub(r"[^a-z\s]", "", text.lower())

# --------------------------------------------------
# Routes
# --------------------------------------------------
@app.route("/")
def home():
    return send_from_directory(app.static_folder, "index.html")

@app.route("/<path:filename>")
def serve_static(filename):
    return send_from_directory(app.static_folder, filename)

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    if not data or "text" not in data:
        return jsonify({"error": "No text provided"}), 400

    # Preprocess
    cleaned = clean_text(data["text"])

    # Model prediction
    vector = vectorizer.transform([cleaned])
    pred = model.predict(vector)[0]

    label_map = {
        0: "No Hate",
        1: "Offensive",
        2: "Hate"
    }

    return jsonify({
        "prediction": label_map[pred]
    })

# --------------------------------------------------
# Run
# --------------------------------------------------
if __name__ == "__main__":
    app.run(debug=True)
