import re
from pprint import pprint
# читаем адресную книгу в формате CSV в список contacts_list
import csv

with open("phonebook_raw.csv") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)

c_l = []
#разбираемся с фамилия,имя,отчество, так, чтобы в итоге все были ф,и,о
def fiochange(input):
    t1 = re.sub(r'(\w+)\s(\w+)\s(\w*)[,;][,;][,;](\w*)[,;]([\w ]*)[,;]([0-9\-\+\(\)доб\. ]*)[,;]([a-zA-Z0-9_\.]*@?[a-zA-Z0-9]*\.?[a-zA-Z]*)',
    r'\1;\2;\3;\4;\5;\6;\7;', input)
    t2 = re.sub(r'(\w+)[,;](\w+)\s(\w*)[,;][,;](\w*)[,;]([\w ]*)[,;]([0-9\-\+\(\)доб\. ]*)[,;]([a-zA-Z0-9_\.]*@?[a-zA-Z0-9]*\.?[a-zA-Z]*)',
    r'\1;\2;\3;\4;\5;\6;\7;', t1)
    t3 = re.sub(r'(\w+)\s(\w+)[,;](\w*)[,;](\w*)[,;]([\w ]*)[,;]([0-9\-\+\(\)доб\. ]*)[,;]([a-zA-Z0-9_\.]*@?[a-zA-Z0-9]*\.?[a-zA-Z]*)',
    r'\1;\2;\3;\4;\5;\6;\7;', t2)
    return(t3)

# TODO 1: выполните пункты 1-3 ДЗ
for k in range(12):
    contacts_list1 = fiochange(contacts_list[k][0])
# избавляемся от скобок минусов и плюсов ( у некоторых написано 7 у некоторых +7)
    contacts_list2 = re.sub(r"[\(\)\-\+]*", "", contacts_list1)
    c_l.append(contacts_list2)

#борьба с пробелами в телефоне, но не в должности
    my_string = c_l[k]
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
        if c_l[k][i] != " ":
            tel += c_l[k][i]
# выставляем формат телефона
    pattern = r"(7|8)(\d{3})(\d{3})(\d{2})(\d{2})(доб.\d{4})?"
    res = re.sub(pattern, r"+7(\2)\3-\4-\5\6", tel)
    c_l[k] =c_l[k][:z[4]]+res+c_l[k][z[5]:]
    print (c_l[k])

#сравнение на совпадение по первым двум позициям
for i in range(12):
    for j in range(i,12):
        if c_l[i][0] == c_l[j][0] and c_l[i][1] == c_l[j][1]:
            for k in range(2,8):
                if c_l[i][k] == "":
                    c_l[i][k] = c_l[j][k]
            c_l[j] = ""

#print (c_l)






for i in range(len(c_l[1])):
    #pprint(c_l[1][i])
    z = [m.start() for m in re.finditer(c_l[1],';')]
#print(z)


for x in contacts_list:
    # pprint(x[0])
    result = re.sub(r'[\(\)]', "", x[0])
    # pprint(result)

    # TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
with open("phonebook.csv", "w") as f:
    datawriter = csv.writer(f, delimiter=',')
    # Вместо contacts_list подставьте свой список
    datawriter.writerows(contacts_list)


f