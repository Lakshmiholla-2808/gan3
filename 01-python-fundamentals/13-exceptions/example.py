class InvalidAge(Exception):
    pass

def read_age(text):
    try:
        age = int(text)
    except ValueError:
        raise InvalidAge(f"'{text}' is not a number")
    if age < 0:
        raise InvalidAge("age cannot be negative")
    return age

for value in ["25", "abc", "-3"]:
    try:
        print("ok", read_age(value))
    except InvalidAge as e:
        print("error:", e)
    finally:
        print("checked", value)
