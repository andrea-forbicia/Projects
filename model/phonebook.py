from typing import List


class Contact:
    def __init__(self, name, surname, phone):
        self.name = name
        self.surname = surname
        self.phone = phone

    def __str__(self):
        return f"{self.name} {self.surname}: {self.phone}"


class PhoneBook:
    def __init__(self):
        self.contacts = list()

    def add_contact(self, name: str, surname: str, phone: str) -> None:
        contact = Contact(name=name, surname=surname, phone=phone)
        self.contacts.append(contact)

    def remove_contact(self, position: int) -> None:
        self.contacts.pop(position)

    def search_contact(self, key: str) -> List[Contact]:
        result = list()
        for contact in self.contacts:
            if key in contact.name or key in contact.surname or key in contact.phone:
                result.append(contact.__str__())
        return result

    def print_contact(self, position: int) -> str:
        contact = self.contacts[position]
        return contact.__str__()

    def get_contacts(self) -> str:
        text = ""
        for contact in self.contacts:
            text = f"{text}{contact.__str__()}\n"
        return text
