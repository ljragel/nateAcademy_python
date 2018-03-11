
ACTION_ADD_CONTACT= 1
ACTION_REMOVE_CONTACT= 2
ACTION_FIND_CONTACT= 3
ACTION_EXPORT_CONTACT=4
ACTION_EXIT=5

MENU_OPTIONS= [ACTION_ADD_CONTACT, ACTION_REMOVE_CONTACT, ACTION_FIND_CONTACT, ACTION_EXPORT_CONTACT, ACTION_EXIT]



def show_menu():
    print("Acciones disponibles:")
    print("1--> Añadir contacto")
    print("2--> Eliminar contacto")
    print("3--> Buscar un contacto")
    print("4--> Exportar contactos a un CSV")
    print("5- Salir")

    selected_aciton=""

    while not selected_aciton.isdigit() or (selected_aciton.isdigit() and int(selected_aciton) not in MENU_OPTIONS):

def add_contact():
    pass





def main():

    action=show_menu()

    while action != ACTION_EXIT:
       if action == ACTION_ADD_CONTACT
           add_contact()
        action= show_menu()
        elif action==ACTION_REMOVE_CONTACT
         remove_contact()
        elif action==ACTION_FIND_CONTACT:
            find_contact()
        elif action== A

    #Exit the program




if __name__=="__main__":
    main()