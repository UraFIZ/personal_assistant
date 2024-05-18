from personal_assistant.src.handlers.errors.custom_exceptions import CustomeExceptions
from personal_assistant.src.models.general.field import Field


class Name(Field):
    def __init__(self, value: str):
        if not self.validate(value):
            raise CustomeExceptions.NameError(f"Name '{value}' must be alphabetic")
        super().__init__(value)

    @staticmethod
    def validate(value: str):
        return value.isalpha()