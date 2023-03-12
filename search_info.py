# модуль поиска

def search_info(word, data):#поиск/сравнение
    if len(data) > 0:
        for item in data:
            if word in item:
                return item
    else:
        return None
