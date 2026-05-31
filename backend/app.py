from flask import Flask, request
from flask_cors import CORS
import pandas as pd
from sklearn.linear_model import LinearRegression

app = Flask(__name__)
CORS(app)

data = pd.read_csv("../datasets/trust_data.csv")

X = data[["transparency","fairness","privacy","security","explainability"]]
y = data["trust_score"]

model = LinearRegression()
model.fit(X, y)

@app.route("/")
def home():
    return "AI Digital Trust Backend Running!"

@app.route("/predict")
def predict():

    transparency = float(request.args.get("transparency"))
    fairness = float(request.args.get("fairness"))
    privacy = float(request.args.get("privacy"))
    security = float(request.args.get("security"))
    explainability = float(request.args.get("explainability"))

    prediction = model.predict([[
        transparency,
        fairness,
        privacy,
        security,
        explainability
    ]])[0]

    return {"trust_score": round(prediction, 2)}

if __name__ == "__main__":
    app.run(debug=True)
