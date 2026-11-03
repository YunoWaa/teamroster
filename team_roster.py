# === Stage 1: Каркас модуля ===
# Project: TeamRoster
from dataclasses import dataclass, field
from enum import Enum


class PlayerStatus(str, Enum):
    ACTIVE = "active"
    INJURED = "injured"
    RESERVE = "reserve"


@dataclass
class Player:
    name: str
    position: str
    number: int
    status: PlayerStatus = PlayerStatus.ACTIVE


def make_demo_players() -> list[Player]:
    return [
        Player("Иванов", "защита", 4, PlayerStatus.ACTIVE),
        Player("Смирнов", "атака", 10, PlayerStatus.ACTIVE),
        Player("Петров", "вратарь", 1, PlayerStatus.INJURED),
        Player("Козлов", "хавбек", 8, PlayerStatus.RESERVE),
    ]


def main() -> None:
    players = make_demo_players()
    for player in players:
        print(
            f"{player.number:>3} {player.name:<10} "
            f"{player.position:<8} {player.status.value}"
        )


if __name__ == "__main__":
    main()
