from add_note import add_note
from export_note import export_data
from print_note import print_note
from datetime import datetime
from id_gen import *

def greeting():
    print("Добро пожаловать в приложение заметки!")

def search_info(word, data):
    if len(data) > 0:
        for item in data:
            if word in item:
                return item
    else:
        return None

def input_data():
    id_note = str("ID-" + id_generator()) #id note
    y_m_d = datetime.now().strftime('%d.%m.%Y')
    h_m = datetime.now().strftime('%H:%M')# date/time
    head_note = input("Введите заголовок заметки: ")
    body_note = input("Введите тело заметки: ")
    return [id_note,y_m_d,h_m,head_note, body_note ]

def menu_note(word):
    print("Выберете команду:\n\
    red - Редактировать заметку;\n\
    del - Удалить заметку;\n\
    return - Вернуться в основное меню.")
    choice = input("Введите команду: ")
    if choice == 'red':
        return 1
    elif choice == 'del':
        delete_note(word)
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

def delete_note(word):
    t = []
    data = []
    tp = []
    id_corrector(word)
    with open('notes.csv','r',encoding='utf-16') as f:
        for line in f:
            if ';' in line:
                temp = line.strip().split(';')
                data.append(line)
                t.append(temp)
        for line in t:
            if word in line:
                tp=line
                tp.pop()

        string_line = ''

        for item in tp:
            string_line = (string_line + item + ";")
        for element in data:
            if string_line in element:
                index = data.index(element)
                data.pop(index)
            else:
                print()
    with open('notes.csv', 'w', encoding='utf-16') as f:
        for text in data:
            f.write(text)




def choice_todo():
    # delete_note()
    print("Вы в главном меню.")
    print("Выберете команду:\n\
    add - Добавить заметку;\n\
    all - Показать все заметки;\n\
    find - Поиск заметки;\n\
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
        word = input("Введите дату (dd.mm.yy) или ID или заголовок: ")
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
        return print('Спасибо за то, что пользовались нашей программой!\n')
    else:
        print('Неверный ввод данных. Повторите попытку выбора.')
        return choice_todo()

