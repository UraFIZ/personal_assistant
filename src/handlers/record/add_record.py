from personal_assistant.src.models.address_book.address_book import AddressBook
from personal_assistant.src.models.address_book.record import Record


def add_record(book: AddressBook, name: str, phone: str):
    record: Record = book.find(name)
    if record:
        record.add_phone(phone)
        print(f"Added phones to existing record: {record}")
    else:
        record = Record(name)
        record.add_phone(phone)
        book.add_record(record)
        print(f"Added new record: {record}")