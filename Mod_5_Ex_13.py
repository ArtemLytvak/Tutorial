import re


def find_all_emails(text):
    result = re.findall(r"[A-z.]+\w+@[A-z]+\.[A-z]{2,}", str(text))

    print(result)
    return result
find_all_emails(["Ima.Fool@iana.org",
                "Ima.Fool@iana.o",
                "1Fool@iana.org",
                "first_last@iana.org",
                "first.middle.last@iana.or",
                "a@test.com",
                "abc111@test.com.net"])