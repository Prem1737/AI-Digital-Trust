from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "AI Digital Trust Backend Running!"

if __name__ == "__main__":
    app.run(debug=True)