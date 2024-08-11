def group_them(**kwargs):
    result = []
    for k, v in kwargs.items():
        result.append(f"{k.capitalize()} is {v}")

    return "\n".join(result)


def test_group_them():
    assert group_them() == ""
    assert group_them(wall="red") == "Wall is red"
    assert group_them(tomato="red", grass="green") == "Tomato is red\nGrass is green"
