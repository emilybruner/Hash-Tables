# Implement me.

def histogram():
    storage = dict()
    bad_chars = [':', ';', ',', '.', '-', '+', '=', '/', '\\', '|', '[ ]', '{ }', '*', '&', '"', '!', '?']

    with open('robin.txt', 'r') as f:
        for line in f:
            for word in line.split():
                word = ''.join(i for i in word if not i in bad_chars)
                word = word.lower()
                if word not in storage:
                    storage[word] = 1
                elif word in storage:
                    storage[word] += 1

    # Turn hashtable into list for sorting
    words = list(storage.items())
    words.sort(key=lambda v: v[0], reverse=False)
    words.sort(key=lambda v: v[1], reverse=True)
    for x in words:
        print(f"{x[0]} {'#' * x[1]}")

histogram()