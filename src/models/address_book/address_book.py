from collections import UserDict
from src.models.address_book.record import Record


class AddressBook(UserDict):
    def add_record(self, record: Record):
        self.data[record.name.value] = record

    def find(self, name: str):
        return self.data.get(name)
    
    def create_record(self, name: str, phone: str):
        record = Record(name)
        record.add_phone(phone)
        self.add_record(record)
        return record

    def delete(self, name: str):
        try:
            del self.data[name]
        except KeyError:
            raise KeyError(f"Record '{name}' not found while trying to delete it")

    def __str__(self):
        return f"Address book: {', '.join(self.data.keys())}"
    
    def to_dict(self):
        return {name: record.to_dict() for name, record in self.data.items()}
    
    @classmethod
    def from_dict(cls, data):
        address_book = cls()
        for name, record in data.items():
            address_book.add_record(Record.from_dict(name, record))
        return address_book