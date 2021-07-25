class Trainer:
    autoincremental_id = 1

    def __init__(self, name):
        self.name = name
        self.id = Trainer.autoincremental_id
        Trainer.autoincremental_id += 1

    @staticmethod
    def get_next_id():
        return Trainer.autoincremental_id

    def __repr__(self):
        return f"Trainer <{self.id}> {self.name}"




