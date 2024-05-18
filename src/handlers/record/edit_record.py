from personal_assistant.src.models.address_book.address_book import AddressBook
from personal_assistant.src.models.address_book.record import Record


def edit_record(book: AddressBook, name: str, old_phone: str, new_phone: str):
    record: Record = book.find(name)
    if record:
        record.edit_phone(old_phone, new_phone)
        print(f"Edited record: {record}")
    else:
        print(f"No record found for name '{name}'")