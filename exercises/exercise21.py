# Exercise 21: Numbers to Names

def number_to_name(number):
    months = ["January", "February", "March", "April", "May", "June",
              "July", "August", "September", "October", "November", "December"]
    numbers = [i for i in range(12)]
    mapped = zip(numbers, months)
    mapped = dict(mapped)
    return ("The name of the month is " + mapped[number-1] + ".")


if __name__ == '__main__':
    mn = int(input("Please enter the number of the month: "))
    print(number_to_name(mn))
