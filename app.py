from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return """
    <h1>Hello from Docker! 🐳</h1>
    <p>This Flask application is running inside a container.</p>
    """


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)