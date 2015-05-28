import textminer.regexes as reg

def binary(a_string):
    return reg.binary_numbers.match(a_string)


def binary_even(a_string):
    return reg.even_binary.match(a_string)


def hex(a_string):
    return reg.hex_code.match(a_string)


def word(a_string):
    return reg.word.match(a_string)


def words(a_string, count=None):
    word_list = reg.words.findall(a_string)
    if count:
        return len(word_list) == count
    else:
        return word_list


def phone_number(a_string):
    return reg.phone.match(a_string)


def money(a_string):
    return reg.dollars.match(a_string)


def zipcode(a_string):
    return reg.ZIP.match(a_string)


def date(a_string):
    return reg.date.match(a_string)


def date2(a_string):
    return reg.hard_date.match(a_string)


def email(a_string):
    return reg.email.match(a_string)


def address(a_string):
    return reg.address.match(a_string)