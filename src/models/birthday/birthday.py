from datetime import datetime
from src.handlers.errors.custom_exceptions import CustomeExceptions
from src.models.general.field import Field


class Birthday(Field):
    def __init__(self, value: str):
        if not self.validate(value):
            raise CustomeExceptions.BirthdayError(f"Birthday '{value}' must be in format 'YYYY-MM-DD'")
        super().__init__(value)

    @staticmethod
    def validate(value: str):
        try:
            datetime.strptime(value, '%Y-%m-%d')
            return True
        except ValueError:
            return False