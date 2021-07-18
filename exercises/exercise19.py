# Exercise 19: BMI Calculator

def bmi_calculator(weight, height):
    bmi = (weight/ (height * height)) * 703

    if(bmi <= 18.5):
        return "You are underweight. You should see your doctor."
    elif(bmi > 25):
        return "You are overweight. You should see your doctor."
    else:
        return "You are within the ideal weight range."


def get_input():
    while True:
        try:
            weight = float(input("Please enter your weight in pound: "))
            break
        except ValueError:
            print("\nPlease enter numeric value.\n")
    while True:
        try:
            height = float(input("Please enter your height in inch: "))
            break
        except ValueError:
            print("\nPlease enter numeric value.\n")

    return (weight, height)

if __name__ == '__main__':
    weight, height = get_input()
    print(bmi_calculator(weight, height))