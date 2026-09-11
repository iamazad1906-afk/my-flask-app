from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return """
    <html>
        <head>
            <title>My Flask App</title>
        </head>

        <body>
            <h1>Hello! 👋</h1>
            <p>My Flask application is running.</p>
        </body>
    </html>
    """


if __name__ == "__main__":
    app.run()
