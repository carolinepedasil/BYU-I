from math import pi
from datetime import datetime

def calculate_tire_volume(width, aspect_ratio, diameter):
    volume = (
        pi * (width ** 2) * aspect_ratio * (width * aspect_ratio + 2540 * diameter)
    ) / 10000000000
    return round(volume, 2)

width = int(input("Enter the width of the tire in mm (ex 205): "))
aspect_ratio = int(input("Enter the aspect ratio of the tire (ex 60): "))
diameter = int(input("Enter the diameter of the wheel in inches (ex 15): "))

volume = calculate_tire_volume(width, aspect_ratio, diameter)
print(f"The approximate volume is {volume} liters")

today_date = datetime.now().strftime("%Y-%m-%d")

with open("volumes.txt", "a") as file:
    file.write(f"{today_date}, {width}, {aspect_ratio}, {diameter}, {volume}\n")

# Exceeding the Requirements
buy_tires = input("Would you like to buy tires with these dimensions? (yes/no): ").strip().lower()
if buy_tires == "yes":
    phone_number = input("Please enter your phone number: ").strip()
    with open("volumes.txt", "a") as file:
        file.write(f"Phone number for purchase: {phone_number}\n")

print("Thank you! Data has been recorded.")
