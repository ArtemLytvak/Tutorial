# ['380998759405', '818765347', '8867658976', '657658976']
def sanitize_phone_number(phone):
    new_phone = (
        phone.strip()
        .replace("+", "")
        .replace("(", "")
        .replace(")", "")
        .replace("-", "")
        .replace(" ", "")
    )
    print(phone)
    return new_phone



def get_phone_numbers_for_countries(list_phones):
    print('s')

print(sanitize_phone_number(' +3 80()12 3)'))