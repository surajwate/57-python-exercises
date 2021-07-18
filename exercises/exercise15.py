def password_validation(password):
    if password == "abc$123":
        return "Welcome!"
    else:
        return "I don't know you."


if __name__ == '__main__':
    passw = input("What is the password? ")
    print(password_validation(passw))
