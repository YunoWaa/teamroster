# === Stage 14: Массовое обновление ===
# Project: TeamRoster
from dataclasses import dataclass, field
from datetime import date


@dataclass
class Player:
    name: str
    position: str
    number: int
    status: str = "active"

    def apply_change(self, new_value, old_value):
        self._old = self.value
        self.value = new_value
        self._changed = True

    @property
    def value(self):
        return self.status

    @value.setter
    def value(self, new_value):
        self.status = new_value

    @property
    def old_value(self):
        return getattr(self, "_old", self.status)

    @property
    def changed(self):
        return getattr(self, "_changed", False)


@dataclass
class TrainingSession:
    title: str
    date: date
    description: str = ""


class TeamRoster:
    def __init__(self):
        self.players = []

    def add_player(self, player):
        self.players.append(player)

    def select_players(self, predicate):
        selected = [p for p in self.players if predicate(p)]
        return selected

    def preview_changes(self, players, field_name, new_values):
        print(f"Предварительный просмотр изменений ({len(players)} игроков):")
        for player in players:
            old = getattr(player, field_name)
            new = new_values.get(player, old)
            if old != new:
                print(f"  {player.name} (#{player.number}): "
                      f"{old} -> {new}")
            else:
                print(f"  {player.name} (#{player.number}): без изменений")
        return players

    def bulk_update(self, players, field_name, new_values):
        updated = 0
        for player in players:
            old = getattr(player, field_name)
            new = new_values.get(player, old)
            if old != new:
                setattr(player, field_name, new)
                updated += 1
        return updated


if __name__ == "__main__":
    team = TeamRoster()
    team.add_player(Player("Иванов", "защита", 3))
    team.add_player(Player("Смирнов", "атака", 10))
    team.add_player(Player("Козлов", "защита", 4))

    selected = team.select_players(lambda p: p.position == "защита")

    status_updates = {
        selected[0]: "injured",
        selected[2]: "suspended",
    }

    team.preview_changes(selected, "status", status_updates)

    updated_count = team.bulk_update(selected, "status", status_updates)
    print(f"Обновлено статусов: {updated_count}")

    for player in team.players:
        print(f"  {player.name} (#{player.number}): {player.status}")
