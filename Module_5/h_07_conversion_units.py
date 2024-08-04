# 1 mile = 1.609344 km
factor = 1.609344


def conversion_mile_to_km(miles: float) -> float:
    return round(miles * factor, 2)


def conversion_km_to_mile(km: float) -> float:
    return round(km / factor, 2)


print(f"1 mile = {conversion_mile_to_km(1)} km")
print(f"5 mile = {conversion_mile_to_km(5)} km")
print("- - - " * 5)
print(f"1 km = {conversion_km_to_mile(1)} mile")
print(f"10 km = {conversion_km_to_mile(10)} mile")

