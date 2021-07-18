# Exercise 18: Temperature Converter

def temperature_converter(convert, temperature):
    if convert == "C":
        return ("Celsius", ((temperature - 32) * (5/9)))
    if convert == "F":
        return ("Fahrenheit", ((temperature * (9 / 5)) + 32))

if __name__ == '__main__':
    c = input("""Press C to convert from Fahrenheit to Celsius.
Press F to convert from Celsius to Fahrenheit.
Your choice:""").capitalize()
    change = ("Fahrenheit" if c == "C" else "Celsius")
    t = int(input(f"Please enter the temperature in {change}: "))
    print(f"The temperature in {temperature_converter(c, t)[0]} is {temperature_converter(c, t)[1]}.")