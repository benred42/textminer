import re

binary_numbers = re.compile(r'\A[01]+')

even_binary = re.compile(r'\A[01]+0\Z')

hex_code = re.compile(r'\b[0-9A-Fa-f]+\b')

word = re.compile(r'(\b(?:\w*-)?[A-Za-z]+$\b)')

words = re.compile(r'(\b(?:\w*-)?[A-Za-z]+\b)')

phone = re.compile(r'(\(?\d{3}\)?[-. ]?)?(\d{3})[-. ]?(\d{4})')

dollars = re.compile(r'\$\d+(,[\d]{3})*(\.[\d]{2})?$')

ZIP = re.compile(r'(\d{5})(-\d{4})?$')

date = re.compile(r'(\d{1,4})[-/](\d{1,2})[-/](\d{2,4})')

hard_date = re.compile(r'([\w.]+)\s([\w]+),?\s(\d+)')

email = re.compile(r'([\w.]+)@(\w+\.\w{2,3})')

address = re.compile(r'(\d+\s[\w., ]+)\n?\s+([\w. ]+),\s([A-Z]{2})\s(\d{5})(-\d{4})?$')