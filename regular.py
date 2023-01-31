import re
from pprint import pprint
from typing import List
# читаем адресную книгу в формате CSV в список contacts_list
import csv

with open("phonebook_raw.csv") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
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

# TODO 1: выполните пункты 1-3 ДЗ
for k in range(12):
    contacts_list1 = fiochange(contacts_list[k][0])

# избавляемся от скобок минусов и плюсов ( у некоторых написано 7 у некоторых +7)
    contacts_list2 = re.sub(r"[\(\)\-\+]*", "", contacts_list1)
    contacts_list3.append(contacts_list2)

#борьба с пробелами в телефоне, но не в должности
    my_string = contacts_list3[k]
    start = -1
    count = 0
    z=[]
    while True:
        start = my_string.find(';', start+1)
        if start == -1:
            break
        count += 1
        z.append(start)

    tel = ""
    for i in range(z[4],z[5]):
        if contacts_list3[k][i] != " ":
            tel += contacts_list3[k][i]

# выставляем формат телефона
    pattern = r"(7|8)(\d{3})(\d{3})(\d{2})(\d{2})(доб.\d{4})?"
    res = re.sub(pattern, r"+7(\2)\3-\4-\5\6", tel)
    contacts_list3[k] = contacts_list3[k][:z[4]]+res+contacts_list3[k][z[5]:]

del_list = []
# объединяем информацию по людям, которые кажутся одинаковыми
for i in range(11):
    poz1 = [m.start() for m in re.finditer(";", contacts_list3[i])]
    for j in range(i+1,12):
        poz2 = [m.start() for m in re.finditer(";", contacts_list3[j])]
        if contacts_list3[i][:poz1[1]] == contacts_list3[j][:poz2[1]]:
            del_list.append(j)
            for k in range(5):
                if contacts_list3[i][poz1[k]+1:poz1[k+1]] == "":
                    sss = ""
                    for t in range(poz2[k]+1,poz2[k+1]):
                        sss += contacts_list3[j][t]
                    contacts_list3[i] = contacts_list3[i][:poz1[1]]+contacts_list3[i][poz1[k]:] + sss + contacts_list3[i][poz1[k+1]:]

for i in del_list:
    contacts_list3[i] =""

for i in range(12-len(del_list)):
    if contacts_list3[i] == "":
        for j in range(i,11):
            contacts_list3[j] = contacts_list3[j+1]

print (contacts_list3)




    # TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
with open("phonebook.csv", "w") as f:
    datawriter = csv.writer(f, delimiter=',')
    # Вместо contacts_list подставьте свой список
    datawriter.writerows(contacts_list3)


