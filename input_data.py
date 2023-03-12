from id_gen import id_generator
from datetime import datetime

def input_data():#позволяет вводить данные
    id_note = str("ID-" + id_generator()) #id note
    y_m_d = datetime.now().strftime('%d.%m.%Y')
    h_m = datetime.now().strftime('%H:%M')# date/time
    head_note = input("Введите заголовок заметки: ")
    body_note = input("Введите тело заметки: ")
    return [id_note,y_m_d,h_m,head_note, body_note ]