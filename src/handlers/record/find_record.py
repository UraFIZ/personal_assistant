


def find_record(book, name: str):
    record = book.find(name)
    if record:
        print(record)
    else:
        print(f"No record found for name '{name}'")