def add_record(book, name: str, phone: str):
    record = book.find(name)
    if record:
        record.add_phone(phone)
        print(f"Added phones to existing record: {record}")
    else:
        new_record = book.create_record(name, phone)
        print(f"Added new record: {new_record}")