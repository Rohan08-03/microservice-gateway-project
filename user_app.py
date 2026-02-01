from flask import Flask, jsonify

app = Flask(__name__)

users = [
    {"id": 1, "name": "Alice", "email": "alice@example.com"},
    {"id": 2, "name": "Bob", "email": "bob@example.com"},
    {"id": 3, "name": "Carol", "email": "carol@example.com"}
]

@app.route("/users")
def get_users():
    return jsonify({"service": "UserService", "data": users})

@app.route("/health")
def health():
    return jsonify({"status": "OK", "service": "UserService"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3001)