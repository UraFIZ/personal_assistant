def delete_record(book, name: str):
    book.delete(name)
    print(f"Deleted record for name '{name}'")