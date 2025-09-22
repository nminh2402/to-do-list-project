from flask import Flask

app = Flask(__name__)

@app.get("/")
def home():
    return "Hello, To-Do (OOP + DB)!"

if __name__ == "__main__":
    app.run(debug=True)
