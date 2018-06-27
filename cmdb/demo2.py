#-*-coding:utf-8-*-

a=[('zhulei', '男'), ('hanqing', '男')]

lista=list(a)

def convertResult(param):
	result = []

	if not isinstance(param,list):

		print("参数应该是数据")

	else:
		for tup in param:
			dict = {}
			print(tup)
			print("result:",result)
			if isinstance(tup, tuple):
				print("i is tuple")
				for j in range(len(tup)):
					if j == 0:
						dict['name'] = tup[j]
					elif j == 1:
						dict['sex'] = tup[j]
					print('dict',dict)
			result.append(dict)
	return result

b=convertResult(a)

print(b)


