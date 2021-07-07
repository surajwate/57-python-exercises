def quote(quote_said, author):
    return f'{author} says, "{quote_said}"'


if __name__ == '__main__':
    q = input('What is the quote?')
    a = input('Who said it?')
    print(quote(q, a))
