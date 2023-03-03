from pprint import pprint
# читаем адресную книгу в формате CSV в список contacts_list
import csv
import re

with open("phonebook_raw.csv", encoding='utf-8') as in_file:
    rows = csv.reader(in_file, delimiter=",")
    contacts_list = list(rows)
    contacts_list_updated = []

# TODO 1: выполните пункты 1-3 ДЗ
def fio():
    pattern = r'([А-Я])'
    substitution = r' \1'
    for column in contacts_list[1:]:
        line = column[0] + column[1] + column[2]
        if len((re.sub(pattern, substitution, line).split())) == 3:
            column[0] = re.sub(pattern, substitution, line).split()[0]
            column[1] = re.sub(pattern, substitution, line).split()[1]
            column[2] = re.sub(pattern, substitution, line).split()[2]
        elif len((re.sub(pattern, substitution, line).split())) == 2:
            column[0] = re.sub(pattern, substitution, line).split()[0]
            column[1] = re.sub(pattern, substitution, line).split()[1]
            column[2] = ''
        elif len((re.sub(pattern, substitution, line).split())) == 1:
            column[0] = re.sub(pattern, substitution, line).split()[0]
            column[1] = ''
            column[2] = ''
    return

def phone_number_formatting():
    phone_pattern = re.compile(
        r'(\+7|8)?\s*\(?(\d{3})\)?\s*\D?(\d{3})[-\s+]?(\d{2})-?(\d{2})((\s)?\(?(доб.)?\s?(\d+)\)?)?')
    phone_substitution = r'+7(\2)\3-\4-\5\7\8\9'
    for column in contacts_list:
        column[5] = phone_pattern.sub(phone_substitution, column[5])
    return

def duplicates_combining():
    for column in contacts_list[1:]:
        last_name = column[0]
        first_name = column[1]
        for contact in contacts_list[1:]:
            new_last_name = contact[0]
            new_first_name = contact[1]
            if last_name == new_last_name and first_name == new_first_name:
                for item in range(2, 7):
                    if contact[item] == '':
                        contact[item] = column[item]

    for contact in contacts_list:
        if contact not in contacts_list_updated:
            contacts_list_updated.append(contact)
    return contacts_list_updated


if __name__ == '__main__':
    fio()
    phone_number_formatting()
    duplicates_combining()

# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
with open("phonebook.csv", "w") as out_file:
    datawriter = csv.writer(out_file, delimiter=',')
    datawriter.writerows(contacts_list_updated)
pprint(contacts_list_updated)