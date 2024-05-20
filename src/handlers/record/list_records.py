from src.utils.formatting.format_table import format_table

def list_records(book):
    if not book.data:
        print("Address book is empty.")
        return
    
    headers = ["Name", "Phone Numbers", "Birthday"]
    rows = [[name, ', '.join(phone.value for phone in record.phones), str(record.birthday) ] for name ,record in book.data.items()]
    print(format_table(headers, rows))