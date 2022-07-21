from model.phonebook import PhoneBook
from model.dispenser import *

# ******************** PhoneBook ********************
print("**** PhoneBook Test ****")
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


# ******************** Dispenser ********************
print("\n**** Dispenser Test ****")
dispenser = Dispenser()

dispenser.add_drink(code="D1", name="Cola", price=1.2)
dispenser.add_drink(code="D2", name="Fanta", price=1.0)
dispenser.add_drink(code="D3", name="Lemon", price=0.8)
dispenser.add_drink(code="D4", name="Water", price=0.6)

dispenser.add_card(code="C1", credit=5.0)
dispenser.add_card(code="C2", credit=4.2)
dispenser.add_card(code="C3", credit=2.4)
dispenser.add_card(code="C4", credit=0.0)

dispenser.add_column(number=1, drink_name="Cola", drink_quantity=10)
dispenser.add_column(number=2, drink_name="Fanta", drink_quantity=8)
dispenser.add_column(number=3, drink_name="Lemon", drink_quantity=6)
dispenser.add_column(number=4, drink_name="Water", drink_quantity=12)

dispenser.deliver_drink(drink_code="D2", card_code="C1")

print("Test get_drink_name:")
print(dispenser.get_drink_name(drink_code="D2"))

print("\nTest get_drink_price:")
print(dispenser.get_drink_price(drink_code="D2"))

print("\nTest get_card_credit:")
print(dispenser.get_card_credit(card_code="C1"))
print("")
