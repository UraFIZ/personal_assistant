
def add_birthday(book, name: str, birthday: str):
    record = book.find(name)
    if record:
        record.add_birthday(birthday)
        print(f"Added birthday to record: {record}")
    else:
        print(f"No record found for name '{name}'")