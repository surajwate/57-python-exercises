def compound_interest(principal, rate_of_interest, number_of_years, compounding_per_year):
    final_amount = principal * ( 1 + (rate_of_interest/(compounding_per_year * 100)))**(number_of_years * compounding_per_year)
    final_amount = round(final_amount, 2)
    return f"""${principal} invested at {rate_of_interest}% for {number_of_years} years
compounded {compounding_per_year} times per year is ${final_amount}."""

if __name__ == '__main__':
    P = int(input("What is the principal amount? "))
    r = float(input("What is the rate? "))
    t = int(input("What is the number of years? "))
    n = int(input("What is the number of tiems the interest is compounded per year? "))
    print(compound_interest(P, r, t, n))