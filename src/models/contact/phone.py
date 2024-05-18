from personal_assistant.src.handlers.errors.custom_exceptions import CustomeExceptions
from personal_assistant.src.models.general.field import Field


class Phone(Field):
    def __init__(self, value: str):
        if not self.validate(value):
            raise CustomeExceptions.PhoneLengthError(f"Phone '{value}' must be 10 digits long")
        super().__init__(value)

    @staticmethod
    def validate(value: str):
        return len(value) == 10 and value.isdigit()
    
    def __repr__(self):
        return f"Phone(number={self.value}"