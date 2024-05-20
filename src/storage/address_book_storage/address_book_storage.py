from src.models.address_book.address_book import AddressBook
from src.storage.base.storage import Storage


class AddressBookStorage(Storage):
    def __init__(self, strategy, filename, modificator, error_exception):
        super().__init__(strategy, filename, modificator, error_exception)

    def save(self, book: AddressBook):
        try:
            super().save(book.to_dict())
        except Exception as e:
            print(f"Error: {e}")

    def load(self) -> AddressBook:
        try:
            data = super().load()
            if not data:
                    return AddressBook()
            return AddressBook.from_dict(data)
        except Exception as e:
            AddressBook()

