def check_pin(number_to_check: int or str) -> bool:
    if validate_length(number_to_check) and validate_digit(number_to_check):
        return True
    return False


def validate_digit(number_to_validate) -> bool:
    str_of_number = (str(number_to_validate))
    if str_of_number.isnumeric():
        return True


def validate_length(number_to_validate) -> bool:
    list_of_number = list(str(number_to_validate))
    if len(list_of_number) == 4:
        return True


pin_to_test1 = 1234
pin_to_test2 = "1a34"
pin_to_test3 = 12342
pin_to_test4 = "0034"
pin_to_test5 = ")@34"

print(f"PIN to test: {pin_to_test1} Is correct? {check_pin(pin_to_test1)}")
print(f"PIN to test: {pin_to_test2} Is correct? {check_pin(pin_to_test2)}")
print(f"PIN to test: {pin_to_test3} Is correct? {check_pin(pin_to_test3)}")
print(f"PIN to test: {pin_to_test4} Is correct? {check_pin(pin_to_test4)}")
print(f"PIN to test: {pin_to_test5} Is correct? {check_pin(pin_to_test5)}")
