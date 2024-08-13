def calculate_bmi(weight: float, height: float) -> float:
    return weight / height ** 2


def bmi_to_text(bmi_score: float) -> str:
    if bmi_score < 18.5:
        return "Underweight"
    elif 18.5 < bmi_score < 25:
        return "Normal"
    elif 25 < bmi_score < 30:
        return "Overweight"
    elif 30 < bmi_score:
        return "Obesity"
    else:
        return "Wrong data"


def test_correct_bmi():
    bmi = calculate_bmi(75, 1.82)
    assert 22 < bmi < 23
    assert bmi_to_text(bmi) == "Normal"


if __name__ == '__main__':
    weight = float(input("your weight [kg]: "))
    height = float(input("your height [m]: "))

    bmi = calculate_bmi(weight, height)
    bmi_text = bmi_to_text(bmi)

    # print(bmi)
    # print(bmi_text)
