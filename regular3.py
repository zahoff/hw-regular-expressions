import re
from pprint import pprint
from typing import List
# читаем адресную книгу в формате CSV в список contacts_list
import csv

with open("phonebook_raw.csv") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
    print('contacts_list', contacts_list[0][0].split(';'))

    contacts_list3 = []

#разбираемся с фамилия,имя,отчество, так, чтобы в итоге все были ф,и,о
def fiochange(input):
    t1 = re.sub(r'(\w+)\s(\w+)\s(\w*)[,;][,;][,;](\w*)[,;]([\w ]*)[,;]([0-9\-\+\(\)доб\. ]*)[,;]([a-zA-Z0-9_\.]*@?[a-zA-Z0-9]*\.?[a-zA-Z]*)',
    r'\1;\2;\3;\4;\5;\6;\7;', input)
    t2 = re.sub(r'(\w+)[,;](\w+)\s(\w*)[,;][,;](\w*)[,;]([\w ]*)[,;]([0-9\-\+\(\)доб\. ]*)[,;]([a-zA-Z0-9_\.]*@?[a-zA-Z0-9]*\.?[a-zA-Z]*)',
    r'\1;\2;\3;\4;\5;\6;\7;', t1)
    t3 = re.sub(r'(\w+)\s(\w+)[,;][,;](\w*)[,;](\w*)[,;]([\w ]*)[,;]([0-9\-\+\(\)доб\. ]*)[,;]([a-zA-Z0-9_\.]*@?[a-zA-Z0-9]*\.?[a-zA-Z]*)',
    r'\1;\2;\3;\4;\5;\6;\7;', t2)
    return(t3)
dict_people = {}
contacts_list1 = []
# TODO 1: выполните пункты 1-3 ДЗ
for k in range(9):
    chel = fiochange(contacts_list[k][0])
    #print(k, chel)
    if chel.count(';') == 7:
        chel = chel[:-1]
    f,im,o,r,d,t,e =chel.split(';')
    res = re.sub(r"[\(\)\-\+ ]*", "", t)
    pattern = r"(7|8)(\d{3})(\d{3})(\d{2})(\d{2})(доб.\d{4})?"
    t = re.sub(pattern, r"+7(\2)\3-\4-\5\6", res)
    fi = f + ' ' + im
    dict_people[k] = [fi,o,r,d,t,e]
        #print(f,im,o,r,d,res,e)
    contacts_list1.append(chel)
#print(dict_people)
for k1,v1 in dict_people.items():
    for k2,v2 in dict_people.items():
        if dict_people[k1][0] == dict_people[k2][0]:
            for i in range(1,6):
                if dict_people[k1][i] == '':
                    dict_people[k1][i] = dict_people[k2][i]

dict2 = dict_people.copy()
for k1,v1 in dict_people.items():
    for k2,v2 in dict_people.items():
        if k1 < k2 and dict_people[k1][0] == dict_people[k2][0]:
            del dict2[k2]

contacts_list3 = [dict2[key] for key in dict2]


    # TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
with open("phonebook.csv", "w") as f:
    datawriter = csv.writer(f, delimiter=',')
    # Вместо contacts_list подставьте свой список
    datawriter.writerows(contacts_list3)