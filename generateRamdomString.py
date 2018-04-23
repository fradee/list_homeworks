import random

def generate_random_string(stringLen):
    res = ''
    alphabet = 'abcdefghijklmnopqrstuvwxyz '
    for i in range(stringLen):
        res = res + alphabet[random.randrange(27)]

    return res

print(generate_random_string(255))