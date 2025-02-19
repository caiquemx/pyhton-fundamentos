#aqui vamos estrutar as principais atividades do programa

#estrutura do contato:
# - Name
# - Telephone
# - Email
# - Favorite

import functions



def show_menu():
  print('-------------------------------------')
  print('---------------AGENDA----------------')
  print('-------------------------------------')
  print('Digite a opção desejada:')
  print('1 - Contatos')
  print('2 - Contatos Favoritos')
  print('3 - Adicionar Contato')
  print('4 - Editar Contato')
  print('5 - Excluir Contato')
  print('6 - Favoritar/Desfavoritar um contato')
  print('7 - Sair')

main_menu_option = 0

while main_menu_option != '7':
  show_menu()
  main_menu_option = input()
  match main_menu_option:
    case '1':
      functions.get_all_contacts()
      input('\nPressione uma tecla para continuar...')
      main_menu_option = ''
    case '2':
      functions.get_favorite_contacts()
      input('\nPressione uma tecla para continuar...')
      main_menu_option = ''
    case '3':
      print("Estrutura de um contato {name: 'qualquer', tel: 'qualquer', email: 'qualquer'}\n")
      contact = {
        'name': input('Digite o nome do contato: '),
        'tel': input('Digite o telefone: '),
        'email': input('Digite o email do contato: '),
        'favorite': input('Contato é favorito? (SIM ou NÃO): ').upper() == 'SIM'
      }

      inside_option = ''
      while inside_option != '0':
        print('0 - SALVAR')
        print('1 - SAIR')
        inside_option = input()
        match inside_option:
          case '0':
            functions.contact_registration(contact['name'], contact['tel'], contact['email'], contact['favorite'])
            break
          case '1':
            break
          case _:
            break
      
      print('Contato adicionado')
      main_menu_option = ''

    case '4':
      print('Para editar você precisa saber o id do contato')
      contact = {}
      id = input('Digite o id do contato:')
      contact['name'] = input('Digite o nome do contato ')
      contact['tel'] = input('Digite o telefone:')
      contact['email'] = input('Digite o email do contato:')

      functions.edit_contact(int(id), contact['name'], contact['tel'], contact['email'], contact['favorite'])
      print('Contato editado')
      main_menu_option = ''

    case '5':
      print('Para excluir você precisa saber o id do contato')
      id = input('Digite o id do contato:')
      functions.remove_contact(int(id))
      print('Contato removido')

      main_menu_option = ''
    case '6':
       print('Para favoritar/desfavoritar você precisa saber o id do contato')
       id = input('Digite o id do contato:')
       functions.toggle_favorite(int(id))
       print('Contato editado')
       main_menu_option = ''

    case '7':
      break



