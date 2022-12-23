#! /usr/bin/python3

import atheris
import sys
import string

with atheris.instrument_imports():
    import phonenumbers


country_codes = [a + b for a in string.ascii_uppercase for b in string.ascii_uppercase]
country_code_end = len(country_codes) - 1
phone_number_formats = [phonenumbers.PhoneNumberFormat.E164, phonenumbers.PhoneNumberFormat.INTERNATIONAL, phonenumbers.PhoneNumberFormat.NATIONAL, phonenumbers.PhoneNumberFormat.RFC3966]
phone_number_format_end = len(phone_number_formats) - 1

@atheris.instrument_func
def ph(fdp):
    country_code = country_codes[fdp.ConsumeIntInRange(0, country_code_end)]
    phone_number_len = fdp.ConsumeIntInRange(0, 16)
    try:
         return phonenumbers.parse(fdp.ConsumeUnicodeNoSurrogates(phone_number_len))
    except phonenumbers.NumberParseException:
        return None

@atheris.instrument_func
def TestOneInput(data):
    fdp = atheris.FuzzedDataProvider(data)
    
    # Checkers
    if phone := ph(fdp):
        phonenumbers.is_possible_number(phone)
    if phone := ph(fdp):
        phonenumbers.is_valid_number(phone)
    if phone := ph(fdp):
        phonenumbers.format_number(phone, phone_number_formats[fdp.ConsumeIntInRange(0, phone_number_format_end)])
    

def main():
    atheris.Setup(sys.argv, TestOneInput)
    atheris.Fuzz()


if __name__ == "__main__":
    main()
