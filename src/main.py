from handlers.birthday.add_birthday import add_birthday
from handlers.birthday.get_upcoming_birthdays import get_upcoming_birthdays
from handlers.birthday.show_birthday import show_birthday
from handlers.record.add_record import add_record
from handlers.record.delete_record import delete_record
from handlers.record.edit_record import edit_record
from handlers.record.find_record import find_record
from handlers.record.list_records import list_records
from storage.AddressBookStorage import AddressBookStorage
from utils.parse.parse_command import parse_command


def main():
    storage = AddressBookStorage()
    book = storage.load()
    parse_command().print_help()

    while True:
        command = input("Enter command: ").strip()
        
        if command.lower() in ["close", "exit"]:
            storage.save(book)
            print("Exiting program.")
            break

        try:
            args = parse_command().parse_args(command.split())
            if args.command == 'add':
                add_record(book, args.name, args.phone[0])
            elif args.command == 'change':
                edit_record(book, args.name, args.old_phone, args.new_phone)
            elif args.command == 'delete':
                delete_record(book, args.name)
            elif args.command == 'phone':
                find_record(book, args.name)
            elif args.command == 'all':
                list_records(book)
            elif args.command == 'hello':
                print("💝🐽🐽🐽 '' 🐷 '' 🐽🐽🐽💝")
            elif args.command == 'add-birthday':
                add_birthday(book, args.name, args.birthday)
            elif args.command == 'show-birthday':
                show_birthday(book, args.name)
            elif args.command == 'birthdays':
                get_upcoming_birthdays(book)
            else:
                print("Unknown command. Please try again.")

        except SystemExit:
            continue

        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nExiting program.")