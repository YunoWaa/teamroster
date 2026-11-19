# === Stage 9: Сортировка записей ===
# Project: TeamRoster
def sort_players_by_name(players, descending=False):
    key = lambda p: p["name"]
    return sorted(players, key=key, reverse=descending)


def sort_players_by_created(players, descending=False):
    key = lambda p: p["created_at"]
    return sorted(players, key=key, reverse=descending)


def sort_players(players, field="name", descending=False):
    if field == "name":
        return sort_players_by_name(players, descending)
    if field == "created_at":
        return sort_players_by_created(players, descending)
    raise ValueError("Неподдерживаемое поле для сортировки: %s" % field)


if __name__ == "__main__":
    data = [
        {"name": "Иванов", "created_at": "2024-05-01"},
        {"name": "Петров", "created_at": "2024-03-10"},
        {"name": "Сидоров", "created_at": "2024-01-15"},
    ]
    print(sort_players(data, "name"))
    print(sort_players(data, "created_at"))
    print(sort_players(data, "name", descending=True))
    print(sort_players(data, "created_at", descending=True))
