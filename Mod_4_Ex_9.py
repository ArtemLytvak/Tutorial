def is_valid_pin_codes(pin_codes):
    a = False

    for i in pin_codes:
        print(len(i))
        x = pin_codes.count(i)
        if x == 1 and len(i) == 4 and type(i) == str and i.isdigit():
            a = True
        else:
            a = False

    print(a)
is_valid_pin_codes(['1101', '9034', '00112'])



















