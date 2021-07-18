# Exercise 21: Numbers to Names

def number_to_name(number):
    months = ["January", "February", "March", "April", "May", "June",
              "July", "August", "September", "October", "November", "December"]
    numbers = [i for i in range(12)]
    mapped = zip(numbers, months)
    mapped = dict(mapped)
    return ("The name of the month is " + mapped[number-1] + ".")


def get_month():
    ans = True
    while ans:
        try:
            mn = int(input("Please enter the number of the month: "))

        except ValueError:
            print("Please enter numberical value between and including 1 and 12.")

        finally:
            if(mn >= 1 and mn <= 12):
                return mn
            elif(mn <= 1 or mn >= 12):
                print("Please enter value between and including 1 and 12.")
                ans = True


if __name__ == '__main__':
    mn = get_month()
    print(number_to_name(mn))
