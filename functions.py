#estrutura do contato:
# - Name
# - Telephone
# - Email
# - Favorite


#GLOBALS

contacts_dict = {}
favorites_contacts = {}

def contact_registration(name: str = '', tel: str = '', email: str = '', favorite: bool = False) -> None:
  contact = { 'name': name, 'tel': tel, 'email': email, 'favorite': favorite }
  contacts_dict[len(contacts_dict)] = contact


def get_all_contacts():
  print(contacts_dict)

def edit_contact(id: int, name: str = '', tel: str = '', email: str = ''):
  filtered_contact = contacts_dict[id]

  filtered_contact['name'] = name if name != '' else filtered_contact['name']
  filtered_contact['email'] = email if email != '' else filtered_contact['email']
  filtered_contact['tel'] = tel if tel != '' and len(tel) > 8 else filtered_contact['tel']

  contacts_dict[id] = filtered_contact

def toggle_favorite(id: int):
 print(type(id))
 contacts_dict[id]['favorite'] = not contacts_dict[id]['favorite']


def get_favorite_contacts():
  favorites_contacts = {}
  index = 0
  while index in range(len(contacts_dict)):
    if contacts_dict[index]['favorite'] == True:
      favorites_contacts[index] = contacts_dict[index]
    index = index + 1

  print(favorites_contacts)


def remove_contact(id: int):
  contacts_dict.pop(id)