from pprint import pprint
import csv
import re

with open("phonebook_raw.csv", encoding="UTF-8") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)

phone_pattern = (
    r"(\+7|8)(\s*)(\(*)(\d{3})(\-*)(\)*)(\s*)(\d{3})(\-*)"
    r"(\s*)(\d{2})(\-*)(\s*)(\d{2})(\s*)(\(*)(доб\.)*(\s*)(\d+)*(\)*)"
)

phone_replace = r"+7(\4)\8-\11-\14\15\17\19"

contacts_list_new = list()
final_list = list()
for contacts in contacts_list:
    fio_list = " ".join(contacts[0:3]).split()
    if len(fio_list) != 3:
        fio_list.append("")
    full_fio_list = fio_list + contacts[3:]
    contact_string = ",".join(full_fio_list)
    contact_edit = re.sub(phone_pattern, phone_replace, contact_string)
    contact = contact_edit.split(",")
    contacts_list_new.append(contact)
    for c in contacts_list_new:
        for contact_in_final_list in final_list:
            if contact_in_final_list[:1] == c[:1]:
                final_list.remove(contact_in_final_list)
                c = [x if x != "" else y for x, y in zip(contact_in_final_list, c)]
        final_list.append(c)

with open("phonebook.csv", "w", encoding="UTF-8") as f:
    datawriter = csv.writer(f, delimiter=",")
    datawriter.writerows(final_list)
