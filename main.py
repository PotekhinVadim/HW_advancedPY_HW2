from pprint import pprint
import csv
import re

with open("phonebook_raw.csv", encoding='UTF-8') as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)

name_pattern = r'^(\w+)(\s*)(\,?)(\w+)(\s*)(\,?)(\w*)(\,?)(\,?)(\,?)'
phone_pattern = r'(\+7|8)(\s*)(\(*)(\d{3})(\-*)(\)*)(\s*)(\d{3})(\-*)(\s*)'\
                r'(\d{2})(\-*)(\s*)(\d{2})(\s*)(\(*)(доб\.)*(\s*)(\d+)*(\)*)'

name_replace = r'\1\3\10\4\6\9\7\8'
phone_replace = r'+7(\4)\8-\11-\14\15\17\19'

contacts_list_new = list()
for contacts in contacts_list:
    contact_string = ','.join(contacts)
    contact_edit = re.sub(phone_pattern, phone_replace, contact_string)
    contact_edit = re.sub(name_pattern, name_replace, contact_string)
    contact = contact_edit.split(',')
    contacts_list_new.append(contact)

for i in contacts_list_new:
      for j in contacts_list_new:
        if i[0] == j[0]:
          if i[1] == '':
            i[1] = j[1]
          if i[2] == '':
            i[2] = j[2]
          if i[3] == '':
            i[3] = j[3]
          if i[4] == '':
            i[4] = j[4]
          if i[5] == '':
            i[5] = j[5]
          if i[6] == '':
            i[6] = j[6]
        contact_list = list()
        for contacts in contacts_list_new:
            if contacts not in contact_list:
                contact_list.append(contacts)
pprint(contact_list)


with open("phonebook.csv", 'w', encoding='UTF-8') as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(contact_list)