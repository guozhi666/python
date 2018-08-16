def counter(base):
    def inc(step = 1):
        return  base + step
    return inc
foo = counter(5)
print foo()
f1 = counter(5)
f2 = counter(5)
print f1()
print f2()
print id(foo), id(f1), id(f2)