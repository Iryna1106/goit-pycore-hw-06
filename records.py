class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)
    
class Name(Field):
    pass

class Phone(Field):
    def __init__(self, value):
        if len(value) != 10 or not value.isdigit():
            raise TypeError('Phone number must be exact 10 digits')
        super().__init__(value)

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, number: str):
        self.phones.append(Phone(number))

    def remove_phone(self, number: str):
        self.phones=[p for p in self.phones if str(p)!=number ]

    def edit_phone(self, old_number, new_number):
        for idx,p in enumerate(self.phones):
             if str(p)==old_number:
                  self.phones[idx]=Phone(new_number)

    def find_phone(self, number):
        for phone in self.phones:
            if phone.value == number:
                return phone