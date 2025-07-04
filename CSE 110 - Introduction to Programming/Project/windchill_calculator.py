def celsius_to_fahrenheit(celsius):
    """
    Convert Celsius to Fahrenheit.
    """
    fahrenheit = celsius * (9 / 5) + 32
    return fahrenheit

def calculate_wind_chill(temperature, wind_speed):
    """
    Calculate wind chill based on temperature (in Fahrenheit) and wind speed.
    Formula from the U.S. National Weather Service.
    """
    wind_chill = 35.74 + (0.6215 * temperature) - (35.75 * (wind_speed ** 0.16)) + (0.4275 * temperature * (wind_speed ** 0.16))
    return wind_chill

temp = float(input("What is the temperature? "))
scale = input("Fahrenheit or Celsius (F/C)? ").strip().upper()

if scale == "C":
    temp = celsius_to_fahrenheit(temp)
    print(f"Temperature converted to Fahrenheit: {temp:.2f}F")

print("\nWind Chill Values:")
for wind_speed in range(5, 65, 5):
    wind_chill = calculate_wind_chill(temp, wind_speed)
    print(f"At temperature {temp:.1f}F, and wind speed {wind_speed} mph, the windchill is: {wind_chill:.2f}F")
