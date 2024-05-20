from src.handlers.birthday.upcoming_birthday_controller import UpcomingBirthday

def get_upcoming_birthdays(book):
    birthday_handler = UpcomingBirthday()
    if not book.data:
        print("Address book is empty.")
        return

    birthday_data = [ { "name": name, "birthday": str(record.birthday), "phone": str(record.phones[0]) } for name, record in book.data.items() if record.birthday ]
    if not birthday_data:
        print("No birthdays in the address book.")
        return
    try:
        for item in birthday_handler.get_upcoming_birthdays(birthday_data):
            print(f"Congratulate {item['name']} on {item['congratulation_date']} at phone {item['phone']}")
    except Exception as e:
        print(e)