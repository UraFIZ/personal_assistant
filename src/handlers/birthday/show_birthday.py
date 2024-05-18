from personal_assistant.src.models.address_book.address_book import AddressBook


def show_birthday(book: AddressBook, name: str):
    record = book.find(name)
    if record:
        if record.birthday:
            print(f"{name} has a birthday in {record.birthday}")
        else:
            print(f"{name} has no birthday date in the address book.")
    else:
        print(f"No birthday date found for name '{name}' in the address book.")