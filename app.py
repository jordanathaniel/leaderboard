# app.py
from flask import Flask, jsonify, request
from models import Leaderboard

app = Flask(__name__)
lb = Leaderboard()

@app.route("/players", methods=["GET"])
def list_players():
    players = [p.to_dict() for p in lb.list_top(100)]
    return jsonify(players)

@app.route("/players", methods=["POST"])
def add_player():
    data = request.json or {}
    name = data.get("name")
    if not name:
        return jsonify({"error": "name is required"}), 400
    p = lb.add_player(name)
    return jsonify(p.to_dict()), 201

@app.route("/players/<int:pid>/score", methods=["POST"])
def add_score(pid):
    data = request.json or {}
    points = data.get("points", 0)
    try:
        p = lb.record_score(pid, int(points))
        return jsonify(p.to_dict())
    except ValueError:
        return jsonify({"error": "player not found"}), 404

if __name__ == "__main__":
    app.run(port=5000, debug=True)
