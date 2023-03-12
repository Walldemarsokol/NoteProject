from export_note import export_data
from print_note import print_note
from search_info import search_info
from input_data import input_data
from delete_note import *
def greeting():
    print("Добро пожаловать в приложение заметки!")

def menu_note(word):
    print("Выберете команду:\n\
    red - Редактировать заметку;\n\
    del - Удалить заметку;\n\
    return - Вернуться в основное меню.")
    choice = input("Введите команду: ")
    if choice == 'red':
        redact_note(word)
        print()
        print()
        print('-' * 130)
        choice_todo()
    elif choice == 'del':
        delete_note(word)
        print()
        print()
        print('-' * 130)
        choice_todo()
    elif choice == 'return':
        print()
        print()
        print()
        return choice_todo()
    else:
        print('Неверный ввод данных. Повторите попытку выбора.')
        print()
        print()
        print()
        return menu_note(word)

def choice_todo():
    # delete_note()
    print("Вы в главном меню.")
    print("Выберете команду:\n\
    add - Добавить заметку;\n\
    all - Показать все заметки;\n\
    find - Поиск заметки по ID/дате/времени/заголовку;\n\
    exit - Выход из программы.")
    ch = input("Введите команду: ")
    if ch == 'add':
        add_note(input_data())
        print()
        print()
        print('-' * 130)
        choice_todo()
    elif ch == 'all':
        data = export_data()
        print_note(data)
        print()
        print()
        print('-' * 130)
        choice_todo()
    elif ch== 'find':
        word = input("Введите дату (dd.mm.yy),время (hh:mm) или ID (ID-..) или заголовок: ")
        data = export_data()#набор списков
        item = search_info(word, data)#озвращает нужный список
        if item != None:
            print('ID'.center(20),'Дата создания'.center(20),'Заголовок'.center(15),'Заметка'.center(20))
            print('-'*130)
            print(item[0].center(20),item[1].center(5),item[2].center(5),item[3].center(20),item[4].center(30))
            print()
            print()
            print()
            menu_note(word)

        else:
            print("Данные не обнаруженны")
            print()
            print()
            print()
            choice_todo()
    elif ch== 'exit':
        return print('Спасибо за то, что пользовались программой!\n')
    else:
        print('Неверный ввод данных. Повторите попытку выбора.')
        return choice_todo()