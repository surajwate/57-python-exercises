# Exercise 17: Blood Alcohol Calculator

def blood_alcohol_calculator(alcohol_consumed, weight_in_pounds, gender, last_drink_hours):
    if gender == "M":
        r = 0.73
    if gender == "F":
        r = 0.66
    bac = ((alcohol_consumed * 5.14) / (weight_in_pounds * r)) - (0.015 * last_drink_hours)
    if bac < 0.08:
        return "legal"
    else:
        return "not legal"

def get_data():
    while True:
        try:
            alcohol_consumed = float(input("Total alcohol consumed : "))
            break
        except :
            print("\nPlease enter the value in float or integer.\n")

    while True:
        try:
            weight_in_pounds = float(input("Body weight in pounds : "))
            break
        except :
            print("\nPlease enter the value in float or integer.\n")

    while True:
        try:
            last_drink_hours = float(input("Number of hours since the last drink : "))
            break
        except :
            print("\nPlease enter the value in float or integer.\n")
    return (alcohol_consumed, weight_in_pounds, last_drink_hours)

if __name__ == '__main__':
    gender = input("Enter your gender (M/F) : ")
    alcohol_consumed, weight_in_pounds, last_drink_hours = get_data()
    print("It is " + blood_alcohol_calculator(alcohol_consumed, weight_in_pounds, gender, last_drink_hours) + " for you to drive.")