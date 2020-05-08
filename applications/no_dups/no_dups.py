def no_dups(s):
    # Implement me.
    storage = dict()

    lower_case = s.lower()
    words = lower_case.split()

# Loop over the input string, assign each word in the string to a dictionary key
# for word in storage
    for word in words:
        if word not in storage:
            storage[word] += 1
        else:
            storage[word] = 1
    s = " ".join(storage.keys())
    return s



if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))