# === Stage 3: Хранилище в памяти ===
# Project: TeamRoster
from uuid import uuid4


class Player:
    def __init__(self, name, position, number, status):
        self.id = uuid4().hex
        self.name = name
        self.position = position
        self.number = number
        self.status = status

    def __repr__(self):
        return "Player(id={!r}, name={!r}, position={!r}, number={!r}, status={!r})".format(
            self.id, self.name, self.position, self.number, self.status)


class PlayerStore:
    def __init__(self):
        self._players = {}

    def add(self, player):
        if not isinstance(player, Player):
            raise TypeError("PlayerStore.add expects a Player instance")
        self._players[player.id] = player
        return player

    def get(self, player_id):
        player = self._players.get(player_id)
        if player is None:
            raise KeyError(player_id)
        return player

    def list(self):
        return list(self._players.values())
