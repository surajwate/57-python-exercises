def simple_interest(principle, rate_of_interest, number_of_years):
    final_amount = principle * (1 + (rate_of_interest/100 * number_of_years))
    final_amount = round(final_amount)
    return f"""After {number_of_years} years at {rate_of_interest}%, the investment will
be worth ${final_amount}."""

if __name__ == '__main__':
    P = int(input("Enter the principal: "))
    r = float(input("Enter the rate of interest(Like 15, not 0.15): "))
    t = int(input("Enter the number of years: "))
    print(simple_interest(P, r, t))