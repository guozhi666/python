# --coding:utf-8 --
import time

#装饰器
def deco(func):
	def wrapper():
		startTime = time.time()
		func()
		endTime = time.time()
		msecs = (endTime- startTime)*1000
		print ("time is %d ms" %msecs)
	return wrapper
@deco
def func():
	print ("hello")
	time.sleep(1)
	print ("world")

if __name__ == '__main__':
	f=func
	f()

print '---------------------------------------'



#带有参数的修饰器
def deco(func):
	def wrapper(a,b):
		startTime = time.time()
		func(a,b)
		endTime = time.time()
		msecs = (endTime- startTime)*1000
		print ("time is %d ms" %msecs)
	return wrapper
@deco
def func(a,b):
	print ("hello,here is a func for add:")
	time.sleep(1)
	print ("result is %d" %(a+b))

if __name__ == '__main__':
	f=func
	f(3,4)
print '---------------------------------------'
	
	
#带有不定参数的装饰器
def deco(func):
	def wrapper(*args, **kwargs):
		startTime = time.time()
		func(*args, **kwargs)
		endTime = time.time()
		msecs = (endTime- startTime)*1000
		print ("time is %d ms" %msecs)
	return wrapper
@deco
def func(a,b):
	print ("hello,here is a func for add:")
	time.sleep(1)
	print ("result is %d" %(a+b))

@deco
def func2(a,b,c):
	print("hello,there is a func for add :")
	time.sleep(1)
	print ('result is %d' %(a+b+c))
if __name__ == '__main__':
	f=func
	func2(3,4,5)
	f(3,4)