def madlib(noun, verb, adverb, adjective):
    return f"Do you {verb} your {adjective} {noun} {adverb}? That's hilarious!"


if __name__ == '__main__':
    n = input("Enter a noun: ")
    v = input("Enter a verb: ")
    adj = input("Enter an adjective: ")
    adv = input("Enter an adverb: ")
    print(madlib(n, v, adv, adj))
