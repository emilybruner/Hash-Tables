def no_dups(s):
    # Implement me.
    storage = dict()

# Loop over the input string, assign each word in the string to a dictionary key
# for word in storage
    for word in s:
        if word not in storage:
            storage[word]
    # index = 0
    # for i in range(0, s):
    #     for j in range(0, i + 1):
    #         if (s[i] == s[j]):
    #             break
        
    #     if (j == i):
    #         s[index] = s[i]
    #         index += 1
    
    # return "".join(s[:index])


if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))