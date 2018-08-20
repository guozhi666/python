#-*- coding:utf-8 -*-

import unittest
from mydic import Dict

class TestDict(unittest.TestCase):
    def test_init(self):
        d = Dict(a = 1, b = 'test')
        self.assertEqual(d.a, 1)  #判断d.a是否等于1
        self.assertEqual(d.a, 'test') #判断d.a是否等于test #-------------------
        self.assertTrue(isinstance(d, dict))#判断d是否是dict类型
    def test_key(self):
        d = Dict()
        d['key'] = 'value'
        self.assertEqual(d.key, 'value')
    def test_attr(self):
        d = Dict()
        d.key = 'value'
        self.assertTrue('key' in d)
        self.assertEqual(d['key'], 'value')
    def test_keyerror(self):
        d = Dict()
        with self.asserRaises(KeyError): #-------------------
            value = d['empty']
    def test_attrerror(self):
        d = Dict()
        with self.asserRaises(AttributeError):#-------------------
            value = d.empty

if __name__ =='__main__':
    unittest.main()