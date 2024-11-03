from addressbook import AddressBook
from functions import *
from utils import parse_input

def main():
    book = AddressBook()
    print("Welcome to an assistant bot!")
    while True:
        try:
            user_input = input("Enter a command: ")
            command, *args = parse_input(user_input)
            if command in ["close", "exit"]:
                print("See you!")
                break
            elif command == "hello":
                print("What would you like me to do?")
            elif command == "add":
                print(add_contact(args,book))
            elif command == "change":
                print(change_contact(args,book))
            elif command == "phone":
                print(show_phone(args[0], book))
            elif command == "all":
                print('Name    | Phone '  )
                print("--------|----------")  
                for name,record in book.data.items(): 
                    print(f"{record.name.value:<7} | {', '.join(map(str, record.phones)):<12}")
            elif command == "delete":
                print(delete_contact(args, book)) 
            else:
                print("Invalid command.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()