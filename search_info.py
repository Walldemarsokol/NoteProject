# модуль поиска

def search_info(word, data):#возвращает нужный список
    if len(data) > 0:
        for item in data:
            if word in item:
                return item
    else:
        return None
