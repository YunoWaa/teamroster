# === Stage 8: Фильтрация записей ===
# Project: TeamRoster
def filter_players_by_position(players, position):
    return [p for p in players if p.get("position") == position]


def filter_players_by_date_range(players, start_date, end_date):
    def parse_date(date_str):
        for fmt in ("%Y-%m-%d", "%d.%m.%Y", "%d/%m/%Y"):
            try:
                return datetime.strptime(date_str, fmt).date()
            except ValueError:
                continue
        raise ValueError(f"Неверный формат даты: {date_str}")

    filtered = []
    for p in players:
        if "date" not in p:
            continue
        player_date = parse_date(p["date"])
        if start_date <= player_date <= end_date:
            filtered.append(p)
    return filtered


def filter_players(players, position=None, start_date=None, end_date=None):
    result = list(players)
    if position is not None:
        result = filter_players_by_position(result, position)
    if start_date is not None and end_date is not None:
        result = filter_players_by_date_range(result, start_date, end_date)
    return result
