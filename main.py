from model.phonebook import PhoneBook

phonebook = PhoneBook()

phonebook.add_contact(name="Mario", surname="Rossi", phone="331")
phonebook.add_contact(name="Valeria", surname="Verdi", phone="332")
phonebook.add_contact(name="Salvatore", surname="Bruno", phone="333")
phonebook.add_contact(name="Franco", surname="Neri", phone="334")
phonebook.add_contact(name="Marta", surname="Bianchi", phone="335")
phonebook.add_contact(name="Francesca", surname="Viola", phone="336")

phonebook.remove_contact(5)

print("Test search_contact:")
print(phonebook.search_contact(key="B"))

print("\nTest print_contact:")
print(phonebook.print_contact(0))

print("\nTest get_contact:")
print(phonebook.get_contacts())
