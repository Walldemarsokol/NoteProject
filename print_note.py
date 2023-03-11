def print_note(data):
    if len(data) > 0:
        print('ID'.center(20),'Дата создания'.center(20),'Заголовок'.center(15),'Заметка'.center(20))
        print('-'*130)
        for item in data:
            print(item[0].center(20),item[1].center(5),item[2].center(5),item[3].center(20),item[4].center(30))
    else:
        print('Справочник пуст!')