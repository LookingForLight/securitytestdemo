#-*-coding:utf-8-*-
from cmdb import commons



class Student:
    classroom = '101'
    address = 'beijing'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_age(self):
        print('%s: %s' % (self.name, self.age))

class Ground(Student):
	def __init__(self, name, age,weight):
		super(Ground,self).__init__(name, age)
		self.weight = weight

	def print_age(self):
		print('%s: %s: %s' % (self.name, self.age, self.weight))

class Animal:

	country = "china"
	def __init__(self,kind , weight):
		self.__kind = kind
		self.__weight = weight

	def get_kind(self):
		return self.__kind

	def get_weight(self):
		return self.__weight

	def set_kind(self,kind):
		self.__kind = kind

	def set_weight(self, weight):
		self.__weight = weight

	def del_kind(self):
		print("删除类型数据")

	kind = property(get_kind, set_kind ,del_kind,"类型")

li = Student("李四", 24)
zhang = Student("张三", 23)


print(Student.classroom)
print(li.classroom)

# 调用方法
li.print_age()
zhang.print_age()

zhu = Ground('zhulei','11','110')
zhu.print_age()

cat = Animal('cat','112')
print(cat.kind)
cat.kind = 114
print(cat.kind)
del cat.kind

print(Animal.__dict__)
print(cat.__dict__)

def run():
    inp = input("请输入您想访问页面的url：  ").strip()


if __name__ == '__main__':
    run()