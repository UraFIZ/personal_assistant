from personal_assistant.src.models.address_book.address_book import AddressBook
from personal_assistant.src.utils.formatting.format_table import format_table

def list_records(book: AddressBook):
    if not book.data:
        print("Address book is empty.")
        return
    
    headers = ["Name", "Phone Numbers", "Birthday"]
    rows = [[name, ', '.join(phone.value for phone in record.phones), str(record.birthday) ] for name ,record in book.data.items()]
    print(format_table(headers, rows))