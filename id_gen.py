
from random import randint
def id_generator():#функция для создания ай ди в базе
    id_num = randint(1,100)
    id_num = str(id_num)
    with open('log_id.csv','r+') as id:
        if id_num in id.read().split(';'):
            return id_generator()
        else:
            id.write(f"{id_num};")
            return id_num

def id_corrector(item):#функция для удаления ID номера из базы
    t=[]
    i=3
    res_item = item
    while(i>0):
        res_item = res_item[:0] + res_item[1:]
        i-=1
    with open('log_id.csv','r+') as id:
        for line in id:
            if ';' in line:
                temp = line.strip().split(';')
                t=temp
        for line in t:
            if res_item in line:
                t.remove(res_item)
                t.remove('')
        with open('log_id.csv', 'w+') as id:
            for line in t:
                id.write(f"{line};")



