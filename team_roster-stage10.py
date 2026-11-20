# === Stage 10: Поиск по нескольким словам ===
# Project: TeamRoster
def search_players(players, query):
    """Поиск игроков по нескольким словам с поддержкой исключений.

    В запросе слова через пробел. Перед словом можно поставить знак
    «-», чтобы исключить игроков, у которых есть это слово в любом
    из полей. Слова без «-» — это обязательные фильтры (AND).
    """
    must_include = []
    must_exclude = []

    for token in query.split():
        if token.startswith("-"):
            must_exclude.append(token[1:].strip().lower())
        else:
            must_include.append(token.lower())

    results = []

    for player in players:
        text = " ".join(
            str(value).lower()
            for value in (player.name, player.position, str(player.number), player.status)
        )

        if any(word in text for word in must_exclude):
            continue

        if must_include and not all(word in text for word in must_include):
            continue

        results.append(player)

    return results


if __name__ == "__main__":
    class Player:
        def __init__(self, name, position, number, status):
            self.name = name
            self.position = position
            self.number = number
            self.status = status

    team = [
        Player("Иван Петров", "защитник", 4, "активен"),
        Player("Алексей Смирнов", "нападающий", 9, "активен"),
        Player("Дмитрий Козлов", "вратарь", 1, "травмирован"),
        Player("Ольга Новикова", "защитник", 5, "активен"),
    ]

    print(search_players(team, "защитник"))
    print(search_players(team, "активен -травмирован"))
    print(search_players(team, "-вратарь нападающий"))
    print(search_players(team, "Петров Иванов"))
    print(search_players(team, ""))
