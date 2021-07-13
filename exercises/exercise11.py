def currency_conversion(euros, rate):
    dollars = euros * (rate/100)
    return f"""{euros} euros at an exchange rate of {rate} is
{dollars:.2f} U.S. dollars."""

if __name__ == '__main__':
    euros = int(input("How many euros are you exchanging? "))
    rate = float(input("What is the exchange rate? "))
    print(currency_conversion(euros, rate))