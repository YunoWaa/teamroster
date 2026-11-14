# === Stage 6: Связанная сущность ===
# Project: TeamRoster
from datetime import date, datetime


class Training:
    def __init__(self, name, description, start_time, end_time, date):
        self.name = name
        self.description = description
        self.start_time = start_time
        self.end_time = end_time
        self.date = date
        self.players = []

    def add_player(self, player_id):
        self.players.append(player_id)

    def remove_player(self, player_id):
        if player_id in self.players:
            self.players.remove(player_id)

    def player_count(self):
        return len(self.players)

    def __str__(self):
        return f"Тренировка: {self.name} ({self.date}, {self.start_time}-{self.end_time})"


class TrainingManager:
    def __init__(self):
        self.trainings = []

    def add_training(self, training):
        self.trainings.append(training)

    def get_training(self, training_id):
        for training in self.trainings:
            if training.name == training_id:
                return training
        return None

    def list_trainings(self):
        return self.trainings

    def create_training(self, name, description, start_time, end_time, date, players=None):
        training = Training(name, description, start_time, end_time, date)
        if players:
            for player_id in players:
                training.add_player(player_id)
        self.add_training(training)
        return training
