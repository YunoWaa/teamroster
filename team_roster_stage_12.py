# === Stage 12: Быстрые фильтры ===
# Project: TeamRoster
from datetime import datetime, timedelta


def _today():
    return datetime.now().date()


def _start_of_week():
    today = _today()
    monday = today - timedelta(days=today.weekday())
    return monday


def filter_player_records(records, player_field, today=None):
    today = today or _today()
    week_start = _start_of_week()

    def is_today(record):
        value = record.get(player_field) or ""
        return value.startswith(str(today))

    def is_this_week(record):
        value = record.get(player_field) or ""
        try:
            date = datetime.strptime(value[:10], "%Y-%m-%d").date()
        except (ValueError, TypeError):
            return False
        return week_start <= date <= today

    def is_overdue(record):
        value = record.get(player_field) or ""
        try:
            date = datetime.strptime(value[:10], "%Y-%m-%d").date()
        except (ValueError, TypeError):
            return False
        return date < today

    overdue = [r for r in records if is_overdue(r)]
    this_week = [r for r in records if is_this_week(r)]
    today_list = [r for r in records if is_today(r)]

    return {
        "today": today_list,
        "this_week": this_week,
        "overdue": overdue,
    }
