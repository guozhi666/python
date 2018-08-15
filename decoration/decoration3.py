import datetime
import time

def logger(fn):
    def wrap(*args, **kwargs):
        print ("args={},kwargs={}".format(args,kwargs))
        start = datetime.datetime.now()
        ret = fn(*args,**kwargs)
        duration = (datetime.datetime.now() - start).total_seconds()
        print("function{} took{}s.".format(fn.__name__,duration))
        if duration>1:
            print("{} took {}s.".format(fn.__name__,duration))
        return ret
    return wrap

@logger
def add(x, y):
    print ('===call add===')
    time.sleep(2)
    return x + y
print (add(4,y=7))