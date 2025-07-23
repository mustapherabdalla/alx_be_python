FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    global FAHRENHEIT_TO_CELSIUS_FACTOR
    temp_in_celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    print(f"{fahrenheit}°F is {temp_in_celsius}°C")

def convert_to_fahrenheit(celsius):
    global CELSIUS_TO_FAHRENHEIT_FACTOR
    temp_in_fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    print(f"{celsius}°C is {temp_in_fahrenheit}°F")


try:
    temperature = float(input("Enter the temperature to convert: "))
    conversion_type = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")

    if conversion_type == "C":
        convert_to_fahrenheit(temperature)
    elif conversion_type == "F":
        convert_to_celsius(temperature)
    else:
        print("Please enter either C or F.")

except ValueError:
    print("Invalid temperature. Please enter a numeric value.")

