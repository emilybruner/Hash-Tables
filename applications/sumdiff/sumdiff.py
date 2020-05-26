#q = set(range(1, 10))
#q = set(range(1, 200))
q = (1, 3, 4, 7, 12)
​
def add(a, b):
    return f(a) + f(b)
​
def sub(c, d):
    return f(c) - f(d)
​
def f(x):
    return x * 4 + 6
​
hashtable = {}
​
min = float("inf")
​
for a in range(len(q)) :
​
    for b in range(a, len(q)):
        key = (q[a], q[b])
        result = add(q[a], q[b])
​
        if result < min:
            min = result
​
        if result not in hashtable:
            hashtable[result] = []
​
        if key != (q[b], q[a]):
            hashtable[result].append((q[b], q[a]))
​
        hashtable[result].append(key)
​
​
for c in range(len(q) - 1, -1, -1):
​
    for d in range(c, -1, -1):
        key = (q[c], q[d])
        result = sub(q[c], q[d])
​
        if result in hashtable:
            for element in hashtable[result]:
                print(element, key, result)
​
    if result < min:
