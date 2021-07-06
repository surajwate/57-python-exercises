def count(word):
    return f'{word} has {len(word)} characters.'

if __name__ == '__main__':
    print(count(input('What is the input string?')))