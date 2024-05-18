from personal_assistant.src.models.address_book.address_book import AddressBook


def delete_record(book: AddressBook, name: str):
    book.delete(name)
    print(f"Deleted record for name '{name}'")