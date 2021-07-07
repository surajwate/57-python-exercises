def simple_math(first, second):
    return f"""{first} + {second} = {first + second}
{first} - {second} = {first - second}
{first} * {second} = {first * second}
{first} / {second} = {int(first / second)}"""


if __name__ == '__main__':
    f = int(input('What is the first number?'))
    s = int(input('What is the second number?'))
    print(simple_math(f, s))
