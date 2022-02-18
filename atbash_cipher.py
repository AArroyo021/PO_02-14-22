atbash_table = {
    'A': 'Z', 'B': 'Y', 'C': 'X', 'D': 'W', 'E': 'V',
    'F': 'U', 'G': 'T', 'H': 'S', 'I': 'R', 'J': 'Q',
    'K': 'P', 'L': 'O', 'M': 'N', 'N': 'M', 'O': 'L',
    'P': 'K', 'Q': 'J', 'R': 'I', 'S': 'H', 'T': 'G',
    'U': 'F', 'V': 'E', 'W': 'D', 'X': 'C', 'Y': 'B', 'Z': 'A'
}


def atbash(message):
    message = list(message);
    for i, char in enumerate(message):
        if char.isupper():
            message[i] = atbash_table.get(message[i])
        elif char.islower():
            message[i] = atbash_table.get(message[i].upper()).lower()
    return "".join(message)


print(atbash("apple"))
print(atbash("Hello world!"))
print(atbash("Christmas is the 25th of December"))