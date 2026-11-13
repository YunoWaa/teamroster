# === Stage 5: Удаление и восстановление ===
# Project: TeamRoster
import datetime


class PlayerStatus:
    ACTIVE = "active"
    INJURED = "injured"
    REMOVED = "removed"


class Player:
    def __init__(self, name, position, number, status=PlayerStatus.ACTIVE):
        self.name = name
        self.position = position
        self.number = number
        self.status = status
        self.removed_at = None
        self.removed_reason = None

    def remove(self, reason, when=None):
        self.status = PlayerStatus.REMOVED
        self.removed_reason = reason
        self.removed_at = when or datetime.datetime.now()

    def restore(self):
        if self.status != PlayerStatus.REMOVED:
            raise ValueError("Игрок уже не в статусе удалённого")
        self.status = PlayerStatus.ACTIVE
        self.removed_at = None
        self.removed_reason = None

    def is_soft_removed(self):
        return self.status == PlayerStatus.REMOVED

    def get_info(self):
        if self.is_soft_removed():
            return f"{self.name} (#{self.number}) — удалён: {self.removed_reason}"
        return f"{self.name} (#{self.number}) [{self.position}]"


class PlayerRoster:
    def __init__(self):
        self._players = {}

    def add(self, player):
        self._players[player.number] = player

    def get(self, number):
        return self._players.get(number)

    def is_present(self, number):
        player = self._players.get(number)
        return player is not None and not player.is_soft_removed()

    def remove_player(self, number, reason, when=None):
        player = self._players.get(number)
        if player is None:
            raise KeyError(f"Игрок #{number} не найден")
        player.remove(reason, when)

    def restore_player(self, number):
        player = self._players.get(number)
        if player is None or not player.is_soft_removed():
            raise KeyError(f"Игрок #{number} не может быть восстановлен")
        player.restore()

    def list_active(self):
        return [p for p in self._players.values() if p.is_present(number)]


if __name__ == "__main__":
    roster = PlayerRoster()
    a = Player("Иванов", "Атака", 10)
    b = Player("Петров", "Защита", 4)
    roster.add(a)
    roster.add(b)

    print(roster.list_active())
    roster.remove_player(10, "переход в другой клуб")
    print(roster.list_active())
    print(roster.get(10).get_info())
    roster.restore_player(10)
    print(roster.list_active())
