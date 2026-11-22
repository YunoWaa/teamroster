# === Stage 11: Группировка ===
# Project: TeamRoster
from collections import Counter, defaultdict


class PositionGroup:
    def __init__(self, name, count):
        self.name = name
        self.count = count

    def __repr__(self):
        return f"PositionGroup({self.name!r}, {self.count})"


def group_players_by_position(players):
    counts = Counter(player["position"] for player in players)
    return [PositionGroup(position, count) for position, count in counts.items()]


def find_position_group(position_groups, position):
    for group in position_groups:
        if group.name == position:
            return group
    return None


def count_players_in_position(position_groups, position):
    group = find_position_group(position_groups, position)
    return group.count if group else 0


def build_position_groups(players):
    return group_players_by_position(players)


def summarize_team(players):
    position_groups = build_position_groups(players)
    total = len(players)
    summary = {
        "groups": position_groups,
        "total": total,
    }
    for group in position_groups:
        summary[group.name] = group.count
    return summary


if __name__ == "__main__":
    team = [
        {"name": "Иванов", "position": "Вратарь", "number": 1, "status": "active"},
        {"name": "Петров", "position": "Защитник", "number": 4, "status": "active"},
        {"name": "Сидоров", "position": "Защитник", "number": 5, "status": "active"},
        {"name": "Козлов", "position": "Полузащитник", "number": 8, "status": "active"},
        {"name": "Волков", "position": "Полузащитник", "number": 10, "status": "active"},
        {"name": "Орлов", "position": "Нападающий", "number": 9, "status": "active"},
        {"name": "Морозов", "position": "Нападающий", "number": 7, "status": "active"},
        {"name": "Смирнов", "position": "Нападающий", "number": 11, "status": "active"},
    ]

    groups = build_position_groups(team)
    for group in groups:
        print(f"{group.name}: {group.count}")

    summary = summarize_team(team)
    print("Всего игроков:", summary["total"])
