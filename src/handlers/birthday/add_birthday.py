from personal_assistant.src.models.address_book.address_book import AddressBook
from personal_assistant.src.models.address_book.record import Record


def add_birthday(book: AddressBook, name: str, birthday: str):
    record: Record = book.find(name)
    if record:
        record.add_birthday(birthday)
        print(f"Added birthday to record: {record}")
    else:
        print(f"No record found for name '{name}'")