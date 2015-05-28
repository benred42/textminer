import textminer.regexes as reg
import re

def words(a_string):
    words_list = reg.words.findall(a_string)
    if words_list == []:
        return None
    else:
        return words_list


def phone_number(a_string):
    number = reg.phone.match(a_string)
    if number:
        phone_dict = {}
        area_code = re.search(r'\d+', number.group(1))
        phone_dict["area_code"] = area_code.group(0)
        phone_dict["number"] = "-".join(number.group(2, 3))
        print(number.group(1))
        return phone_dict
    else:
        return None


def money(a_string):
    money_check = reg.dollars.match(a_string)
    if money_check:
        money = money_check.group(0)
        money_dict = {}
        money_dict["currency"] = money[0]
        amount = re.findall(r'[\d.]+', money[1:])
        amount = "".join(amount)
        money_dict["amount"] = float(amount)
        return money_dict
    else:
        return None


def zipcode(a_string):
    zip_check = reg.ZIP.match(a_string)
    if zip_check:
        zips_dict = {}
        zips_dict["zip"] = zip_check.group(1)
        if zip_check.group(2):
            zips_dict["plus4"] = zip_check.group(2)[1:]
        else:
            zips_dict["plus4"] = None
        return zips_dict
    else:
        return None


def date(a_string):
    date_check = reg.date.match(a_string)
    if date_check:
        date_elements = list(date_check.groups())
        for index in range(len(date_elements)):
            if len(date_elements[index]) == 4:
                year = date_elements.pop(index)
                date_elements.append(year)
        date_dict = {}
        date_dict["month"] = int(date_elements[0])
        date_dict["day"] = int(date_elements[1])
        date_dict["year"] = int(date_elements[2])
        return date_dict
    else:
        return None


def email(a_string):
    email_check = reg.email.match(a_string)
    if email_check:
        email_dict = {}
        email_dict["local"] = email_check.group(1)
        email_dict["domain"] = email_check.group(2)
        return email_dict
    else:
        return None


def address(a_string):
    address_check = reg.address.match(a_string)
    if address_check:
        address_dict = {}
        addr = re.match(r'[\w\s]+', address_check.group(1))
        address_dict["address"] = addr.group(0)
        address_dict["city"] = address_check.group(2)
        address_dict["state"] = address_check.group(3)
        address_dict["zip"] = address_check.group(4)
        if address_check.group(5):
            address_dict["plus4"] = address_check.group(5)[1:]
        else:
            address_dict["plus4"] = None
        return address_dict
    else:
        return None


def date2(a_string):
    numerical = re.sub(r'[A-Za-z.]+', "1", a_string)
    date2_check = reg.hard_date.match(numerical)
    if date2_check:
        date_elements = list(date2_check.groups())
        for index in range(len(date_elements)):
            if len(date_elements[index]) == 4:
                year = date_elements.pop(index)
                date_elements.append(year)
        date_dict = {}
        date_dict["month"] = int(date_elements[0])
        date_dict["day"] = int(date_elements[1])
        date_dict["year"] = int(date_elements[2])
        return date_dict
    else:
        return None
