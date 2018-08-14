# -*- coding:utf-8 -*-
#工厂方法模式
from abc import ABCMeta,abstractmethod

class Payment(metaclass=ABCMeta):
	#抽象产品
	@abstractmethod
	def pay(self, money):
		pass
		
class AliPay(Payment):
	#具体产品
	def pay(self, money):
		print('使用支付宝支付%s元' %money)
		
class ApplePay(Payment):
	#抽象工厂
	def pay(self,money):
		print('使用苹果支付支付%s元' %money)
		
class PaymentFactory(metaclass=ABCMeta):
	#具体工场
	@abstractmethod
	def creat_payment(self):
		pass
		
