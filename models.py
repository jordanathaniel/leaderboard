# models.py
import json
from typing import List

class Player:
    def __init__(self, player_id: int, name: str, score: int = 0):
        self.id = player_id
        self.name = name
        self.score = score

    def to_dict(self):
        return {"id": self.id, "name": self.name, "score": self.score}

class Leaderboard:
    def __init__(self, storage_file="data.json"):
        self.storage_file = storage_file
        self.players: List[Player] = []
        self._load()

    def _load(self):
        try:
            with open(self.storage_file, "r") as f:
                items = json.load(f)
        except Exception:
            items = []
        self.players = [Player(p["id"], p["name"], p["score"]) for p in items]

    def _save(self):
        with open(self.storage_file, "w") as f:
            json.dump([p.to_dict() for p in self.players], f, indent=2)

    def add_player(self, name: str) -> Player:
        next_id = max([p.id for p in self.players], default=0) + 1
        p = Player(next_id, name)
        self.players.append(p)
        self._save()
        return p

    def record_score(self, player_id: int, delta: int):
        for p in self.players:
            if p.id == player_id:
                p.score += delta
                self._save()
                return p
        raise ValueError("Player not found")

    def list_top(self, n=10):
        return sorted(self.players, key=lambda x: x.score, reverse=True)[:n]

    def get_player(self, player_id: int):
        for p in self.players:
            if p.id == player_id:
                return p
        return None
