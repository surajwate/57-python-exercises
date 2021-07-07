from datetime import date

def retirement_calculator(current_age, retirement_age):
    current_year = date.today().year
    retirement_years = retirement_age - current_age
    return f"""You have {retirement_years} years left until you can retire.
It's {current_year}, so you can retire in {current_year + retirement_years}."""


if __name__ == '__main__':
    age = int(input('What is your current age?'))
    retirement = int(input('At what age would you like to retire?'))
    print(retirement_calculator(age, retirement))
