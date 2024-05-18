from personal_assistant.src.models.address_book.address_book import AddressBook
from personal_assistant.src.models.address_book.record import Record


def find_record(book: AddressBook, name: str):
    record: Record = book.find(name)
    if record:
        print(record)
    else:
        print(f"No record found for name '{name}'")