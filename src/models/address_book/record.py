from src.handlers.errors.custom_exceptions import CustomeExceptions
from src.models.birthday.birthday import Birthday
from src.models.contact.phone import Phone
from src.models.general.name import Name


class Record:
    def __init__(self, name: str):
        self.name = Name(name)
        self.phones: list[Phone] = []
        self.birthday = None

    def add_phone(self, phone: str):
        if self.find_phone(phone):
            raise CustomeExceptions.PhoneAlreadyExists(f"Phone '{phone}' already exists in the record")
        self.phones.append(Phone(phone))
    
    def add_birthday(self, birthday: str):
        if not Birthday.validate(birthday):
            raise CustomeExceptions.BirthdayError(f"Birthday '{birthday}' must be in format 'YYYY-MM-DD'")
        self.birthday = Birthday(birthday)

    def remove_phone(self, phone: str):
        try:
            index = next(i for i, p in enumerate(self.phones) if p.value == phone)
            del self.phones[index]
        except StopIteration:
            raise CustomeExceptions.PhoneNotFound(f"Phone '{phone}' not found while trying to remove it")

    def edit_phone(self, old_phone: str, new_phone: str):
        if not Phone.validate(new_phone):
            raise CustomeExceptions.PhoneLengthError(f"Phone '{new_phone}' must be 10 digits long")
        try:
            phone_to_edit = next(p for p in self.phones if p.value == old_phone)
            phone_to_edit.value = new_phone
        except StopIteration:
            raise CustomeExceptions.PhoneNotFound(f"Phone '{old_phone}' not found while trying to edit it")

    def find_phone(self, phone: str):
        return next((p for p in self.phones if p.value == phone), None)
    
    def to_dict(self):
        result = {
            "phones": [phone.value for phone in self.phones]
        }
        if self.birthday:
            result["birthday"] = self.birthday.value
        return result

    def __str__(self):
            phones = '; '.join(p.value for p in self.phones)
            return f"Contact name: {self.name.value}, phones: {phones}, birthday: {self.birthday.value if self.birthday else 'N/A'}"
    
    @classmethod
    def from_dict(cls, name, record_data):
        record = cls(name)
        for phone in record_data.get("phones", []):
            record.add_phone(phone)
        if "birthday" in record_data:
            record.add_birthday(record_data["birthday"])
        return record