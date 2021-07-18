# Exercise 16: Legal Driving Age

def legal_driving_age(age):
    if (age < 16):
        return "You are not old enough to legally drive."
    else:
        return "You are old enough to legally drive."
    
if __name__ == '__main__':
    age = int(input("What is your age? "))
    print(legal_driving_age(age))