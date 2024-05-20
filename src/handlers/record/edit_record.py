
def edit_record(book, name: str, old_phone: str, new_phone: str):
    record = book.find(name)
    if record:
        record.edit_phone(old_phone, new_phone)
        print(f"Edited record: {record}")
    else:
        print(f"No record found for name '{name}'")