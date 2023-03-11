
from random import randint
def id_generator():
    id_num = randint(1,100)
    print(id_num)
    id_num = str(id_num)
    with open('log_id.csv','r+') as id:
        if id_num in id.read().split(';'):
            return id_generator()
        else:
            id.write(f"{id_num};")
            return id_num



