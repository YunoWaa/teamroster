# === Stage 2: Проверка полей ===
# Project: TeamRoster
from typing import Optional


VALID_POSITIONS = {
    "ВР",
    "Защ",
    "Пол",
    "Нап",
}

VALID_STATUSES = {
    "Активен",
    "Травмирован",
    "Резерв",
    "Отстранён",
}


def normalize_text(value: str) -> str:
    text = value.strip()
    text = text.replace("\u00a0", " ").replace("\t", " ")
    return text


def normalize_position(value: str) -> str:
    text = normalize_text(value).upper()
    if text not in VALID_POSITIONS:
        raise ValueError(
            "Неверная позиция: допустимы "
            + ", ".join(sorted(VALID_POSITIONS))
            + ". Введено «" + value.strip() + "»."
        )
    return text


def normalize_status(value: str) -> str:
    text = normalize_text(value).lower()
    lookup = {
        "активный": "Активен",
        "травмированный": "Травмирован",
        "резерв": "Резерв",
        "отстранённый": "Отстранён",
        "отстраненный": "Отстранён",
    }
    if text not in lookup:
        raise ValueError(
            "Неверный статус: допустимы "
            + ", ".join(sorted(VALID_STATUSES))
            + ". Введено «" + value.strip() + "»."
        )
    return lookup[text]


def normalize_number(value: str) -> int:
    text = normalize_text(value)
    try:
        return int(text)
    except ValueError:
        raise ValueError(
            "Номер должен быть целым числом. Введено «" + value.strip() + "»."
        )


def normalize_number_in_range(value: str, low: int, high: int) -> int:
    number = normalize_number(value)
    if number < low or number > high:
        raise ValueError(
            f"Номер должен находиться в диапазоне {low}-{high}. "
            f"Введено «{number}»."
        )
    return number


def check_player(name: str, position: str, number: str, status: str) -> None:
    normalized_name = normalize_text(name)
    if not normalized_name:
        raise ValueError("Имя игрока не может быть пустым.")
    if len(normalized_name) > 50:
        raise ValueError("Имя игрока не должно превышать 50 символов.")

    normalized_position = normalize_position(position)
    normalized_status = normalize_status(status)
    normalized_number = normalize_number_in_range(number, 1, 99)

    if len(normalized_name) != len(set(normalized_name)):
        raise ValueError("Имя игрока не должно содержать пробелов или дублей.")
