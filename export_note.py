
def export_data():#разбивает на несколько списков
    with open('notes.csv', 'r', encoding='utf-16') as file:
        data = []
        t = []
        for line in file:
            if ';' in line:
                temp = line.strip().split(';')
                data.append(temp)
            else:
                data.append(t)
                t = []
    return data