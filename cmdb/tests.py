from django.test import TestCase
from collections import Iterable
# Create your tests here.
from cmdb import commons
a = [1,2,3,4,5]

for i in a:
	print(i)

for i in range(len(a)):
	print(i,a[i])

x = 9

if x in a:
	print('True')


tpl = "i am {},age {},{}".format("seven",16,'alex')
print(tpl)

dic = {'Name': 'Jack', 'Age': 7, 'Class': 'First'}

for key in dic:
	print(key,dic[key])

for letter in 'Hello world':     # 第一个实例
   if letter == 'e':
      break
   print ('当前字母为 :', letter)

var = 10                    # 第二个实例
while var > 0:
   print ('当期变量值为 :', var)
   var -= 1
   if var == 5:
      break

def func(*args):
	for arg in args:

		print(arg)
func('a', 'b', 'c')
li = [1,2,3]
func(li)


def func(*args, **kwargs):

    for arg in args:
        print(arg)

    for kwg in kwargs:
        print(kwg, kwargs[kwg])

lis = [1, 2, 3]
dic = {
    'k1': 'v1',
    'k2': 'v2'
}

func(*lis, **dic)

a = 1

def func1():
    print(a)

func1()


name = 'jack'

def outer():
    name='tom'

    def inner():
        name ='mary'
        print(name)

    inner()

outer()

name ='jack'



def outer(func):
    def inner():
        print("认证成功！")
        result = func()
        print("日志添加成功")
        return result
    return inner

def outerdemo(func):
	print("认证成功")
	result = func()
	print("添加日志")
	return result

@outer
def f1():
    print("业务部门1数据接口......")


s = 'this is a test'
b = bytes(s,encoding='utf-8')

f = open('test.txt','wb')
f.write(b)
f.close()
