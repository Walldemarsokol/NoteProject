def add_note (data):#функция для создания заметки
    with open('notes.csv', 'a+', encoding='utf-16') as file:
        for i in data:
            file.write(f"{i};")
        file.write(f"\n")
