from flask import Flask, render_template, request
import numpy as np
import pickle

app = Flask(__name__)

# Load your trained model
model = pickle.load(open("model.pkl", "rb"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    features = [float(x) for x in request.form.values()]
    prediction = model.predict([features])

    # Update the result logic
    if prediction[0] == 4:
        result = "Malignant"
    elif prediction[0] == 2:
        result = "Benign"
    else:
        result = "Unknown"

    return render_template("index.html", prediction_text=f"Prediction: {result}")

if __name__ == "__main__":
    app.run(debug=True)
