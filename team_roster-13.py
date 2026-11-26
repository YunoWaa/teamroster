# === Stage 13: Поиск дубликатов ===
# Project: TeamRoster
import re
from typing import Dict, List, Tuple


def normalize_name(name: str) -> str:
    name = name.strip().lower()
    name = re.sub(r"[\s_-]+", " ", name)
    name = re.sub(r"[^a-zа-яё0-9\s]", "", name)
    name = re.sub(r"\s+", " ", name).strip()
    return re.sub(r"^"+r"(?:.+?\s)+", lambda m: m.group(0), name).strip()


def normalize_number(number) -> str:
    number = str(number).strip()
    number = re.sub(r"[^0-9]", "", number)
    return number


def normalize_position(position: str) -> str:
    position = str(position).strip().lower()
    position = position.replace(" ", "").replace("-", "").replace("_", "")
    return position


def normalize_status(status: str) -> str:
    status = str(status).strip().lower()
    status = status.replace(" ", "").replace("-", "").replace("_", "")
    return status


def normalize_player(player: dict) -> Tuple[str, str, str, str]:
    return (
        normalize_name(player.get("name", "")),
        normalize_position(player.get("position", "")),
        normalize_number(player.get("number", "")),
        normalize_status(player.get("status", "")),
    )


def find_duplicate_players(players: List[dict]) -> List[dict]:
    duplicates = []
    seen_keys: Dict[Tuple[str, str, str, str], List[int]] = {}

    for index, player in enumerate(players):
        key = normalize_player(player)
        if key not in seen_keys:
            seen_keys[key] = []
        seen_keys[key].append(index)

    for key, indices in seen_keys.items():
        if len(indices) > 1:
            duplicates.extend(players[i] for i in indices)

    return duplicates


def remove_duplicate_players(players: List[dict]) -> List[dict]:
    unique_players = []
    seen_keys: Dict[Tuple[str, str, str, str], None] = {}

    for player in players:
        key = normalize_player(player)
        if key not in seen_keys:
            seen_keys[key] = None
            unique_players.append(player)

    return unique_players
