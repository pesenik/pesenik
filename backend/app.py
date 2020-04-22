import os

from sanic import Sanic

app = Sanic()

PORT = int(os.env.get("PORT", "8000"))

@app.route("/")
def index():
    return 'Hello, World!'


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=PORT)
