
def hello(greet_name):
    return f'Hello {greet_name}, nice to meet you!'


if __name__ == '__main__':
    name = input("What is your name?")
    print(hello(name))
