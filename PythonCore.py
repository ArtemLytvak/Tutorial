# '380998759405', '818765347', '8867658976', '657658976'
# Japan	JP	+81
# Singapore	SG	+65
# Taiwan	TW	+886
# Ukraine	UA	+380
def sanitize_phone_number(phone):
    new_phone = (
        phone.strip()
        .removeprefix("+")
        .replace("(", "")
        .replace(")", "")
        .replace("-", "")
        .replace(" ", "")
    )

    return new_phone


def get_phone_numbers_for_countries(list_phones):

    country_phone_dict = {'JP': '81', 'SG': '65', 'TW': '886'}
    result = {'JP': [], 'SG': [], 'TW': [], 'UA': []}
    for tel in list_phones:
        x = sanitize_phone_number(tel)
        for country_code, phone_code in country_phone_dict.items():
            if x.startswith(phone_code):
                result[country_code].append(x)
                break
        else:
            result['UA'].append(x)

    return result


if __name__ == "__main__":
    x = get_phone_numbers_for_countries(['380998759405', '818765347', '8867658976', '657658976'])
    print(x)







