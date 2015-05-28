import textminer.regexes as reg


def phone_numbers(a_string):
    numbers = reg.phone.findall(a_string)
    number_list = []
    for number in numbers:
        phone = number[0] + number[1] + "-" + number[2]
        number_list.append(phone)
    return number_list


def emails(a_string):
    emails = reg.email.findall(a_string)
    email_list = []
    for email in emails:
        email_address = email[0] + "@" + email[1]
        email_list.append(email_address)
    return email_list