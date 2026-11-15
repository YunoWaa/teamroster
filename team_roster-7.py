# === Stage 7: Генерация идентификаторов ===
# Project: TeamRoster
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, List, Optional

PROJECT_PREFIX = "TR"
_id_counter = 0


class DuplicateIdError(Exception):
    pass


@dataclass
class Player:
    name: str
    position: str
    number: int
    status: str = "active"
    id: str = field(default="")

    def generate_id(self, pool: Optional[Dict[str, "Player"]] = None) -> str:
        global _id_counter
        base = f"{PROJECT_PREFIX}{_id_counter}"
        candidate = base
        attempts = 0
        while pool and candidate in pool:
            _id_counter += 1
            candidate = f"{PROJECT_PREFIX}{_id_counter}"
            attempts += 1
            if attempts > 1000:
                raise DuplicateIdError(f"Unable to generate unique id after {attempts} attempts")
        _id_counter += 1
        self.id = candidate
        return candidate


@dataclass
class Training:
    title: str
    date: str
    duration_minutes: int = 90
    id: str = field(default="")

    def generate_id(self, pool: Optional[Dict[str, "Training"]] = None) -> str:
        global _id_counter
        base = f"{PROJECT_PREFIX}{_id_counter}"
        candidate = base
        attempts = 0
        while pool and candidate in pool:
            _id_counter += 1
            candidate = f"{PROJECT_PREFIX}{_id_counter}"
            attempts += 1
            if attempts > 1000:
                raise DuplicateIdError(f"Unable to generate unique id after {attempts} attempts")
        _id_counter += 1
        self.id = candidate
        return candidate


class RosterRegistry:
    def __init__(self) -> None:
        self.players: Dict[str, Player] = {}
        self.trainings: Dict[str, Training] = {}

    def add_player(self, player: Player) -> str:
        player.generate_id(self.players)
        self.players[player.id] = player
        return player.id

    def add_training(self, training: Training) -> str:
        training.generate_id(self.trainings)
        self.trainings[training.id] = training
        return training.id

    def get_player(self, player_id: str) -> Optional[Player]:
        return self.players.get(player_id)

    def get_training(self, training_id: str) -> Optional[Training]:
        return self.trainings.get(training_id)
