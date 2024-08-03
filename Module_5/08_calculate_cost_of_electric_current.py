def calculation_cost(time: float, cost: float = 1.2):
    """
    This function calculates the cost of electricity

    :param time: How long does it run (give in hours)
    :param cost: How much 1kWh costs?
    :return: Total spent on electricity
    """
    return time * cost


print(calculation_cost(180 , 2))