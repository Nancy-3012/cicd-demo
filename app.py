from flask import Flask

app = Flask(__name__)

COLOR = "crimson"
VERSION = "Version 2"


@app.route("/")
def home():
    return f"""
    <html>
      <body style="background-color:{COLOR}; color:white; font-family:Arial;
                   text-align:center; padding-top:120px;">
        <h1>Hello from my CI/CD pipeline!</h1>
        <h2>{VERSION}</h2>
      </body>
    </html>
    """


@app.route("/health")
def health():
    return {"status": "ok"}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)