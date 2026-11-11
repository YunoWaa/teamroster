# === Stage 4: Редактирование записей ===
# Project: TeamRoster
from dataclasses import dataclass, field, fields
from typing import Any


ALLOWED_PLAYER_FIELDS = {
    "name": str,
    "position": str,
    "number": int,
    "status": str,
}


@dataclass
class Player:
    name: str
    position: str
    number: int
    status: str


def _get_player(players: list[Player], player_id: int) -> Player | None:
    for player in players:
        if player.number == player_id:
            return player
    return None


def edit_player(players: list[Player], player_id: int, changes: dict[str, Any]) -> Player | None:
    target = _get_player(players, player_id)
    if target is None:
        return None

    allowed_fields = set(ALLOWED_PLAYER_FIELDS.keys())
    unknown_fields = set(changes.keys()) - allowed_fields
    if unknown_fields:
        raise ValueError(f"Недопустимые поля для редактирования: {', '.join(sorted(unknown_fields))}")

    invalid_types = {
        name: type(value).__name__
        for name, value in changes.items()
        if not isinstance(value, ALLOWED_PLAYER_FIELDS[name])
    }
    if invalid_types:
        raise ValueError(f"Неверный тип данных для полей: {invalid_types}")

    for name in allowed_fields:
        if name in changes:
            setattr(target, name, changes[name])

    return target


def build_edit_players_module() -> dict[str, Any]:
    return {
        "edit_player": edit_player,
        "Player": Player,
        "ALLOWED_PLAYER_FIELDS": ALLOWED_PLAYER_FIELDS,
        "get_player": _get_player,
    }
