
def create_phonebook(name):
    phonebook = {"name": name, "contacts" : {}} 
    return phonebook

phonebook = create_phonebook("Celine's PhoneBook")

def add_contact(name, number, phonebook):
    phonebook["contacts"][name] = number 

add_contact("Heba", 911, phonebook)


print(phonebook)

