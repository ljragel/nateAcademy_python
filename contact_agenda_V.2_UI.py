
import  pickle
from time import sleep
from tkinter import *
from tkinter import ttk

ACTION_ADD_CONTACT = 1
ACTION_REMOVE_CONTACT = 2
ACTION_FIND_CONTACT = 3
ACTION_EXPORT_CONTACT = 4
ACTION_EXIT = 5
ACTION_SHOW_CONTACTS = 6

MENU_OPTIONS = [ACTION_ADD_CONTACT,
                ACTION_REMOVE_CONTACT,
                ACTION_FIND_CONTACT,
                ACTION_EXPORT_CONTACT,
                ACTION_SHOW_CONTACTS]

SAVE_FILE_NAME = "contacts.save"


def ask_until_option_expected(options):
    selected_action = ""

    while not selected_action.isdigit() or (selected_action.isdigit() and int(selected_action) not in options):
        selected_action = input("¿Qué opción deseas?")

    return int(selected_action)


def show_menu():
    print("Acciones disponibles a elegir")
    print("1--> Añadir contacto")
    print("2--> Eliminar contacto")
    print("3--> Buscar un contacto")
    print("4--> Exportar contactos a un CSV")
    print("5--> Salir")
    print("6--> Mostrar contactos guardados")

    return ask_until_option_expected(MENU_OPTIONS)


def add_contact(contacts):
    print("\n\n Añadir contacto \n")
    contact = {
        "name": input("Nombre: "),
        "phone": input("Teléfono: "),
        "email": input("Email: ")
    }
    contacts.append(contact)
    print("Se ha añadido el contacto {} correctamente \n".format(contact["name"]))
    sleep(2)


def remove_contact(contacts):
    print("Elige el contacto que quieres borrar de la lista \n")
    print("-----------------------------------------------------")
    print(contacts)
    contact_to_remove = input("¿Qué contacto quieres borrar?. Escribe el nombre del contacto")
    for contact in contacts:
        if contact["name"] == contact_to_remove:
            contacts.remove(contact)
    print("Tu contacto seleccionado se ha eliminado con éxito!")
    print("-----------------------------------------------------")


def find_contact(contacts):
    print("\n\nBuscar contacto\n")
    search_term = input("Introducir el nombre del contacto o parte de él: ")
    found_contacts = []

    print("He encontrado los siguientes contactos:")
    contact_indexes = []
    contact_counter = 0

    for contact in contacts:
        if contact["name"].find(search_term) >= 0:
            found_contacts.append(contact)
            print("{} - {}".format(contact_counter, contact["name"]))
            contact_indexes.append(contact_counter)
            contact_counter += 1

    contact_index = 0

    if len(contact_indexes) > 1:
        contact_index = ask_until_option_expected(contact_indexes)
    elif len(contact_indexes) == 0:
        print("No se ha encontrado ninguno.")
        return

    print("\nInformación sobre {}\n".format(found_contacts[contact_index]["name"]))
    print("Nombre: {name}, Telefono: {phone}, Email: {email}\n\n".format(**found_contacts[contact_index]))
    sleep(2)


def export_contact(contacts):
    pass


def show_contacts(contacts):
    print(contacts)


def load_contacts():
    try:
        return pickle.load(open(SAVE_FILE_NAME, "rb"))
    except FileNotFoundError:
        return []


def save_contacts(contacts):
    with open(SAVE_FILE_NAME, "wb") as save_file:
        pickle.dump(contacts, save_file)
    print("Datos guardados satisfactoriamente!")


def main():
    contacts = load_contacts()
    action = show_menu()

#Interfaz
    root= Tk()
    frame_add_contact= ttk.Frame(root, padding="30 12 30 12")
    frame_add_contact.grid()







if __name__ == "__main__":
    main()