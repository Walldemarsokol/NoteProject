from id_gen import id_corrector
from datetime import datetime
from add_note import add_note


def new_input(word):
    id_note = word  # id note
    y_m_d = datetime.now().strftime('%d.%m.%Y')
    h_m = datetime.now().strftime('%H:%M')  # date/time
    head_note = input("Введите новый заголовок заметки: ")
    body_note = input("Введите новое тело заметки: ")
    return [id_note, y_m_d, h_m, head_note, body_note]

def delete_note(word):#функция удаления заметки
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

def redact_note(word):#функция редактирования заметки
    delete_note(word)
    i=3
    res_item = word
    while(i>0):
        res_item = res_item[:0] + res_item[1:]
        i-=1
    with open('log_id.csv', 'r+') as id:
        id.write(f"{res_item};")
    add_note(new_input(word))
