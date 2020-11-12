# Program to check whether a phone number is valid or not
# need to install 'phonenumbers' prior to this - 'pip install phonenumbers'

import phonenumbers

# Parsing String to Phone number

phone_number = phonenumbers.parse("+6197087104")

# Validating a phone number

valid = phonenumbers.is_valid_number(phone_number)

# Checking possibility of a number

possible = phonenumbers.is_possible_number(phone_number)

# Printing the output

print(valid)
print(possible)