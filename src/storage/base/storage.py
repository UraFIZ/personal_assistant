from src.storage.serialization.serialization_strategy import SerializationStrategy

class Storage:
    def __init__(self, strategy: SerializationStrategy, storage_path: str, modificator: str = 'w', error_exception: Exception = SyntaxError):
        self.storage_path = storage_path
        self.modificator = modificator
        self.error_exception = error_exception
        self.strategy = strategy

    def save(self, data: dict):
        with open(self.storage_path, self.modificator) as file:
            file.write(self.strategy.serialize(data))

    def load(self) -> dict:
        try:
            with open(self.storage_path, 'r') as file:
                return self.strategy.deserialize(file.read())
        except (FileNotFoundError, self.error_exception):
            return {}