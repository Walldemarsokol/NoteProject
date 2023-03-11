# модуль поиска

from export_note import export_data
from print_data import print_data

def search_info(word, data):
    if len(data) > 0:
        for item in data:
            if word in item:
                return item
    else:
        return None
