def add(x, y):
    return x + y
print (add(4,5))

def new_add(x):
    def inner(y):
        return x + y
    return inner

print(new_add(4)(5))